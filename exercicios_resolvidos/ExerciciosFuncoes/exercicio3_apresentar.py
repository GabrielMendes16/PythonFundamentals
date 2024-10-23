# Exercício 3: Função com Parâmetros Opcionais
# Desenvolva uma função chamada apresentar que recebe dois parâmetros: nome e saudacao com valor padrão "Olá". 
# A função deve retornar uma string combinando a saudação e o nome. Teste a função de duas maneiras:

# Apenas com o nome "Ana".
# Com o nome "Carlos" e a saudação "Boa tarde"

def apresentar(nome,saudacao="Olá"):
    print(f"{saudacao}, {nome}")

print(apresentar("Ana"))
print(apresentar("Carlos", "Boa Tarde"))