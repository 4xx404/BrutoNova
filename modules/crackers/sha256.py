#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time
from urllib.request import urlopen, hashlib
from modules.stylesheet.Styling import bc, sd
banner, sBan, eBan, iBan = sd.banner.logo, sd.sBan, sd.eBan, sd.iBan

class sha256_hash:
	def __init__(self, sha256_hash):
		self.sha256 = sha256_hash

	def crack(self, option):
		self.wopt = option
		if(self.wopt == 1):
			wordlist = str(input(bc.BC + ' Online Wordlist: ' + bc.GC))
			if(wordlist != '' or wordlist != ' '):
				try:
					passwords = str(urlopen(wordlist).read(), 'utf-8')
				except Exception:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Failed to open ' + bc.RC + wordlist)
					from brutoNova import brutoNova
					brutoNova()
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Wordlist value cannot be empty\n')
				from brutoNova import brutoNova
				brutoNova()
		else:
			wordlist = str(input(bc.BC + ' Local Wordlist: ' + bc.GC))
			if(wordlist != '' or wordlist != ' '):
				try:
					passwords = open(wordlist).read()
				except Exception:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Failed to open ' + bc.RC + wordlist)
					from brutoNova import brutoNova
					brutoNova()
			else:
				os.system('clear')
				print(banner)
				print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Wordlist value cannot be empty\n')
				from brutoNova import brutoNova
				brutoNova()
		
		os.system('clear')
		print(banner)
		print(bc.BC + ' SHA256: ' + bc.GC + self.sha256)
		print(bc.BC + ' Wordlist: ' + bc.GC + wordlist + '\n')
		match = ''
		for passwd in passwords.split('\n'):
			if(passwd != ''):
				pw = hashlib.sha256(bytes(passwd, 'utf-8')).hexdigest()
				if(self.sha256 == pw):
					print(sBan + ' Found a Match: ' + bc.GC + passwd)
					input(bc.BC + '\n Press Enter to Continue...')
					os.system('clear')
					print(banner)
					from brutoNova import brutoNova
					brutoNova()			
				elif(self.sha256 != pw):
					print(eBan + ' No Match: ' + bc.RC + passwd)
			else:
				continue
			
		input(bc.BC + '\n Press Enter to Continue...')
		os.system('clear')
		print(banner)
		from brutoNova import brutoNova
		brutoNova()
