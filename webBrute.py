#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
import sys, os, time
import requests

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

def bruteItWeb():
	os.system('clear')
	print(banner)
	print(bcolors.BLUE + " [" + bcolors.GREEN + "?" + bcolors.BLUE + "] Enter " + bcolors.GREEN + "#//" + bcolors.BLUE + " to return to nova " + bcolors.BLUE + "[" + bcolors.GREEN + "?" + bcolors.BLUE + "]")
	print(bcolors.BLUE + " [" + bcolors.GREEN + "?" + bcolors.BLUE + "] Make sure to include http/https in Target URL [" + bcolors.GREEN + "?" + bcolors.BLUE + "]")
		
	webhost = input(bcolors.BLUE + " Target URL: " + bcolors.GREEN)
	
	if webhost == "#//":
		from brutonova import nova
		nova()
	else:
		wordlist = input(bcolors.BLUE + " Local Wordlist: " + bcolors.GREEN)
		words = open(wordlist, "r+")
		print(bcolors.BLUE + "\n [" + bcolors.GREEN + "?" + bcolors.BLUE + "] Leave Extension empty for directories only [" + bcolors.GREEN + "?" + bcolors.BLUE + "]")
		ext = str(input(bcolors.BLUE + " Extension: " + bcolors.GREEN))
		if ext == "":
			ext = ""
		else:
			if ext[0] == ".":
				ext = ext
			else:
				print(bcolors.BLUE + " EXTENSION ERROR: " + bcolors.RED + "Include dot in Extension")
				input(bcolors.BLUE + " Press Enter to Continue...")
				bruteItWeb()

		for word in words:
			word = word.split("\n")
			url = webhost + "/" + str(word[0]) + ext
			status = bcolors.BLUE + " Testing Directory: " + bcolors.GREEN + url
			print(status)

			try:
				response = requests.get(url)				
				if(response.status_code == 200):
					print(bcolors.BLUE + " Match Found: " + bcolors.GREEN + url + " ::" + bcolors.BLUE + "Status Code("+bcolors.GREEN+str(response.status_code)+bcolors.BLUE+")")
				
				elif(response.status_code == 301):
					print(bcolors.BLUE + " Match Found: " + bcolors.GREEN + url + " ::" + bcolors.BLUE + "Status Code("+bcolors.GREEN+str(response.status_code)+bcolors.BLUE+")")


				elif(response.status_code == 302):
					print(bcolors.BLUE + " Match Found: " + bcolors.GREEN + url + " ::" + bcolors.BLUE + "Status Code("+bcolors.GREEN+str(response.status_code)+bcolors.BLUE+")")


				elif(response.status_code == 410):
					print(bcolors.BLUE + " Match Found: " + bcolors.GREEN + url + " ::" + bcolors.BLUE + "Status Code("+bcolors.GREEN+str(response.status_code)+bcolors.BLUE+")")


				elif(response.status_code == 500):
					print(bcolors.BLUE + " Match Found: " + bcolors.GREEN + url + " ::" + bcolors.BLUE + "Status Code("+bcolors.GREEN+str(response.status_code)+bcolors.BLUE+")")


				elif(response.status_code == 503):
					print(bcolors.BLUE + " Match Found: " + bcolors.GREEN + url + " ::" + bcolors.BLUE + "Status Code("+bcolors.GREEN+str(response.status_code)+bcolors.BLUE+")")

				else:
					pass
			
			except Exception:
				print(bcolors.BLUE + " HOST ERROR: " + bcolors.RED + " Failed to Connect")
				input(" Press Enter to Continue...")
				bruteItWeb()

		print(bcolors.BLUE + "\n [" + bcolors.GREEN + "*" + bcolors.BLUE + "] Completed Brute Force [" + bcolors.GREEN + "*" + bcolors.BLUE + "]")
		input(" Press Enter to Continue...")
		bruteItWeb()
