#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, time
from modules.stylesheet.Styling import bc, sd
banner, sBan, eBan, iBan, menuOptions, md5Options = sd.banner.logo, sd.sBan, sd.eBan, sd.iBan, sd.menuOptions, sd.md5Options
from modules.crackers.sha1 import sha1_hash
from modules.crackers.sha224 import sha224_hash
from modules.crackers.sha256 import sha256_hash
from modules.crackers.sha384 import sha384_hash
from modules.crackers.sha512 import sha512_hash
from modules.crackers.sha3224 import sha3224_hash
from modules.crackers.sha3256 import sha3256_hash
from modules.crackers.sha3384 import sha3384_hash
from modules.crackers.sha3512 import sha3512_hash
from modules.database.md5_db import hash_db_MD5
from modules.bruters.web_directory import webBrute
from modules.bruters.ftp import ftpBrute

os.system('clear')
print(banner)

def brutoNova():
	for o, d in menuOptions.items():
		if(d != 'Quit'):
			print(' ' + bc.BC + str(o) + '. ' + bc.GC + d)
		else:
			print('\n ' + bc.BC + str(o) + '. ' + bc.RC + d)

	try:
		option = int(input(bc.BC + '\n Option: ' + bc.GC))
		os.system('clear')
		print(banner)
	except ValueError:
		os.system('clear')
		print(banner)
		print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
		brutoNova()
	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		quit()
	print(bc.BC + "\n [" + bc.GC + "?" + bc.BC + "] Enter " + bc.GC + "#//" + bc.BC + " to return to menu")
	if(option == 0):
		os.system('clear')
		print(banner)
		quit()
	elif(option == 1):
		try:
			uhash = str(input(bc.BC + " SHA1 Hash: " + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(uhash == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		elif(len(uhash) != 40):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Invalid SHA1 Hash\n')
			brutoNova()
		else:
			if(uhash != '' or uhash != ' '):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()
				if(woption == 1):
					sha1 = sha1_hash(uhash)
					sha1.crack(woption)
				elif(woption == 2):
					sha1 = sha1_hash(uhash)
					sha1.crack(woption)
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()				
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + " ERROR: " + bc.BC + " Invalid SHA1 Hash\n")
				brutoNova()
	elif(option == 2):
		try:
			uhash = str(input(bc.BC + " SHA224 Hash: " + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(uhash == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		elif(len(uhash) != 56):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Invalid SHA224 Hash\n')
			brutoNova()
		else:
			if(uhash != '' or uhash != ' '):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()

				if(woption == 1):
					sha224 = sha224_hash(uhash)
					sha224.crack(woption)
				elif(woption == 2):
					sha224 = sha224_hash(uhash)
					sha224.crack(woption)
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()				
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + " ERROR: " + bc.BC + " Invalid SHA224 Hash\n")
				brutoNova()
	elif(option == 3):
		try:
			uhash = str(input(bc.BC + " SHA256 Hash: " + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(uhash == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		elif(len(uhash) != 64):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Invalid SHA256 Hash\n')
			brutoNova()
		else:
			if(uhash != '' or uhash != ' '):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()

				if(woption == 1):
					sha256 = sha256_hash(uhash)
					sha256.crack(woption)
				elif(woption == 2):
					sha256 = sha256_hash(uhash)
					sha256.crack(woption)
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()				
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + " ERROR: " + bc.BC + " Invalid SHA256 Hash\n")
				brutoNova()
	elif(option == 4):
		try:
			uhash = str(input(bc.BC + " SHA384 Hash: " + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(uhash == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		elif(len(uhash) != 96):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Invalid SHA384 Hash\n')
			brutoNova()
		else:
			if(uhash != '' or uhash != ' '):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()

				if(woption == 1):
					sha384 = sha384_hash(uhash)
					sha384.crack(woption)
				elif(woption == 2):
					sha384 = sha384_hash(uhash)
					sha384.crack(woption)
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()				
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + " ERROR: " + bc.BC + " Invalid SHA256 Hash\n")
				brutoNova()
	elif(option == 5):
		try:
			uhash = str(input(bc.BC + " SHA512 Hash: " + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(uhash == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		elif(len(uhash) != 128):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Invalid SHA512 Hash\n')
			brutoNova()
		else:
			if(uhash != '' or uhash != ' '):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()

				if(woption == 1):
					sha512 = sha512_hash(uhash)
					sha512.crack(woption)
				elif(woption == 2):
					sha512 = sha512_hash(uhash)
					sha512.crack(woption)
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()				
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + " ERROR: " + bc.BC + " Invalid SHA512 Hash\n")
				brutoNova()
	elif(option == 6):
		try:
			uhash = str(input(bc.BC + " SHA3-224 Hash: " + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(uhash == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		elif(len(uhash) != 56):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Invalid SHA3-224 Hash\n')
			brutoNova()
		else:
			if(uhash != '' or uhash != ' '):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()

				if(woption == 1):
					sha3224 = sha3224_hash(uhash)
					sha3224.crack(woption)
				elif(woption == 2):
					sha3224 = sha3224_hash(uhash)
					sha3224.crack(woption)
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()				
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + " ERROR: " + bc.BC + " Invalid SHA3-224 Hash\n")
				brutoNova()
	elif(option == 7):
		try:
			uhash = str(input(bc.BC + " SHA3-256 Hash: " + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(uhash == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		elif(len(uhash) != 64):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Invalid SHA3-256 Hash\n')
			brutoNova()
		else:
			if(uhash != '' or uhash != ' '):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()

				if(woption == 1):
					sha3256 = sha3256_hash(uhash)
					sha3256.crack(woption)
				elif(woption == 2):
					sha3256 = sha3256_hash(uhash)
					sha3256.crack(woption)
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()				
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + " ERROR: " + bc.BC + " Invalid SHA3-256 Hash\n")
				brutoNova()
	elif(option == 8):
		try:
			uhash = str(input(bc.BC + " SHA3-384 Hash: " + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(uhash == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		elif(len(uhash) != 96):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Invalid SHA3-384 Hash\n')
			brutoNova()
		else:
			if(uhash != '' or uhash != ' '):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()

				if(woption == 1):
					sha3384 = sha3384_hash(uhash)
					sha3384.crack(woption)
				elif(woption == 2):
					sha3384 = sha3384_hash(uhash)
					sha3384.crack(woption)
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()				
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + " ERROR: " + bc.BC + " Invalid SHA3-384 Hash\n")
				brutoNova()
	elif(option == 9):
		try:
			uhash = str(input(bc.BC + " SHA3-512 Hash: " + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(uhash == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		elif(len(uhash) != 128):
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Invalid SHA3-512 Hash\n')
			brutoNova()
		else:
			if(uhash != '' or uhash != ' '):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()

				if(woption == 1):
					sha3512 = sha3512_hash(uhash)
					sha3512.crack(woption)
				elif(woption == 2):
					sha3512 = sha3512_hash(uhash)
					sha3512.crack(woption)
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()				
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + " ERROR: " + bc.BC + " Invalid SHA3-512 Hash\n")
				brutoNova()
	elif(option == 10):
		md5db = hash_db_MD5()
		print()
		for o, d in md5Options.items():
			print(' ' + bc.BC + str(o) + '. ' + bc.GC + d)

		try:
			md5option = str(input(bc.BC + '\n Option: ' + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(md5option == '1'):
			#Add Single MD5 Hash to Database
			try:
				plainText = input(bc.BC + ' Enter Word as Plain-Text: ' + bc.GC)
			except KeyboardInterrupt:
				os.system('clear')
				print(banner)
				brutoNova()
			if(plainText == ''):
				os.system('clear')
				print(banner)
				print(bc.BC + ' ERROR: ' + bc.RC + ' Hash value cannot be empty\n')
				brutoNova()
			else:
				md5db.single_word(plainText)
		elif(md5option == '2'):
			try:
				wordlist = str(input(bc.BC + ' Local Wordlist: ' + bc.GC))
			except KeyboardInterrupt:
				os.system('clear')
				print(banner)
				brutoNova()
			if(wordlist == ''):
				print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Wordlist value cannot be empty')
				input(bc.BC + ' Press Enter to Continue...\n')
				brutoNova()
			else:
				Words = []
				try:
					x = open(wordlist, 'r+')
					words = x.readlines()
					for word in words:
						Words.append(word.replace('\n', ''))
				except Exception:
					print(bc.BC + ' FILE ERROR: ' + bc.RC + 'Failed to open ' + wordlist)
					input(bc.BC + ' Press Enter to Continue...\n')
					brutoNova()
				
				md5db.wordlist(wordlist, *Words)
		elif(md5option == '3'):
			os.system('clear')
			print(banner)
			print(bc.BC + '\n 1. ' + bc.GC + 'Search Plain Text')
			print(bc.BC + ' 2. ' + bc.GC + 'Search Hash\n')
			try:
				hashOption = int(input(bc.BC + ' Option: ' + bc.GC))
			except ValueError:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
				brutoNova()
			except KeyboardInterrupt:
				os.system('clear')
				print(banner)
				brutoNova()
			if(hashOption == 1):
				try:
					plainText = str(input(bc.BC + ' Plain-Text to Search: ' + bc.GC))
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()
				if(plainText == ''):
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Plain-Text value cannot be empty\n')
					brutoNova()
				else:
					hashSearch = ''
					md5db.search_hash(plainText, hashSearch)
			elif(hashOption == 2):
				hashSearch = str(input(bc.BC + ' Hash to Search: ' + bc.GC))
				if(hashSearch == ''):
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Hash value cannot be empty\n')
					brutoNova()
				else:
					plainText = ''
					md5db.search_hash(plainText, hashSearch)
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
				brutoNova()
		elif(md5option == '#//'):
			os.system('clear')
			print(banner)
			brutoNova()
		else:
			os.system('clear')
			print(banner)
			print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option')
			brutoNova()
	elif(option == 11):
		print(iBan + ' Include ' + bc.GC + 'http://' + bc.BC + ' || ' + bc.GC + 'https://' + bc.BC + ' in Target URL')
		try:
			webhost = str(input(bc.BC + ' Target URL: ' + bc.GC))
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
		if(webhost == "#//"):
			os.system('clear')
			print(banner)
			brutoNova()
		else:
			if(webhost.startswith('http://') or webhost.startswith('https://')):
				print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
				print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
				try:
					woption = int(input(bc.BC + ' Option: ' + bc.GC))
				except ValueError:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Option value must be INTEGER\n')
					brutoNova()
				except KeyboardInterrupt:
					os.system('clear')
					print(banner)
					brutoNova()
				if(woption == 1):
					webbrute = webBrute(webhost, woption)
					webbrute.bruteForce()
				elif(woption == 2):
					webbrute = webBrute(webhost, woption)
					webbrute.bruteForce()
				else:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option\n')
					brutoNova()
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Target URL, use ' + bc.GC + 'http://' + bc.BC + ' || ' + bc.GC + 'https://')
				brutoNova()
	elif(option == 12):
		try:
			host = str(input(bc.BC + ' Target IP: ' + bc.GC))
			if(host == '#//'):
				os.system('clear')
				print(banner)
				brutoNova()
			elif(host == '' or host == ' '):
				os.system('clear')
				print(banner)
				print('\n' + eBan + bc.RC + ' ERROR: ' + bc.BC + 'Host value cannot be empty\n')
				brutoNova()
			else:
				host = host

			user = str(input(bc.BC + ' Username(Single): ' + bc.GC))
			if(user == '#//'):
				os.system('clear')
				print(banner)
				brutoNova()
			elif(user == ''):
				os.system('clear')
				print(banner)
				print('\n' + eBan + bc.RC + ' ERROR: ' + bc.BC + 'Username value cannot be empty\n')
				brutoNova()
			else:
				user = user
				
			print(bc.BC + '\n 1. ' + bc.GC + 'Online Wordlist')
			print(bc.BC + ' 2. ' + bc.GC + 'Local Wordlist\n')
			woption = str(input(bc.BC + ' Option: ' + bc.GC))		
			if(woption == '#//'):
				os.system('clear')
				print(banner)
				brutoNova()
			elif(woption == '' or woption == ' '):
				os.system('clear')
				print(banner)
				print(bc.BC + bc.RC + ' ERROR: ' + bc.BC + 'Option value cannot be empty & must be INTEGER\n')
				brutoNova()
			elif(woption == '1'):
				wopt = woption
			elif(woption == '2'):
				wopt = woption
			else:
				os.system('clear')
				print(banner)
				print(bc.BC + bc.RC + ' ERROR: ' + bc.BC + 'Option value cannot be empty & must be INTEGER\n')
				brutoNova()

			wordlist = str(input(bc.BC + ' Wordlist: ' + bc.GC))
			if(wordlist == '#//'):
				os.system('clear')
				print(banner)
				brutoNova()
			elif(wordlist == ''):
				os.system('clear')
				print(banner)
				print(bc.BC + bc.RC + ' ERROR: ' + bc.BC + 'Wordlist value cannot be empty\n')
				brutoNova()
			else:
				wordlist = wordlist
			
			print('\n' + iBan + ' Leave empty to use your single username')
			unameWordlist = str(input(bc.BC + ' Username Wordlist(Multiple): ' + bc.GC))
			if(wordlist == '#//'):
				os.system('clear')
				print(banner)
				brutoNova()
			elif(wordlist == ''):
				unameWordlist = ''
			else:
				ftp_server = ftpBrute(host, user)
				ftp_server.bruteForce(wordlist, wopt, unameWordlist)

		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			brutoNova()
	else:
		os.system('clear')
		print(banner)
		print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Invalid Option, avaliable options 1-12\n')
		brutoNova()

if(__name__ == '__main__'):
	brutoNova()
