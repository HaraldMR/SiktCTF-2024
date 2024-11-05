from flask import Flask, request, jsonify, render_template, send_file
import base64

app = Flask(__name__)

ENCRYPTED_FLAG = "YzkvGZW{LkpgtWkrk}"
FLAG = "SiktCTF{LilacWine}"

# Main page
@app.route('/')
def index():
    return render_template("index.html", flag=ENCRYPTED_FLAG)

# Hint endpoint (hidden in source code comments)
@app.route('/hidden/hint.txt')
def hint():
    hint_message = "The key is a name associated with virtue."
    encoded_hint = base64.b64encode(hint_message.encode()).decode()
    return jsonify({
        "hint": encoded_hint
    })

# Key part endpoints hidden in various ways
@app.route('/images/secret.png')
def image():
    return send_file("static/what.jpg", mimetype='image/jpg')

@app.route('/hidden/secret.txt')
def secret():
    return "The image is questionable, i wouldnt trust it!"

@app.route('/source.html')
def source():
    return "<!-- Look at the comments in the source code -->"

@app.route('/robots.txt')
def robots():
    return "User-agent: *\nDisallow: /hidden\n\n# Part 3 of the key is hidden in an unexpected place."

@app.route('/hidden/key.txt')
def hidden_key():
    return "Key part 3 is: A"

@app.route('/.well-known/security.txt')
def security_txt():
    return """
    Contact: mailto:admin@example.com
    Encryption: https://example.com/pgp-key.txt
    Acknowledgements: https://example.com/hall-of-fame
    Preferred-Languages: en
    Canonical: https://example.com/.well-known/security.txt

    <!-- Part 4 of the key is C -->
    """

# Validation endpoint
@app.route('/submit', methods=['POST'])
def validate():
    user_input = request.form.get('decrypted_flag')
    if user_input == FLAG:
        return jsonify({"message": "Congratulations! You've successfully decrypted the message."})
    return jsonify({"message": "Incorrect. Try again."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)