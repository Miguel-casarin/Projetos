import tkinter as tk
import exe_consulta2

def adicionar_mensagem(mensagem):
    campo_texto.insert(tk.END, mensagem + "\n")
    campo_texto.see(tk.END)

def exibir_livros():
    livros = exe_consulta2.livros()
    for livro in livros:
        adicionar_mensagem(f"Livro: {livro[0]}, Autor: {livro[1]}, Valor: {livro[2]}, Editora: {livro[3]}")

def exibir_autores():
    autores = exe_consulta2.autores()
    for autor in autores:
        adicionar_mensagem(f"Livro: {autor[0]}, Autor: {autor[1]}, Valor: {autor[2]}, Editora: {autor[3]}")

def exibir_autoras():
    autoras = exe_consulta2.autoras()
    for autora in autoras:
        adicionar_mensagem(f"Livro: {autora[0]}, Autor: {autora[1]}, Valor: {autora[2]}, Editora: {autora[3]}")

def exibir_dados():
    dados = exe_consulta2.dados()
    for dado in dados:
        adicionar_mensagem(f"ID: {dado[0]}, Livro: {dado[1]}, Autor: {dado[2]}, Valor: {dado[3]}, Editora: {dado[4]}, Sexo: {dado[5]}")

window = tk.Tk()
window.title("Consulta de Livros")

campo_texto = tk.Text(window, height=40, width=90)
campo_texto.pack(padx=5, pady=5)

# Container para os botões
button_frame = tk.Frame(window)
button_frame.pack()

# Botões
botao_livros = tk.Button(button_frame, text="Todos Livros", command=exibir_livros)
botao_livros.pack(side=tk.LEFT, padx=3, pady=3)

botao_autores = tk.Button(button_frame, text="Autores", command=exibir_autores)
botao_autores.pack(side=tk.LEFT, padx=3, pady=3)

botao_autoras = tk.Button(button_frame, text="Autoras", command=exibir_autoras)
botao_autoras.pack(side=tk.LEFT, padx=3, pady=3)

botao_dados = tk.Button(button_frame, text="Dados", command=exibir_dados)
botao_dados.pack(side=tk.LEFT, padx=3, pady=3)

window.mainloop()
