def operacoes(primeiro_numero, segundo_numero):
    
    def adicao(primeiro_numero, segundo_numero):
        return primeiro_numero + segundo_numero
    
    def subtracao(primeiro_numero, segundo_numero):
       return primeiro_numero - segundo_numero
   
    def divisao(primeiro_numero, segundo_numero):
        return primeiro_numero / segundo_numero
    
    def mutiplicacao(primeiro_numero, segundo_numero):
        return primeiro_numero * segundo_numero

    return adicao(primeiro_numero, segundo_numero), subtracao(primeiro_numero, segundo_numero), divisao(primeiro_numero, segundo_numero) , mutiplicacao(primeiro_numero, segundo_numero)

while True:
    
    
    print("""
        Menu de Opções:
         1 - Somar
         2 - Subtrair
         3 - Mutiplicar
         4 - Dividir 
         5 - Sair do Programa 
          """)
    opcao = input("O que deseja fazer: ")
    print("-" * 50)
    if opcao == "5":
        print("Obrigado por usar nosso programa")
        break
    
    elif opcao in ["1", "2", "3", "4"]:
        
        primeiro_numero = input("Digite primeiro número: ")
        segundo_numero = input("Digite Segudno número: ")
        print("-" * 50)
        
        try:
            primeiro_numero = float (primeiro_numero)
            segundo_numero = float (segundo_numero)
            
            somar, subtrair, dividir, mutiplicar = operacoes(primeiro_numero, segundo_numero)
            
            if opcao == "1":
                print(f"O Resultado da soma entre {primeiro_numero} e {segundo_numero} é = {somar:.2f}")
            elif opcao == "2":
                print(f"O Resultado da subtração entre {primeiro_numero} e {segundo_numero} é = {subtrair:.2f}")
            elif opcao == "3":
                print(f"O Resultado da Mutiplicação entre {primeiro_numero} e {segundo_numero} é = {mutiplicar:.2f}")
            elif opcao == "4":
                print(f"O Resultado da Divisão entre {primeiro_numero} e {segundo_numero} é = {dividir:.2f}")
        except:
            print("Entrada Invalida!")
            continue

