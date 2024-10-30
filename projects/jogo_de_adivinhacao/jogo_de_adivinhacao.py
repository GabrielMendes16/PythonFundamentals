import random
# Lista de palavras e dicas
palavras = {
    "gato": "Um animal de estimação que gosta de caçar ratos.",
    "cachorro": "Um animal leal que é conhecido como o melhor amigo do homem.",
    "pássaro": "Um animal que pode voar e costuma fazer ninhos em árvores.",
    "peixe": "Um animal que vive na água e não pode viver fora dela.",
    "elefante": "Um grande mamífero conhecido por sua tromba e presas.",
    "sombra": "O que não tem luz, mas segue você o dia todo.",
    "eco": "O que repete o que você diz, mas não tem boca.",
    "ilha": "Um pedaço de terra cercado por água.",
    "relógio": "O que sempre avança, mas nunca se move.",
    "nuvem": "O que flutua no céu e pode chover.",
    "inception": "Um ladrão que entra nos sonhos das pessoas para roubar segredos.",
    "forrest gump": "A história de um homem com um coração puro que vive eventos históricos.",
    "star wars": "Uma épica saga espacial que envolve a luta entre o bem e o mal.",
    "o senhor dos anéis": "A jornada de um hobbit para destruir um anel poderoso.",
    "jurassic park": "Um parque temático que traz dinossauros de volta à vida, mas algo dá errado.",
    "titanic": "Um romance que se desenrola a bordo de um famoso navio que afunda.",
    "matrix": "Um homem descobre a verdade sobre a realidade e sua luta contra máquinas."
}

# Função para jogar
def jogar():
    # Escolher uma palavra aleatória
    palavra_secreta = random.choice(list(palavras.keys()))
    tentativas = 5  # Número de tentativas permitidas

    print(f"""
          Bem-vindo ao jogo de adivinhação!

          - Você tem que adivinhar a palavra secreta
          - Você Terá 5 chances para adivinhar
          - Dica: {palavras[palavra_secreta]}
          """)
    
    while tentativas > 0:
        palpite = input("Qual é a sua palpite? ").lower()

        if palpite == palavra_secreta:
            print("Parabéns! Você adivinhou a palavra!")
            resposta = input("Gostaria de jogar novamente ?: ").lower()
            if resposta == "sim":
                jogar()
                break
            else:
                print("Obrigado por jogar")
                break
        else:
            tentativas -= 1
            print(f"Errado! Você ainda tem {tentativas} tentativas restantes.")

    if tentativas == 0:
        print(f"Você perdeu! A palavra era '{palavra_secreta}'.")
        resposta = input("Gostaria de jogar novamente ?: ").lower()
        if resposta == "sim":
            jogar()
            
        else:
            print("Obrigado por jogar")
            


jogar()