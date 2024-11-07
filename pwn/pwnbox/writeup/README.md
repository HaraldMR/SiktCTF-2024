# pwnbox
Pwn the server to get the flag

## Flag
CTF{Do_You_Know_How_To_Pwn?}

## Writeup
nmap shows us that this machine has two open ports: a http port and a ssh port.

The website has an upload page. Uploading any file displays where the file is stored. under /uploads we can check if there are any more files here. and there are. using /uploads/* we can see that there is a file "welcome.txt" on the server. Someone has left the username and password of a develpoper user in plaintext. We can use this to ssh into the machine.

Looking at the homefolder we see a gitrepo with the same file as before. it contains the same text as before. The git logs reveal that there has been a change to this file however, and we can git show this file in one of the earlier commits, which will give us the username and password of a "admin" user. logging into this user gives us the flag.

## Credit
The inspiration came from the HTB machine "Editorial", the git part is similar.