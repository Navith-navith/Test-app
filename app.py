from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    subject1 INTEGER NOT NULL,
                    subject2 INTEGER NOT NULL,
                    subject3 INTEGER NOT NULL,
                    subject4 INTEGER NOT NULL,
                    subject5 INTEGER NOT NULL
                    )''')
conn.commit()
conn.close()

# Home page - display all students
@app.route('/')
def home():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('student.html', students=students)

# Add new student
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    subject1 = request.form['subject1']
    subject2 = request.form['subject2']
    subject3 = request.form['subject3']
    subject4 = request.form['subject4']
    subject5 = request.form['subject5']
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, subject1, subject2, subject3, subject4, subject5) VALUES (?, ?, ?, ?, ?, ?, ?)", (name, age, subject1, subject2, subject3, subject4, subject5))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

# Delete student
@app.route('/delete/<int:id>')
def delete_student(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))    


