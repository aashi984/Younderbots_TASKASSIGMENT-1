from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="task1"
    )

@app.route('/')
def home():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM A1")
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('index.html', data=rows)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO A1 (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        db.commit()
    except:
        db.rollback()
    finally:
        cursor.close()
        db.close()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM A1 WHERE id = %s", (id,))
        db.commit()
    except:
        db.rollback()
    finally:
        cursor.close()
        db.close()

    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def edit(id):
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    db = get_connection()
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE A1 SET name=%s, email=%s, phone=%s WHERE id=%s", (name, email, phone, id))
        db.commit()
    except:
        db.rollback()
    finally:
        cursor.close()
        db.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)