import os
from modules.stylesheet.Styling import bc, sd
sBan = sd.sBan

def cleanup():
	try:
		os.system('rm -rf __pycache__/')
		os.system('rm -rf modules/bruters/__pycache__/')
		os.system('rm -rf modules/crackers/__pycache__/')
		os.system('rm -rf modules/database/__pycache__/')
		os.system('rm -rf modules/stylesheet/__pycache__/')
	except Exception:
		pass

	print(sBan + ' Complete')

if(__name__ == '__main__'):
	cleanup()
