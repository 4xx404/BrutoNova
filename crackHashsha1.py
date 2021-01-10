#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen, hashlib
import sys, os, time

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

def crackItSha1():
	os.system('clear')
	print(banner)
	print(bcolors.BLUE + " [" + bcolors.GREEN + "?" + bcolors.BLUE + "] Enter " + bcolors.GREEN + "#//" + bcolors.BLUE + " to return to menu " + bcolors.BLUE + "[" + bcolors.GREEN + "?" + bcolors.BLUE + "]")
	
	uhash = str(input(bcolors.BLUE + " SHA1 Hash: " + bcolors.GREEN))
	if uhash == "#//":
		from brutonova import nova
		nova()
	elif len(uhash) != 40:
		print(bcolors.BLUE + " HASH ERROR: " + bcolors.RED + " Invalid SHA1 Hash")
		input(bcolors.BLUE + " Press Enter to Continue...")
		crackItSha1()
	else:
		print(bcolors.BLUE + " 1. " + bcolors.GREEN + "URL Wordlist")
		print(bcolors.BLUE + " 2. " + bcolors.GREEN + "Local Wordlist\n")
		woption = int(input(bcolors.BLUE + " Option: " + bcolors.GREEN))

		if woption == 1:
			wordlist = input(bcolors.BLUE + " URL Wordlist: " + bcolors.GREEN)
			passwords = str(urlopen(wordlist).read(), 'utf-8')

		elif woption == 2:
			try:
				wordlist = input(bcolors.BLUE + " Local Wordlist: " + bcolors.GREEN)
				passwords = open(wordlist).read()
			except FileNotFoundError as e:
				print(bcolors.BLUE + " FILE ERROR: " + bcolors.RED + "File Not Found")
				input(bcolors.BLUE + "Press Enter to Continue...")
				crackItSha1()

		else:
			print(bcolors.BLUE + " OPTION ERROR: " + bcolors.RED + "Invalid Option")
			input(bcolors.BLUE + "Press Enter to Continue...")
			crackItSha1()

		for pw in passwords.split('\n'):
			tryHash = hashlib.sha1(bytes(pw, 'utf-8')).hexdigest()
	
			if tryHash == uhash:
				print(bcolors.BLUE + "\n Matched Password: [" + bcolors.GREEN + "*" + bcolors.BLUE + "] " + bcolors.GREEN + str(pw) + bcolors.BLUE + " [" + bcolors.GREEN + "*" + bcolors.BLUE + "]")
				input(bcolors.BLUE + " Press Enter to Continue...")
				crackItSha1()

			elif tryHash != uhash:
				print(bcolors.BLUE + " Trying Password: " + bcolors.RED + str(pw) + bcolors.BLUE + " 		[" + bcolors.RED + "!" + bcolors.BLUE + "] Does NOT match [" + bcolors.RED + "!" + bcolors.BLUE + "]")

		print(bcolors.BLUE + "\n [" + bcolors.RED + "!" + bcolors.BLUE + "] Matched Password: " + bcolors.RED + "Not Found " + bcolors.BLUE + "[" + bcolors.RED + "!" + bcolors.BLUE + "]")
		input(bcolors.BLUE + "Press Enter to Continue...")
		crackItSha1()
