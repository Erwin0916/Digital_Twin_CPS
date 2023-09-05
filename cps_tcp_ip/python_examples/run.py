'''
Created on 2020. 5. 21.

@author: CTNguyen - conanttldvn@gmail.com
'''
import platform
import os.path
from os import path

print('Start config')


###############################################################################
# check if CoppeliaSimEdu was installed
try:
    if platform.system() =='Windows':
        print('Is CoppeliaSimEdu installed?     ',path.exists("C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\coppeliaSim.exe"))
    elif platform.system() =='Linux':
        print('Is CoppeliaSimEdu installed?     ',path.exists("C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\coppeliaSim.exe"))      # check for Ubuntu
        pass
except:
    print('Please install CoppeliaSim Edu software.')


###############################################################################
# copy remoteApi for python
import shutil
import pathlib
try:
    if platform.system() =='Windows':                  
        target = str(pathlib.Path(__file__).parent.absolute()) + '\\coppeliasim_utils\\remoteApi.dll'
        if path.exists(target):
            pass
        else:
            print('Copy remoteApi.dll')
            original = "C:\\Program Files\\CoppeliaRobotics\\CoppeliaSimEdu\\programming\\remoteApiBindings\\lib\\lib\\Windows\\remoteApi.dll"
            shutil.copyfile(original, target)
        
        target = str(pathlib.Path(__file__).parent.absolute()) + '\\sim.py'     
        if path.exists(target):
            pass
        else:  
            print('Copy sim.py')         
            original = "C:\\Program Files\\CoppeliaRobotics\\CoppeliaSimEdu\\programming\\remoteApiBindings\\python\\python\\sim.py"
            shutil.copyfile(original, target)
          
        target = str(pathlib.Path(__file__).parent.absolute()) + '\\simConst.py'      
        if path.exists(target):
            pass
        else: 
            print('Copy simConst.py')       
            original = "C:\\Program Files\\CoppeliaRobotics\\CoppeliaSimEdu\\programming\\remoteApiBindings\\python\\python\\simConst.py"        
            shutil.copyfile(original, target)        
        
    elif platform.system() =='Linux':
        #print('Copy remoteApi.so')
        #os.startfile("C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\coppeliaSim.exe")       # check for Ubuntu    
        pass
except:
    print('Can not copy remoteApi files.')


###############################################################################
# modify remoteApiConnections.txt
try:
    if platform.system() =='Windows':
        original    = "C:\\Program Files\\CoppeliaRobotics\\CoppeliaSimEdu\\remoteApiConnections.txt"
        target      = "C:\\Program Files\\CoppeliaRobotics\\CoppeliaSimEdu\\remoteApiConnections_origin.txt"        
        if (path.exists(target) and path.exists(original)):
            #print('already modified remoteApiConnections.txt')
            pass
        elif path.exists(original):
            print('backup remoteApiConnections.txt')                      
            os.rename(original,target)

            print('create new remoteApiConnections.txt')
            original    = "C:\\Program Files\\CoppeliaRobotics\\CoppeliaSimEdu\\remoteApiConnections_origin.txt"
            target      = "C:\\Program Files\\CoppeliaRobotics\\CoppeliaSimEdu\\remoteApiConnections.txt"         
            shutil.copyfile(original, target)

            print('modify new remoteApiConnections.txt')
            file = open(target,"r+")
            file.truncate(0)
            file.write('portIndex1_port             = 19997\n')
            file.write('portIndex1_debug            = true\n')
            file.write('portIndex1_syncSimTrigger   = true\n')
            file.close()        

    elif platform.system() =='Linux':   
        pass
except:
    print('Can not modify remoteApiConnections.txt.')


###############################################################################
# run python program on computer
import os
try:
    if platform.system() =='Windows':
        cmd_list = [
            "python gui_indy7.py"
        ] 
        if True:      
            for cmd in cmd_list:
                #print('command: ', cmd)
                returned_value = os.system(cmd)  # returns the exit code in unix
                #print('returned value: ', returned_value)          

    elif platform.system() =='Linux':    
        pass
except:
    print('Can not run gui_indy7.py file.')

print('End config')
