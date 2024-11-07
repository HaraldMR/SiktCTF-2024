# Zucchini
I dont know about you, but i find zucchinis to be terribly plain. And who decided to name them that, anyways?

## Flag
SiktCTF{Summer_Squash_B3Krn5I22dRC215FijweC}

## Writeup
<details>
<summary> View writeup</summary>

The file is a squashfs file system. Unsquashfs the file and look through its contents, you will find a few hints throughout it, until you look in the apache2 folders under www. here is a html file that includes some sort of javascript that displays a flag after heavily decrypting some string. Open the html file in a browser or run the js to get the flag.

</details>