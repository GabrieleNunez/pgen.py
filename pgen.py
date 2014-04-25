#Author: Gabriele M. Nunez (P13Darksight) (http://thecoconutcoder.com)
#This is my first python program so excuse any short comings!
#It's a password generator and it attempts to copy it to the clipboard.
#I will eventually make it cross compatible but I'm on Windows  so that is my primary focus and I'm happy with what I've made
#Simple, sweet, and python code is so clean!

import  random
import	sys
import	subprocess

passLen = 10
try:
	if len(sys.argv) > 0:
		passLen = int(sys.argv[1])
except: passLen = 10

tick = 0
password = ""

while tick < passLen:
	tick = tick + 1
	type = random.randrange(0,4)
	c = '';
	if type == 0:
		c = chr(random.randrange(0x61,0x7A))
	elif type == 1:
		c = chr(random.randrange(0x41,0x5A))
	elif type == 2:
		c = chr(random.randrange(0x30,0x39))
	else:
		c = chr(random.randrange(0x23,0x26))
	password += c
print("Your password is {0} and is being copied to the clipboard".format(password))
#This script is now Windows Only
#Sorry I don't know the mac or linux equiv to it at the moment
subprocess.check_call("echo {0} | clip".format(password),shell=True)