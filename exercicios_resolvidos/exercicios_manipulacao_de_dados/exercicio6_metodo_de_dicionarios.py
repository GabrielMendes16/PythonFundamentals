# Métodos de Dicionários:
# Crie um dicionário com informações de um usuário, adicione uma nova chave com o valor de salario, 
# modifique o valor da chave "cargo" e remova a chave "idade" usando o método pop().


funcionario = {
    "nome": "Afonso Martins",
    "idade": 35,
    "cargo": "Analista de Dados"
}
print("Criação do dicionario")
print(funcionario)
print("-" * 82)

print("Adicionado uma nova chave e valor: ")
print("-" * 82)
funcionario.update({"salario": 2800})
print(funcionario)
print("-" * 82)


print("Modificando valor da chave cargo: ")
print("-" * 82)
funcionario.update({"cargo": "Analista Cloud"})
print(funcionario)
print("-" * 82)

print("Removendo chave e valor: ")
print("-" * 82)
chave_removida = funcionario.pop("idade")
print(f"O valor {chave_removida} e sua chave idade foi removida")
print("-" * 82)
print(funcionario)