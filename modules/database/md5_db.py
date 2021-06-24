#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen, hashlib
from modules.stylesheet.Styling import bc, sd
banner, sBan, eBan, iBan, md5Options = sd.banner.logo, sd.sBan, sd.eBan, sd.iBan, sd.md5Options
import sys, os, time
import sqlite3

class hash_db_MD5:
	def __init__(self):
		self.conn = sqlite3.connect('/var/www/html/BrutoNova-UI/db/brutoNova.db')
		self.db = self.conn.cursor()
		self.db.execute('''CREATE TABLE IF NOT EXISTS MD5_HASHES(
				PLAIN_TEXT	TEXT 		NOT NULL	UNIQUE,
				HASH		TEXT);
			''')
		self.conn.commit()
		self.db.execute('''CREATE TABLE IF NOT EXISTS FTP_CREDS(
				HOST		TEXT 		NOT NULL	UNIQUE,
				USER		TEXT		NOT NULL,
				PASSWORD	TEXT);
			''')
		self.conn.commit()
		self.db.execute('''CREATE TABLE IF NOT EXISTS SSH_CREDS(
				HOST		TEXT 		NOT NULL	UNIQUE,
				USER		TEXT		NOT NULL,
				KEY		TEXT);
			''')
		self.conn.commit()
		self.db.execute('''CREATE TABLE IF NOT EXISTS WEB_LOGIN_CREDS(
				HOST		TEXT 		NOT NULL	UNIQUE,
				USER		TEXT		NOT NULL,
				PASSWORD	TEXT);
			''')
		self.conn.commit()			

	def single_word(self, word):
		self.plainText = word
		self.md5Result = hashlib.md5(self.plainText.encode('utf-8'))
		self.md5 = self.md5Result.hexdigest()

		try:
			self.db.execute('INSERT OR IGNORE INTO MD5_HASHES(PLAIN_TEXT, HASH) VALUES (?,?) ', (self.plainText, self.md5))
			self.conn.commit()
		except Exception:
			print('\n' + eBan + bc.RC + ' ERROR: ' + bc.BC + 'Hash Failed')
			input(bc.BC + ' Press Enter to Continue...\n')
			from brutoNova import brutoNova
			brutoNova()

		print('\n' + sBan + bc.GC + ' Hash Successfully Added')
		print(bc.BC + ' Plain-Text: ' + bc.GC + self.plainText)
		print(bc.BC + ' Hash: ' + bc.GC + self.md5Result.hexdigest())
		input(bc.BC + '\n Press Enter to Continue...\n')
		os.system('clear')
		print(banner)
		from brutoNova import brutoNova
		brutoNova()
		
	def wordlist(self, wordlist, *words):
		self.wordlist = wordlist
		self.words = list(words)
		self.countTotal = str(len(self.words))

		count = 0
		for word in self.words:
			if(word != ''):
				os.system('clear')
				print(banner)
				md5 = hashlib.md5(word.encode('utf-8'))
				status = bc.BC + ' Hashing: ' + bc.GC + str(word.replace('\n', ''))
				md5Result = md5.hexdigest()
				try:
					count += 1
					print(bc.BC + ' Progress: ' + bc.GC + str(count) + bc.BC + '/' + bc.GC + self.countTotal)
					print(bc.BC + ' Updating Database with wordlist: ' + bc.GC + wordlist)
					print(status + bc.BC + '\t' + bc.RC + md5Result)
					self.db.execute('INSERT OR IGNORE INTO MD5_HASHES(PLAIN_TEXT, HASH) VALUES (?,?) ', (word, md5Result))
					self.conn.commit()
				except sqlite3.IntegrityError:
					continue
			else:
				continue

		os.system('clear')
		print(banner)
		print(sBan + ' Updated Database with wordlist: ' + bc.GC + wordlist)
		print(bc.BC + ' ' + str(count) + ' Hashes successfully added to database')
		input(bc.BC + '\n Press Enter to Continue...\n')
		from brutoNova import brutoNova
		brutoNova()
		
	def search_hash(self, plainText, hashSearch):
		self.plain_text = plainText
		self.hash_query = hashSearch
		
		if(self.plain_text != '' and self.hash_query == ''):
			self.db.execute("SELECT * FROM MD5_HASHES WHERE PLAIN_TEXT='" + self.plain_text + "';")
			res = self.db.fetchall()
			for row in res:
				print('\n' + sBan + ' Matching Hash has been found\n')
				print(bc.BC + ' Plain-Text: ' + bc.GC + row[0])
				print(bc.BC + ' Hash: ' + bc.GC + row[1] + '\n')
		if(self.hash_query != '' and self.plain_text == ''):
			self.db.execute("SELECT * FROM MD5_HASHES WHERE HASH='" + self.hash_query + "';")
			res = self.db.fetchall()
			for row in res:
				print('\n' + sBan + ' Matching Hash has been found\n')
				print(bc.BC + ' Plain-Text: ' + bc.GC + row[0])
				print(bc.BC + ' Hash: ' + bc.GC + row[1] + '\n')

		input(bc.BC + ' Press Enter to Continue...')
		os.system('clear')
		print(banner)
		from brutoNova import brutoNova
		brutoNova()

	def addFTPCreds(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		try:
			self.db.execute('INSERT INTO FTP_CREDS(HOST, USER, PASSWORD) VALUES (?,?,?)', (self.host, self.user, self.password))
			self.conn.commit()
		except sqlite3.IntegrityError:
			pass
