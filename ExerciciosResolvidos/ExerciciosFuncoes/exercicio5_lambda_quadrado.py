# Exercício 5: Função Lambda
# Utilizando uma função lambda, crie uma função que recebe um número e retorna seu quadrado. 
# Aplique essa função na lista [2, 4, 6, 8] utilizando map e exiba a lista resultante.

lista_de_numeros = [2,4,6,8]

numeros_ao_quadrado = list(map(lambda numero: numero ** 2, lista_de_numeros))

for resultado in numeros_ao_quadrado:
    print(resultado, end=" | ")


