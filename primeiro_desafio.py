
indice_arroba = email.find("@")

dominio_email = email[indice_arroba:]

print(dominio_email)

indice_primeironome = nome.find(" ")

primeiro_nome = nome[0:indice_primeironome+1]

print(primeiro_nome)

texto_final = f"O usuário {primeiro_nome}foi cadastrado com o dominio de email: {dominio_email}"

print(texto_final)