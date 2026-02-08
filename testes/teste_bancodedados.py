import sqlite3

nome =  input("Digite o nome do usuário:")
email = input("Digite o email dele:")
numero = input("Digite o numero dele:")

conexao = sqlite3.connect("bancodedados_teste.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT,
               email Text,
               numero INTEGER
               )
               """)

cursor.execute(
    "INSERT INTO usuarios (nome, email, numero) VALUES (?, ?, ?)",
    (nome, email, numero)
)

conexao.commit( )

cursor.execute("SELECT * FROM usuarios")
print(cursor.fetchall())

conexao.close()