import sqlite3 as sql

conn = sql.connect(':memory:')

conn.execute("""
    CREATE TABLE usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE
    )
""")

conn.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("Ana", "ana@gmail.com"))
conn.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("João", "joao@gmail.com"))
conn.commit()

cursor = conn.execute("SELECT * FROM usuarios")

for linha in cursor:
    print(linha)

conn.close()