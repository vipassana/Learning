'''
Code playing with subprocess
'''
import subprocess
import time

if __name__ == '__main__':
    i=0
    subprocess.Popen(['python', 'child.py'], shell=True, stdin=subprocess.PIPE)
    while True:
        print i
        i += 1
        time.sleep(0.5)
