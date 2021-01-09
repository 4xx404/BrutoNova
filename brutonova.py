#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time
from crackHash import crackIt
from webBrute import bruteIt
from hashMD5 import hashDB

class bcolors:
	GREEN = '\033[1;39m'
	BLUE = '\033[1;34m'
	RED = '\033[1;31m'

banner = bcolors.RED + '''
    ___           __       _  __              
   / _ )______ __/ /____  / |/ /__ _  _____ _ 
  / _  / __/ // / __/ _ \/    / _ \ |/ / _ `/ 
 /____/_/  \_,_/\__/\___/_/|_/\___/___/\_,_/  
                                             
'''

def nova():
	os.system("clear")
	print(banner)
	print(bcolors.BLUE + " 1. " + bcolors.GREEN + "Crack SHA1 Hashes")
	print(bcolors.BLUE + " 2. " + bcolors.GREEN + "Brute Force Web Directories")
	print(bcolors.BLUE + " 3. " + bcolors.GREEN + "Add to MD5 Hash Database\n")
	print(bcolors.BLUE + " 0. " + bcolors.GREEN + "Quit\n")

	try:
		option = int(input(bcolors.BLUE + " Option: " + bcolors.GREEN))
		
		if option == 1:
			crackIt()

		elif option == 2:
			bruteIt()

		elif option == 3:
			hashDB()

		elif option == 0:
			print(bcolors.BLUE + " Quitting...")
			time.sleep(1)
			quit()

	except ValueError:
		print(bcolors.BLUE + " OPTION ERROR: " + bcolors.RED + "Invalid Option")
		input(bcolors.BLUE + " Press Enter to Continue...")
		nova()

if __name__ == '__main__':
	nova()
