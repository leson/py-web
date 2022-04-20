import sqlite3,sys
print(sys.path)
conn=sqlite3.connect("./db/books.db")

cur=conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS books
    (id int primary key,
    sort int,
    name text,
    price real
    )
""")

cur.execute("""
INSERT INTO books VALUES(1,1,"Computer Science",39.9)
""")

books=[
    (2,2,"Deep Learning",98),
    (3,2,"Reenforcement Learning",108),
    (4,3,"Artificial Intelligence",128)
]

cur.executemany("INSERT INTO books VALUES(?,?,?,?)",books)

conn.commit()
conn.close()
print("init db completed")