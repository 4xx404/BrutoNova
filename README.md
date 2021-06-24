# BrutoNova  

Hash Cracker, Brute Forcer tools & MD5 Database.  
  
BrutoNova is a multi-tool designed for password cracking & brute force. Since MD5 encryption is irreversible, the MD5 Database enables you to store plain text strings & their equivalent hashed string for fast offline search.  
  
# Usage  
```
git clone https://github.com/4xx404/BrutoNova && cd BrutoNova
sudo chmod +x setup.py server.py && ./setup.py
python3 brutoNova.py
```
  
# Hashing/Cracking  
* Use online & local wordlists  
* Crack SHA1, SHA224, SHA256, SHA384, SHA512, SHA3-224, SHA3-256, SHA3-384 & SHA3-512 hashes  
* Fast offline search
* Quickly hash full wordlists into the data  
  
# Brute Force
* Web Directory Brute Force(with or without an extension)  
* FTP Server Brute Force
* SSH Brute Force(Coming soon)
* Web Login Brute Force(Coming soon)
* Positive Brute Force credentials are automatically added to database
  
# Web UI
* Use the search bar to find a specific database record
* Toggle between search & full database
  
The Web UI is not fully finished but is complete enough to be usable with BrutoNova as it currently is. The Web Interface files, including database file, will be moved to /var/www/html/ during setup & can be opened in the browser simply by running the server using...
```
./server.py
```
  
I intend to add more hash types & the above mentioned brute force tools in future updates.  
