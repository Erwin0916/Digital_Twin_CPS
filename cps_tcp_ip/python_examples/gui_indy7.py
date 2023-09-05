'''
Author: Marks Calderon Niquin
Email: markscalderonniquin@gmail.com
github: hypagetech
Program to control kuka arm robot on CoppeliaSim through sliders GUI with TKinder
'''

import sys
import os

os.chdir("../")
path1 = os.getcwd()
print(path1)
os.chdir("coppeliasim_utils")
path2 = os.getcwd()
print(path2)

sys.path.append(path1)
sys.path.append(path2)

from tkinter import *
from tkinter import messagebox
from coppeliasim_utils import sim
import time
import math

root = Tk()

class GUI(Frame):
    scales_l = []
    labels_l = []
    handles = []
    boolConnect = False
    clientID = -1
    base = 'joint'
    #final = 'LBR_iiwa_14_R820_connection'

    def __init__(self):
        super().__init__()
        self.initUI()
        #sim.simxFinish(-1) #clean all ports

    def initUI(self):
        self.master.title("ARM Robot control")
        for i in range(6):
            #tit = "M"+str(i+1)
            tit = "M"+str(i)
            w_label = Label(self.master, text=tit).grid(row=i, column=0, pady=4, padx = 4)
            win = Scale(self.master, from_=-180, to=180, tickinterval= 30, orient=HORIZONTAL, resolution=10, length=450, command=lambda value, name=i: self.onScale(name, value))
            win.set(0)
            win.grid(row=i, column=1)

            self.scales_l.append(win)
            self.labels_l.append(w_label)

        self.conectar = Button(self.master, text ="Connector", command = self.onConnect)
        self.conectar.grid(row=8,column=1)

    def onScale(self, name,value):
        if(self.clientID != -1):
            print("{} : {}".format(name, value))
            obj = self.handles[int(name)]
            ang = float(value)*math.pi/180
            sim.simxSetJointTargetPosition(self.clientID, obj ,ang ,sim.simx_opmode_oneshot)
            #print(self.objFinal)
            #pos = sim.simxGetObjectPosition(self.clientID, self.objFinal, -1, sim.simx_opmode_streaming )
            #print(pos)



    def onConnect(self):
        if self.clientID != -1:
            return
        
        # Close any open connections
        sim.simxFinish(-1) 

        # Connect to the V-REP continuous server
        #self.clientID = sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
        self.clientID = sim.simxStart('127.0.0.1',19998,True,True,5000,5) # Connect to CoppeliaSim

        if self.clientID == -1:
            messagebox.showinfo( "It can not be connected.")
        else:            
            print('Connected to remote API server of CoppeliaSim')
            # --------------------- Start the simulation    
            #sim.simxStartSimulation(self.clientID, sim.simx_opmode_oneshot)
            sim.simxStartSimulation(self.clientID, sim.simx_opmode_blocking)

            for i in range(6):
                #j = i + 1
                nom = self.base + str(i)
                print(nom)
                result, handle=sim.simxGetObjectHandle(self.clientID, nom, sim.simx_opmode_blocking)
                if result != sim.simx_return_ok:
                    raise Exception('could not get object handle for first joint')                
                else:
                    self.handles.append(handle)
                    sim.simxSetJointTargetPosition(self.clientID, handle ,0.0 ,sim.simx_opmode_oneshot)
            #self.objFinal = sim.simxGetObjectHandle(self.clientID, 'LBR_iiwa_14_R820_link8', sim.simx_opmode_oneshot_wait)
            #print(self.objFinal)
            time.sleep(1)
            print("Connected and sent command to the motor.")

def close_window():
  print("Close all ports")
  sim.simxFinish(-1) #clean all ports
  root.destroy()

def main():
    root.protocol("WM_DELETE_WINDOW", close_window)
    ex = GUI()
    root.geometry("500x500")
    root.mainloop()


if __name__ == '__main__':
    main()
