#!/usr/bin/env python3

import os, sys, time
import subprocess
from pyngrok import ngrok
from modules.stylesheet.Styling import bc, sd
banner, sBan, eBan, iBan = sd.banner.logo, sd.sBan, sd.eBan, sd.iBan

os.system('clear')
print(banner)

def runServer():
	print(bc.BC + " Starting Ngrok HTTP Tunnel...")
	try:
		http_tunnel = ngrok.connect()
		time.sleep(1)
		if http_tunnel:
			serverStatus = sBan + ' Ngrok Tunnel: ' + bc.GC + 'Connected'
		else:
			serverStatus = eBan + ' Ngrok Tunnel: ' + bc.RC + 'Disconnected'
		
		os.system('clear')
		print(banner)
		print(serverStatus)
		brutoNovaURL = str(http_tunnel).replace('"', '').replace('NgrokTunnel: ', '').replace(' -> http://localhost:80', '').replace('http', 'https') + "/BrutoNova-UI/"
		time.sleep(0.5)
		print(bc.BC + ' Interface URL: ' + bc.GC + brutoNovaURL)
		ngrok_process = ngrok.get_ngrok_process()
		print(bc.BC + "\n" + iBan + bc.GC + " CTRL + C" + bc.BC + " to stop the server\n")
		os.chdir('/var/www/html/')
		subprocess.call(['php', '-S', 'localhost:80'])
		ngrok_process.proc.wait()
	except KeyboardInterrupt:
		os.system('clear')
		print(banner)
		print(bc.BC + " Closing PHP Web Server...")
		time.sleep(0.5)
		print(bc.BC + " Closing Ngrok HTTP Tunnel...")
		ngrok.disconnect(http_tunnel.public_url)
		time.sleep(0.5)
		print(bc.BC + " Killing Ngrok process...")
		time.sleep(0.5)
		ngrok.kill()
		time.sleep(0.5)
		os.system('clear')
		print(banner)
		quit()

if __name__ == '__main__':
	runServer()
