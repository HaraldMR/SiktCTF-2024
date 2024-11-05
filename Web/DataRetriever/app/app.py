from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    if request.headers.get('DNT') == '1':
        return render_template('dnt.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
