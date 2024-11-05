# urgent

Someone is trying to hack my server, the username and password for it is ctfuser. They stole my important text file, please get it back for me.


## Flag
SiktCTF{WHo_is_TH3_Re4L_HaCk3R?}

## Writeup
<details>
<summary> View Writeup </summary>
There are logs on the server, which reveals there is an ftp server on the same server that someone has tried to connect from. running nmap on the server also reveals that there is an open vsftpd server on port 2121. Log into this and the flag is there.
</details>