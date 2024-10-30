import os
import random

def limpar_prompt():
    os.system("cls" if os.name == "nt" else "clear")

def quiz():
    perguntas = {
        "Qual é a capital da França?": {
            "opções": ["A) Berlim", "B) Madri", "C) Paris", "D) Roma"],
            "resposta": "C"
        },
        "Qual é o maior planeta do sistema solar?": {
            "opções": ["A) Terra", "B) Marte", "C) Júpiter", "D) Saturno"],
            "resposta": "C"
        },
        "Quem escreveu 'Romeu e Julieta'?": {
            "opções": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen"],
            "resposta": "B"
        },
        "Qual é o elemento químico com símbolo 'O'?": {
            "opções": ["A) Ouro", "B) Oxigênio", "C) Ósmio", "D) Carbono"],
            "resposta": "B"
        },
        "Em que ano o homem chegou à Lua pela primeira vez?": {
            "opções": ["A) 1965", "B) 1969", "C) 1972", "D) 1975"],
            "resposta": "B"
        }
    }

    pontuacao = 0

    print("Bem-vindo ao Quiz! Responda as perguntas abaixo:\n")

    for pergunta, dados in perguntas.items():
        print("-" * 50)
        print(pergunta)
        print("-" * 50)
        opcoes = dados["opções"]
        random.shuffle(opcoes)
        for opcao in opcoes:
            print(opcao)
        resposta = input("Digite a letra da sua resposta: ").upper()
        limpar_prompt()

        if resposta == dados["resposta"]:
            print("Correto!\n")
            pontuacao += 10
        else:
            print(f"Incorreto! A resposta correta é {dados['resposta']}.\n")
    if pontuacao == 0:
        print(f"Sua pontuação final é {pontuacao} e você errou um total de {len(perguntas)} perguntas.")
    else:
        print(f"Sua pontuação final é {pontuacao} e você acertou {len(perguntas)} perguntas.")
    
quiz()
