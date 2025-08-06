from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


# Initialize SQLite database
def init_db():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                amount REAL
            )
            '''
        )
        conn.commit()
init_db()

# Initialize a counter
form_count = 0

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/weeklyblogs')
def info():
    return render_template('weeklyblogs.html')

@app.route('/aboutus')
def chatbot():
    return render_template('aboutus.html')

@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, email, amount FROM users')
    users = cursor.fetchall()
    conn.close()
    user_list = [{'name': user[0], 'email': user[1], 'amount': user[2]} for user in users]
    return jsonify(user_list)

if __name__ == '__main__':
    app.run(debug=True)
