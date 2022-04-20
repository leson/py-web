import sqlite3
from flask import Flask
from flask import request,jsonify,render_template

print(__name__)

app = Flask(__name__)

@app.route('/api/books', methods=['GET', 'POST'])
def getBooks():
    conn=sqlite3.connect("./db/books.db")
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    sql="select * from books"
    rows=cur.execute(sql).fetchall()
    rows=[dict(row) for row in rows]
    return jsonify(rows)

@app.route("/",methods=["GET"])
def books():
    return render_template("books.html",title="books list")
