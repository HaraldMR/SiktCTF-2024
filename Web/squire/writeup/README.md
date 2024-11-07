# Writeup

The login page is vulnerable to SQL injection, those rats of yours made a good job of finding the hole in their defences!
the vulnerable field is the password field. working injections:
anything' OR '1'='1'
anything' OR 1=1 --

You can deduce from the description that the username should be admin.

Successful injections sends you to the next page which shows a gif that has the flag.