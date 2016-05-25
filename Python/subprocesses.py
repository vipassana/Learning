'''
Code to spawn a subprocess that monitors stdin while parent does other things
'''
import subprocess
import time

if __name__ == '__main__':
    i=0
    ip_tracker = subprocess.Popen(raw_input)
    while True:
        print i
        i += 1
        time.sleep(0.5)
