import sqlite3

with sqlite3.connect('saper.db') as con:
  cur = con.cursor()
# cur.execute('''DROP TABLE student''')
cur.execute('''CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    hobby TEXT,
    birth_date INTEGER,
    score INTEGER
     )''')
cur.execute('''SELECT * FROM student WHERE LENGTH(surname) >10''')
cur.execute('''UPDATE student SET name = 'genius' WHERE score>10''')
cur.execute('''SELECT * FROM student WHERE name = 'genius' ''')
# cur.execute('''DELETE FROM student WHERE id % 2 = 0''')
item = cur.fetchall()
for i in item:
    print(i)