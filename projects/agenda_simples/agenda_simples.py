import os

agenda = []

def limpar_prompt():
    os.system("cls" if os.name == "nt" else "clear")

def acoes():
    
    def adicionar():
        tarefa = input("Digite sua tarefa: ")
        print("-" * 43)
        agenda.append(tarefa)
        limpar_prompt()
        print(f"A tarefa de nome: {tarefa} foi adicionada")
        
        
        
        
    def visualizar():
        if agenda:
            limpar_prompt()
            print("Tarefas:")
            for indice, tarefa in enumerate(agenda, start=1):
                print(f"{indice} - {tarefa}")
        else:
            limpar_prompt()
            print("Tarefas inexistentes.")
            



        
    def remover():
        visualizar()
        try:
            indice = input("Digite o número da tarefa para remover: ")
            indice = int(indice)
            
            if 1 <= indice <= len(agenda):
                tarefa_removida= agenda.pop(indice - 1)
                limpar_prompt()
                print(f"""Tarefas Removidas: {tarefa_removida}""")
            else:
                print("Tarefa não encontrada")
    
        except:
            print("Entrada inválida. Por favor, digite um número.")
        
    return adicionar,visualizar,remover
    
adicionar, visualizar, remover = acoes()
    
    


while True:
    
    
    print("-" * 43)
    print("""
          1 - Adicionar Tarefas
          2 - Visualizar Tarefas
          3 - Remover Tarefas
          4 - Sair 
          """)
    print("-" * 43)
    
    opcao = input("O que deseja fazer ?: ")
    print("-" * 43)
    
    try:
        if opcao == "4":
            break
        elif opcao == "1":
            adicionar()
        elif opcao == "2":
            visualizar()
        elif opcao == "3":
            remover()
        else:
            print("Opção invalida")
    except:
        continue