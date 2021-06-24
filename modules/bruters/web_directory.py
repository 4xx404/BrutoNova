#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, time
import requests
from urllib.request import urlopen
from modules.stylesheet.Styling import bc, sd
banner, sBan, eBan, iBan, md5Options = sd.banner.logo, sd.sBan, sd.eBan, sd.iBan, sd.md5Options

class webBrute:
	def __init__(self, host, wordlistOpt):
		self.host = host
		self.option = wordlistOpt

	def bruteForce(self):
		if(self.option == 1):
			wordlist = str(input(bc.BC + ' Online Wordlist: ' + bc.GC))
			if(wordlist != '' or wordlist != ' '):
				try:
					words = str(urlopen(wordlist).read(), 'utf-8')
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
					words = open(wordlist).read()
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

		print('\n' + iBan + ' Leave Extension empty for directories only')
		ext = str(input(bc.BC + ' Extension: ' + bc.GC))
		if(ext == ''):
			ext = ''
		else:
			if(ext[0] == '.'):
				ext = ext
			else:
				ext = '.' + ext

		os.system('clear')
		print(banner)
		print(bc.BC + ' Host: ' + bc.GC + self.host)
		print(bc.BC + ' Wordlist: ' + bc.GC + wordlist + '\n')

		hits = []
		for word in words.split('\n'):
			if(word != ''):
				if(self.host.endswith('/')):
					url = self.host + word + ext
				else:
					url = self.host + "/" + word + ext

				try:
					req = requests.get(url)
				except Exception:
					os.system('clear')
					print(banner)
					print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Failed to connect to ' + bc.RC + url)
					from brutoNova import brutoNova
					brutoNova()
				
				if(req.status_code == 200 or req.status_code == 301 or req.status_code == 302 or req.status_code == 410 or req.status_code == 500 or req.status_code == 503):
					print(sBan + bc.GC + ' ' + str(req.status_code) + bc.BC + ' :: ' + bc.GC + url)
					entry = str(req.status_code) + ':#:' + url
					hits.append(entry)
				else:
					print(eBan + bc.RC + ' ' + url)
			else:
				continue
			
		os.system('clear')
		print(banner)
		print(bc.BC + ' Host: ' + bc.GC + self.host)
		print(bc.BC + ' Wordlist: ' + bc.GC + wordlist + '\n')
		print(sBan + ' Results: ')
		for hit in hits:
			code = hit.split(':#:')[0]
			url = hit.split(':#:')[1]
			print('\t' + bc.BC + code + ' ' + bc.GC + hit)

		input(bc.BC + '\n Press Enter to Continue...\n')
		from brutoNova import brutoNova
		brutoNova()
