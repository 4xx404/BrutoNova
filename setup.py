#!/usr/bin/env python3

import os, sys, time
from modules.stylesheet.Styling import bc, sd
banner, sBan, eBan, iBan = sd.banner.logo, sd.sBan, sd.eBan, sd.iBan

os.system('clear')
print(banner)

def runSetup():
	print(bc.BC + ' Running BrutoNova setup...\n Installing Dependencies...\n')
	try:
		os.system('python3 -m pip install -r requirements.txt')
	except Exception:
		print(eBan + bc.RC + ' Failed to install dependencies\n')
		quit()

	os.system('clear')
	print(banner)
	print(sBan + ' Dependencies Installed')
	try:
		os.system('mv BrutoNova-UI /var/www/html/')
	except Exception:
		print(eBan + ' Failed to move ' + bc.RC + 'BrutoNova-UI/' + bc.BC + ' to ' + bc.RC + '/var/www/html/')
		print(eBan + ' Setup failed')
		quit()

	print(sBan + ' Moved ' + bc.GC + 'BrutoNova-UI/' + bc.BC + ' to ' + bc.GC + '/var/www/html/')
	print(sBan + ' Setup successful')
	quit()

if __name__ == '__main__':
	runSetup()
