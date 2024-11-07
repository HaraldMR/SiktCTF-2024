# Writeup

Description: 
*Someone is trying to hack my server, the username and password for it is ctfuser. They stole my important text file, please get it back for me.*

There are logs in the users home driectory under **.logs**, which reveals that someone has been logging in to another service on port 2121.
Scanning it we can se that it is an ftp server. Log into this using an ftp client. 
Fortunately there is no password for the ftp server so we can retrieve the flag for free.