# Shiva
There are three seperate flags on in this android app. find the first flag.

First flag is plain
Second flag is waiting for your signature
Third flag is not positive

## Flags
SiktCTF{UnlimitedPower}
SiktCTF{TheFinalDaysAreUponUs}
SiktCTF{InTheEndHopePrevails}

## Writeup
<details>
<summary> View writeup</summary>

Using jadx we can reverse the apk file, here we can find the first password in plain text. Use this password to unlock the first flag in the app. The second and third flags can be found by either instrumentation or repackaging of the app.
Use android studio to emulate the app.

</details>