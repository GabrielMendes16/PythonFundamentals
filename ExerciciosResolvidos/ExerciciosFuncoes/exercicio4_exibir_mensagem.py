# Exercício 4: Função Sem Retorno
# Crie uma função chamada exibir_mensagem que recebe uma string como parâmetro e imprime a mensagem.
# Adicione uma condição dentro da função que, se a mensagem for "Bom dia", também imprima "Tenha um ótimo dia!". 
# Teste a função com as mensagens "Bom dia" e "Boa noite".

def exibir_mensagem(mensagem):
    print("Bom Dia")
    if mensagem == "Bom Dia":
        print("Tenha um ótimo dia!")

print(exibir_mensagem("Bom Dia"))