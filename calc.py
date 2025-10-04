import math
import tkinter as tk
import re 

def click(botao):
    if botao == "=":
        try:
            expressao = entrada.get()
            expressao = re.sub(r'√(\d+)', r'math.sqrt(\1)', expressao)         
            resultado = eval(expressao)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
    elif botao == "C":
        entrada.delete(0, tk.END)
    elif botao == "%":
        try:
            valor = float(entrada.get())
            resultado = valor / 100
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, str(resultado))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Erro")
    elif botao == "Del":
        expressao = entrada.get()
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, expressao[:-1])
        
    else:
        entrada.insert(tk.END, botao)

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, width=20, font=("Arial", 20), borderwidth=3, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4)

botoes = [
    "C", "√", "%", "Del",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "=", "+" 
]

linha, coluna = 1, 0
for botao in botoes:
    tk.Button(janela, text=botao, width=5, height=2, font=("Arial", 18),
              command=lambda b=botao: click(b)).grid(row=linha, column=coluna)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

janela.mainloop()
