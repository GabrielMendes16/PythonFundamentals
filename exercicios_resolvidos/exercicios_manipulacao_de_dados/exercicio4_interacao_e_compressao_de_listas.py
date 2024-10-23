# Iteração e Compreensão de Listas:
# Crie uma lista de números e utilize um loop para multiplicar cada número por 2. Depois, refaça o mesmo usando compreensão de lista.

numeros = [2, 4, 6, 8, 10]

print("Pecorrendo a lista com loop e realizando mutplicação: ")

for multiplicar in numeros:
    resultado = multiplicar * 2
    print(resultado, end = " ")
print()

   

usando_compreensao = [x * 2 for  x in numeros]
print(f"Usando compreensão de lista: {usando_compreensao}")