# Writeup

The `disk.zip` file can be unpacked to obtain `disk.raw`.

Using `mmls`, you’ll see one partition on the disk, which is NTFS starting at offset 2048. However, the partition is oddly named "ext3."

Use the `sigfind` tool to search for other filesystem signatures that indicate the start of an EXT3 filesystem. You will find multiple matches, but most are false positives. The correct partition is found with a match at offset 79874. EXT3 begins with 1024 empty bytes, so when examining the filesystem, adjust by subtracting two sectors from this offset to locate the actual start.

The correct offset for the old partition is therefore 79872:

```bash
fls -o 79872 disk.raw
```

Export four files using:

```bash
tsk_recover -o 79872 disk.raw output
```

Concatenate the files:

```bash
cat output/* > newfile
```

This will yield a `.tar` file within an `.xz` file. Extract it with:

```bash
tar Jxvf newfile
```

Open the extracted GPX file in a GPS viewer (e.g., Google Earth).

The solution word is written as a track within the GPX file.
