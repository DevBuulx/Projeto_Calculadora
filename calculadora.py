import tkinter as tk

def press_key(key):
    entry.insert(tk.END, key)

def calcular():
    try:
        expressao = entry.get().replace(',', '.')
        resultado = eval(expressao)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultado).replace('.', ','))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def limpar_tudo():
    entry.delete(0, tk.END)

def inverter_sinal():
    entrada = entry.get()
    if entrada and entrada[0] == '-':
        entrada = entrada[1:]
    else:
        entrada = '-' + entrada
    entry.delete(0, tk.END)
    entry.insert(tk.END, entrada)

janela = tk.Tk()
janela.title("Calculadora")
janela.configure(bg="black")

background_color = "black"
button_color = "#727c77"  # Cimento Queimado
text_color = "#FFFFFF"

entry = tk.Entry(janela, width=30, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)
entry.config(bg=background_color, fg=text_color)

botoes = [
    'AC', '%', '+/-', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '0', '.', '=', 
]

row_val = 1
col_val = 0

button_width = 6
button_height = 3

for button_text in botoes:
    if button_text == 'AC':
        button = tk.Button(janela, text=button_text, padx=20, pady=20, font=("Arial", 16), command=limpar_tudo, width=button_width, height=button_height)
    elif button_text == '%':
        button = tk.Button(janela, text=button_text, padx=20, pady=20, font=("Arial", 16), command=calcular, width=button_width, height=button_height)
    elif button_text == '+/-':
        button = tk.Button(janela, text=button_text, padx=20, pady=20, font=("Arial", 16), command=inverter_sinal, width=button_width, height=button_height)
    elif button_text == '=':
        button = tk.Button(janela, text=button_text, padx=20, pady=20, font=("Arial", 16), command=calcular, width=button_width, height=button_height)
    else:
        button = tk.Button(janela, text=button_text, padx=20, pady=20, font=("Arial", 16), command=lambda key=button_text: press_key(key), width=button_width, height=button_height)
    button.grid(row=row_val, column=col_val, padx=5, pady=5, ipadx=10, ipady=10)
    button.config(bg=button_color, fg=text_color)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

janela.mainloop()
