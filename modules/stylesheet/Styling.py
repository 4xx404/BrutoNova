class bc:
	GC = '\033[1;39m'
	BC = '\033[1;34m'
	RC = '\033[1;31m'

class sd:
	iBan = bc.BC + " [" + bc.GC + "?" + bc.BC + "]" # Info banner
	sBan = bc.BC + " [" + bc.GC + u'\u2713' + bc.BC + "]" # Success banner
	eBan = bc.BC + " [" + bc.RC + u'\u2717' + bc.BC + "]" # Error banner
	
	menuOptions = {
		1:"Crack Sha1 Hash",
		2:"Crack Sha224 Hash",
		3:"Crack Sha256 Hash",
		4:"Crack Sha384 Hash",
		5:"Crack Sha512 Hash",
		6:"Crack Sha3-224 Hash",
		7:"Crack Sha3-256 Hash",
		8:"Crack Sha3-384 Hash",
		9:"Crack Sha3-512 Hash",
		10:"Add MD5 hash/es to Database",
		11:"Brute Force Web Directories",
		12:"Brute Force FTP Server",
		0:"Quit",
	}
	
	md5Options = {
		" 1":"Add Single MD5 Hash to Database",
		" 2":"Add Wordlist to MD5 Database",
		" 3":"Search MD5 Database",
	}

	class banner:
		author = bc.BC + "\n\tAuthor: " + bc.RC + "4" + bc.GC + "x" + bc.BC + "x" + bc.RC + "4" + bc.GC + "0" + bc.BC + "4\n"
		version = bc.BC + "\tVersion: " + bc.RC + "2" + bc.GC + "." + bc.BC + "0\n"
		github = bc.BC + "\tGithub: " + bc.RC + "h" + bc.GC + "t" + bc.BC + "t" + bc.RC + "p" + bc.GC + "s" + bc.BC + ":" + bc.RC + "/" + bc.GC + "/" + bc.BC + "g" + bc.RC + "i" + bc.GC + "t" + bc.BC + "h" + bc.RC + "u" + bc.GC + "b" + bc.BC + "." + bc.RC + "c" + bc.GC + "o" + bc.BC + "m" + bc.RC + "/" + bc.GC + "4" + bc.BC + "x" + bc.RC + "x" + bc.GC + "4" + bc.BC + "0" + bc.RC + "4\n"
		logo = bc.RC + '''
		    ___           __       _  __              
		''' + bc.BC + '''   / _ )______ __/ /____  / |/ /__ _  _____ _ 
		''' + bc.RC + '''  / _  / __/ // / __/ _ \/    / _ \ |/ / _ `/ 
		''' + bc.GC + ''' /____/_/  \_,_/\__/\___/_/|_/\___/___/\_,_/  
		''' + author + version + github
