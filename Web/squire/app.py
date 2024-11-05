from flask import Flask, request, render_template_string, g, redirect, url_for, flash, render_template, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Using a parameterized query for username
    query_secure = "SELECT * FROM users WHERE username = ?"
    user_secure = query_db(query_secure, (username,), one=True)
    
    if user_secure:
        # Vulnerable part: password check with string concatenation
        query_insecure = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        user_insecure = query_db(query_insecure, one=True)
        
        if user_insecure:
            session['logged_in'] = True
            return redirect(url_for('success'))
    
    flash('Login failed!', 'error')
    return redirect(url_for('index'))

@app.route('/success')
def success():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template("success.html")

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
        db.execute("INSERT INTO users (username, password) VALUES ('admin', 'ilikestrongpasswordsthatareverylongandcomplicatedhahahahaehehehah')")
        db.commit()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=80)
