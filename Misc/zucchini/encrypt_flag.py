from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os

# Read the flag from the flag file
with open('flag.txt', 'r') as file:
    flag = file.read().strip()

# Generate a random key
key = os.urandom(16)

# Create a cipher object and encrypt the flag
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(flag.encode(), AES.block_size))

# Encode the ciphertext and the key
encrypted_flag = base64.b64encode(cipher.iv + ct_bytes).decode('utf-8')
encoded_key = base64.b64encode(key).decode('utf-8')

# Generate the parts for the HTML file
html_script = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Secret</title>
</head>
<body>
    <h1 id="flag"></h1>
    <script>
        function decodeBase64(str) {{
            return atob(str);
        }}

        function decryptFlag(encrypted, key) {{
            var decipher = crypto.subtle.importKey("raw", new Uint8Array(decodeBase64(key).split('').map(c => c.charCodeAt(0))), "AES-CBC", false, ["decrypt"]).then(key => {{
                var iv = new Uint8Array(decodeBase64(encrypted).split('').slice(0, 16).map(c => c.charCodeAt(0)));
                var data = new Uint8Array(decodeBase64(encrypted).split('').slice(16).map(c => c.charCodeAt(0)));
                return crypto.subtle.decrypt({{ name: "AES-CBC", iv: iv }}, key, data);
            }}).then(decrypted => {{
                var decoder = new TextDecoder();
                return decoder.decode(new Uint8Array(decrypted));
            }}).catch(err => console.error(err));
            return decipher;
        }}

        var encryptedFlag = "{encrypted_flag}";
        var key = "{encoded_key}";

        decryptFlag(encryptedFlag, key).then(flag => {{
            document.getElementById("flag").innerHTML = flag;
        }});
    </script>
</body>
</html>
"""

# Save the HTML script to a file
with open('index.html', 'w') as file:
    file.write(html_script)

print("Encryption complete. 'index.html' generated.")
