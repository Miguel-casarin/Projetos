import tkinter as tk

window = tk.Tk()

for i in range(16):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

livro_txt = tk.Label(window, text="Titulo Livro:", foreground="black", width=20, height=2)
livro_txt.grid(row=0, column=0, sticky='w', padx=5, pady=5)

livro_txtbox = tk.Entry(window, foreground="black", background="#D3D3D3", width=50)
livro_txtbox.grid(row=0, column=1, padx=5, pady=5)

autor_txt = tk.Label(window, text="Nome Autor:", foreground="black", width=20, height=2)
autor_txt.grid(row=1, column=0, sticky='w', padx=5, pady=5)

autor_txtbox = tk.Entry(window, foreground="black", background="#D3D3D3", width=50)
autor_txtbox.grid(row=1, column=1, padx=5, pady=5)

sexo_autor_txt = tk.Label(window, text="Sexo Autor (M/F):", foreground="black", width=20, height=2)
sexo_autor_txt.grid(row=2, column=0, sticky='w', padx=5, pady=5)

sexo_autor_txtbox = tk.Entry(window, foreground="black", background="#D3D3D3", width=50)
sexo_autor_txtbox.grid(row=2, column=1, padx=5, pady=5)

paginas_txt = tk.Label(window, text="Numero Paginas:", foreground="black", width=20, height=2)
paginas_txt.grid(row=3, column=0, sticky='w', padx=5, pady=5)

paginas_txtbox = tk.Entry(window, foreground="black", background="#D3D3D3", width=50)
paginas_txtbox.grid(row=3, column=1, padx=5, pady=5)

valor_txt = tk.Label(window, text="Valor do livro (use ponto no lugar da virgula):", foreground="black", width=35, height=2)
valor_txt.grid(row=4, column=0, sticky='w', padx=5, pady=5)

valor_txtbox = tk.Entry(window, foreground="black", background="#D3D3D3", width=50)
valor_txtbox.grid(row=4, column=1, padx=5, pady=5)

estado_txt = tk.Label(window, text="Estado do Autor:", foreground="black", width=20, height=2)
estado_txt.grid(row=5, column=0, sticky='w', padx=5, pady=5)

estado_txtbox = tk.Entry(window, foreground="black", background="#D3D3D3", width=50)
estado_txtbox.grid(row=5, column=1, padx=5, pady=5)

ano_txt = tk.Label(window, text="Ano de Publicacao:", foreground="black", width=20, height=2)
ano_txt.grid(row=6, column=0, sticky='w', padx=5, pady=5)

ano_txtbox = tk.Entry(window, foreground="black", background="#D3D3D3", width=50)
ano_txtbox.grid(row=6, column=1, padx=5, pady=5)

editora_txt = tk.Label(window, text="Editora:", foreground="black", width=20, height=2)
editora_txt.grid(row=7, column=0, sticky='w', padx=5, pady=5)

editora_txtbox = tk.Entry(window, foreground="black", background="#D3D3D3", width=50)
editora_txtbox.grid(row=7, column=1, padx=5, pady=5)

#botão
enviar_btn = tk.Button(window, text="Enviar", width=10, command=lambda: enviar_dados())
enviar_btn.grid(row=8, column=1, sticky='e', padx=5, pady=5)

def enviar_dados():
    titulo_livro = livro_txtbox.get()
    nome_autor = autor_txtbox.get()
    sexo_autor = sexo_autor_txtbox.get()
    numero_paginas = paginas_txtbox.get()
    valor_livro = valor_txtbox.get()
    estado_autor = estado_txtbox.get()
    ano_publicacao = ano_txtbox.get()
    editora = editora_txtbox.get()
    
window.mainloop()