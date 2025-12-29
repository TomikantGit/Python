email_antigo = "TAFODANECURSOR@GMAIL.COM"

email_antigo = email_antigo.lower()

# para utilizar funções do próprio python, é necessário colocar após o = da variavel, a função correspondente

# - len : conta a quantidade de caracteres de um texto

# exemplo: email = len(email)

# - find : procura o index de uma letra em um texto

# exemplo: email = email.find("@")

emailbusca = email_antigo.find("t")

caracteres_email = len(email_antigo)

print(caracteres_email)

print(email_antigo[emailbusca:])

# replace - poder trocar uma parte do texto escrito

emailtrocado = email_antigo.replace("gmail.com","yahoo.com")

print(emailtrocado)