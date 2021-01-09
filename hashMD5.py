#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen, hashlib
import sys, os, time
import sqlite3

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

def hashDB():
	os.system('clear')
	print(banner)
	print(bcolors.BLUE + " 1. " + bcolors.GREEN + "Add Single MD5 Hash to Database")
	print(bcolors.BLUE + " 2. " + bcolors.GREEN + "Add Wordlist to MD5 Database")
	print(bcolors.BLUE + " 3. " + bcolors.GREEN + "Search MD5 Database\n")
	print(bcolors.BLUE + " [" + bcolors.GREEN + "?" + bcolors.BLUE + "] Enter " + bcolors.GREEN + "#//" + bcolors.BLUE + " to return to menu " + bcolors.BLUE + "[" + bcolors.GREEN + "?" + bcolors.BLUE + "]")

	md5option = str(input(bcolors.BLUE + " Option: " + bcolors.GREEN))
		
	conn = sqlite3.connect("db/bruto.db")
	cursor = conn.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS hashes (
		id		integer 			PRIMARY KEY	AUTOINCREMENT,
		plain_text	text 		NOT NULL	UNIQUE,
		hash		text
		);''')
	conn.commit()
		
	if md5option == "1":
		plainText = input(bcolors.BLUE + " Enter Word as Plain-Text: " + bcolors.GREEN)
		if plainText == "":
			print(bcolors.BLUE + " HASH ERROR: " + bcolors.RED + " Hash value cannot be empty")
			input(bcolors.BLUE + " Press Enter to Continue...")
			hashDB()
			
		else:
			md = hashlib.md5(plainText.encode('utf-8'))
			x = md.hexdigest()

			try:
				cursor.execute("INSERT INTO hashes (plain_text, hash) VALUES (?,?) ", (plainText, x))
				conn.commit()
				print(bcolors.BLUE + "\n ["+ bcolors.GREEN +"+" +bcolors.BLUE + "] Hash Successfully Added [" + bcolors.GREEN + "+" + bcolors.BLUE + "]")
				print(bcolors.BLUE + " Plain-Text: " + bcolors.GREEN + plainText)
				print(bcolors.BLUE + " Hash: " + bcolors.GREEN + x)

			except Exception:
				print(bcolors.BLUE + " HASH ERROR: " + bcolors.RED + "Hash Failed")
				input(bcolors.BLUE + " Press Enter to Continue...")
				hashDB()
		
			input(bcolors.BLUE + " Press Enter to Continue...")
			hashDB()
				
	elif md5option == "2":
		wordlist = input(bcolors.BLUE + " Local Wordlist: " + bcolors.GREEN)
		if wordlist == "":
			print(bcolors.BLUE + " WORDLIST ERROR: " + bcolors.RED + " Wordlist value cannot be empty")
			input(bcolors.BLUE + " Press Enter to Continue...")
			hashDB()
		else:
			try:
				words = open(wordlist, "r+")
			except Exception:
				print(bcolors.BLUE + " FILE ERROR: " + bcolors.RED + "Failed to open " + wordlist)
				input(bcolors.BLUE + " Press Enter to Continue...")
				hashDB()

			count = 0

			for word in words:
				os.system('clear')
				print(banner)
				md = hashlib.md5(word.encode('utf-8'))
				status = bcolors.BLUE + " Hashing: " + bcolors.GREEN + str(word.replace("\n", ""))
				x = md.hexdigest()

				print(bcolors.BLUE + " Updating Database with wordlist: " + bcolors.GREEN + wordlist)
				print(status + bcolors.BLUE + "	" + bcolors.RED + x)

				cursor.execute("INSERT INTO hashes (plain_text, hash) VALUES (?,?) ", (word, x))
				conn.commit()
				count += 1
			
			os.system('clear')
			print(banner)
			print(bcolors.BLUE + " Updated Database with wordlist: " + bcolors.GREEN + wordlist)
			print(bcolors.BLUE + " ["+ bcolors.GREEN + "+" +bcolors.BLUE + "] " + str(count) + " Hashes Successfully Added to Database [" + bcolors.GREEN + "+" + bcolors.BLUE + "]\n")
			input(bcolors.BLUE + " Press Enter to Continue...")
			hashDB()
		
	elif md5option == "3":
		hashToSearch = str(input(bcolors.BLUE + " Hash to Search: " + bcolors.GREEN))
		if hashToSearch == "":
			print(bcolors.BLUE + " HASH ERROR: " + bcolors.RED + " Hash value cannot be empty")
			input(bcolors.BLUE + " Press Enter to Continue...")
			hashDB()
		else:
			cursor.execute("SELECT * FROM hashes WHERE hash='"+hashToSearch+"';")
			res = cursor.fetchall()
		
			for row in res:
				print(bcolors.BLUE + "\n [" + bcolors.GREEN + "*" + bcolors.BLUE + "] Matching hash has been found [" + bcolors.GREEN + "*" + bcolors.BLUE + "]")
				print(bcolors.BLUE + " Database ID: " + bcolors.GREEN + str(row[0]))
				print(bcolors.BLUE + " Plain-Text: " + bcolors.GREEN + row[1])
				print(bcolors.BLUE + " Hash: " + bcolors.GREEN + row[2] + "\n")
		
			input(bcolors.BLUE + " Press Enter to Continue...")
			hashDB()

	elif md5option == "#//":
		from brutonova import nova
		nova()

	else:
		print(bcolors.BLUE + " OPTION ERROR: " + bcolors.RED + " Invalid Option")
		input(bcolors.BLUE + " Press Enter to Continue...")
		hashDB()
