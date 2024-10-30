def contador_de_vogais(string):
    vogais = "aeiouAEIOUéáúãÚàêâÊôÔÂ"
    contador = 0
    
    for letra in string:
        if letra in vogais:
            contador += 1
            
    return contador


palavra = input("Informe a palavra: ")

quatidade_vogais = contador_de_vogais(palavra)

print(f"Esta palavra contém {quatidade_vogais} vogais!")
