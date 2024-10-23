# Manipulação de Strings:
# Crie uma string que contenha uma frase com pelo menos 5 palavras. 
# Use os métodos upper(), replace() e split() para manipular a string e exiba os resultados.

print("Criação da String: ")
frase = "Jesus é o caminho e a vida nele posso confiar!"
print(frase)
print("-" * 82)


frase.upper()

print("Mostrando Frase Usando o Método 'Upper()': ")
print(frase)
print("-" * 82)

print("Mostrando a Frase Usando o  Método 'replace(): '")
nova_frase = frase.replace("vida", "escolha certa")
print(nova_frase)
print("-" * 82)

print("Mostrando a Frase Usando o  Método 'split(): '")
elemento = frase.split()
frase = ("-".join(elemento))
print(frase)