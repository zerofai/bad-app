from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create SQLite database and table if not exist
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')

# Insert some sample data
cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'password123')")
conn.commit()
conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Vulnerable code: SQL Injection can be performed by injecting malicious SQL statements in the input
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username='" + username + "' and password='" + password + "'")
        results = cursor.fetchall()
        if len(results) == 1:
            return "Login successful!"
        else:
            error = "Invalid username or password"
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)