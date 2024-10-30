import tkinter as tk
import time

def atualizar_relogio():
    
    hora_atual = time.strftime('%H:%M:%S')
    rotulo.config(text=hora_atual)
    rotulo.after(1000, atualizar_relogio)


janela = tk.Tk()
janela.title("Relógio Digital")


rotulo = tk.Label(janela, font=('Helvetica', 48), fg='black')
rotulo.pack(pady=20)

atualizar_relogio()
janela.mainloop()
