# Exercício 6: Funções Aninhadas
# Desenvolva uma função chamada calcular_volumes que recebe o raio de um cilindro e sua altura. 
# Dentro dessa função, crie duas funções internas:

# volume_cilindro que calcula o volume do cilindro (V = πr²h).
# volume_esfera que calcula o volume de uma esfera com o mesmo raio (V = (4/3)πr³).
# A função calcular_volumes deve retornar ambos os volumes. Utilize a função para calcular os volumes com raio = 3 e altura = 5, 
# e exiba os resultados.

pi = 3.14

def calcular_volumes(diametro, altura):
    
    raio = diametro / 2
    
    def volume_cilindro(raio, altura):
        area_base = pi * (raio ** 2)  
        volume = area_base * altura    
        return volume

    def volume_esfera(raio):
        volume = (4/3) * pi * (raio ** 3)  
        return volume
    
    resultado_cilindro = volume_cilindro(raio, altura)
    resultado_volume_esfera = volume_esfera(raio)

    return resultado_cilindro, resultado_volume_esfera


resultado_cilindro, resultado_volume_esfera = calcular_volumes(3, 5)


print(f"Volume do Cilindro: {resultado_cilindro:.2f} cm³")
print(f"Volume da Esfera: {resultado_volume_esfera:.2f} cm³")
