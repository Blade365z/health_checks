import os
import getpass
import psutil
import subprocess
import socket
import platform
import datetime


threshold_value=40
partition="/"




def check_no_network():
    """Returns true if it fails to resolve Google;s url , false otherwise"""
    try:
        socket.gethostbyname("www.google.com")
        print('CONNECTED TO NETWORK...')
        return False 
    except:
        return True

def os_specs():
    print('Hello',getpass.getuser())
    print('Time :',datetime.datetime.now())
    print('OS : ',platform.system(),'',platform.release())


def cpu_utilization():
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30
    print('Memory currently in use  :', memoryUse)


def check_memory_usage():
     df = subprocess.Popen(['df','-h'], stdout=subprocess.PIPE)
     for line in df.stdout:
        splitline = line.decode().split()
        if splitline[5] == partition:
            if int(splitline[4][:-1]) > threshold_value:
                print('Low disk space alert !')



print('--------------------------------------------')
os_specs()
cpu_utilization()
check_memory_usage()
check_no_network()

print('--------------------------------------------')
