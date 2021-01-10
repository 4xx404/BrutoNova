#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time
from crackHashsha1 import crackItSha1
from crackHashsha224 import crackItSha224
from crackHashsha256 import crackItSha256
from crackHashsha384 import crackItSha384
from crackHashsha512 import crackItSha512
from crackHashsha3224 import crackItSha3224
from crackHashsha3256 import crackItSha3256
from crackHashsha3384 import crackItSha3384
from crackHashsha3512 import crackItSha3512
from hashMD5 import hashDB
from webBrute import bruteItWeb

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
	print(bcolors.BLUE + " 2. " + bcolors.GREEN + "Crack SHA224 Hashes")
	print(bcolors.BLUE + " 3. " + bcolors.GREEN + "Crack SHA256 Hashes")
	print(bcolors.BLUE + " 4. " + bcolors.GREEN + "Crack SHA384 Hashes")
	print(bcolors.BLUE + " 5. " + bcolors.GREEN + "Crack SHA512 Hashes")
	print(bcolors.BLUE + " 6. " + bcolors.GREEN + "Crack SHA3-224 Hashes")
	print(bcolors.BLUE + " 7. " + bcolors.GREEN + "Crack SHA3-256 Hashes")
	print(bcolors.BLUE + " 8. " + bcolors.GREEN + "Crack SHA3-384 Hashes")
	print(bcolors.BLUE + " 9. " + bcolors.GREEN + "Crack SHA3-512 Hashes")
	print(bcolors.BLUE + " 10. " + bcolors.GREEN + "Add to MD5 Hash Database")
	print(bcolors.BLUE + " 11. " + bcolors.GREEN + "Brute Force Web Directories\n")
	print(bcolors.BLUE + " 0. " + bcolors.GREEN + "Quit\n")

	try:
		option = int(input(bcolors.BLUE + " Option: " + bcolors.GREEN))

		if option == 1:
			crackItSha1()
			
		elif option == 2:
			crackItSha224()

		elif option == 3:
			crackItSha256()
			
		elif option == 4:
			crackItSha384()
			
		elif option == 5:
			crackItSha512()
			
		elif option == 6:
			crackItSha3224()
			
		elif option == 7:
			crackItSha3256()
			
		elif option == 8:
			crackItSha3384()
			
		elif option == 9:
			crackItSha3512()
		
		elif option == 10:
			hashDB()
		
		elif option == 11:
			bruteItWeb()

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
