import secrets
import string

def gerador_de_senhas(tamanho=6):
    digitos = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(digitos) for _ in range(tamanho))
    return senha
    

senha_aleatorio = gerador_de_senhas()
print(senha_aleatorio)


