import random

numero_sorteado = random.randint(1, 100)
numero_informado = None

while numero_informado != numero_sorteado:

    entrada = input("Informe um número para tentar acertar o número sorteado: ")

    try:
        numero_informado = int(entrada) 
        
        if abs(numero_sorteado - numero_informado) <= 10:
            print("Palpite próximo")
        elif numero_sorteado > numero_informado:
            print("Palpite muito baixo")
        else:
            print("Palpite muito alto")
            
    except ValueError:
        print("Entrada inválida, por favor insira um número.")

print("Palpite Correto, Você Acertou!")
