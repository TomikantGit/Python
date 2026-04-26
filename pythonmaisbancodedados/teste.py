import mysql.connector

meubanco = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password =  "@Cabo1234_tomikant"
)

print(meubanco)

cursor = meubanco.cursor()

cursor.execute("USE meubancototal")
cursor.execute("CREATE TABLE Funcionarios (nome VARCHAR(50), idade VARCHAR(2), email VARCHAR(50))")