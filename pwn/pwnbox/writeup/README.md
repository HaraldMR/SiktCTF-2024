# Writeup
nmap shows us that this machine has two open ports: one http port and an ssh port.

The website has an upload page. Uploading any file displays where the file is stored. under /uploads we can check if there are any more files here. and there are. misspelling a file under /uploads/ lets us see all the files that are in the directory. We can see that there is a file "welcome.txt" on the server. Someone has left the username and password of an user in plaintext. We can use this to ssh into the machine.

Looking at the homefolder we see a gitrepo with the same file as before. It has the same contents. 
The git logs reveal that there has been a change to this file however, and we can `git checkout` the earlier commit and `git show` this file which will give us the username and password of the "admin" user. Logging into this user lets us retrieve the flag.