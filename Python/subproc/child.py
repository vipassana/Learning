'''
This is the subprocess that reads stdin
'''

import sys
input = raw_input()
sys.stdout.write('Received: %s'%input)
