import os
import psutil
import subprocess

threshold=40
partition="/"

def cpu_utilization():
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30
    print('memory currently in use  :', memoryUse)


def check_memory_usage():
     df = subprocess.Popen(['df','-h'], stdout=subprocess.PIPE)
     for line in df.stdout:
        splitline = line.decode().split()
        if splitline[5] == partition:
            if int(splitline[4][:-1]) > threshold:
                print('Low disk space warning')

cpu_utilization()
check_memory_usage()


