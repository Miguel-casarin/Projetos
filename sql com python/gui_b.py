import tkinter as tk
from tkinter import scrolledtext
import conector

def conectar():
    conexao = conector.conection_db()
    cursor = conexao.cursor()
    return conexao, cursor

def fechar_conexao(conexao, cursor):
    cursor.close()
    conexao.close()

def executar_consulta(query):
    conexao, cursor = conectar()
    cursor.execute(query)
    resultados = cursor.fetchall()
    fechar_conexao(conexao, cursor)
    return resultados

def mostrar_resultados(resultados, texto_resultado):
    texto_resultado.delete(1.0, tk.END)
    for linha in resultados:
        texto_resultado.insert(tk.END, f"{linha}\n")

def todos_os_livros(texto_resultado):
    query = "SELECT livro, autor, valor, editora FROM LIVROS"
    resultados = executar_consulta(query)
    mostrar_resultados(resultados, texto_resultado)

def livros_autores(texto_resultado):
    query = "SELECT livro, autor, valor, editora FROM LIVROS WHERE sexo = 'M'"
    resultados = executar_consulta(query)
    mostrar_resultados(resultados, texto_resultado)

def livros_autoras(texto_resultado):
    query = "SELECT livro, autor, valor, editora FROM LIVROS WHERE sexo = 'F'"
    resultados = executar_consulta(query)
    mostrar_resultados(resultados, texto_resultado)

def todos_os_dados(texto_resultado):
    query = "SELECT * FROM LIVROS"
    resultados = executar_consulta(query)
    mostrar_resultados(resultados, texto_resultado)

def sair(root):
    root.destroy()

def abrir_janela():
    root = tk.Tk()
    root.title("Consulta ao Banco de Dados de Livros")

    texto_resultado = scrolledtext.ScrolledText(root, width=100, height=20)
    texto_resultado.pack(pady=10)

    frame_botoes = tk.Frame(root)
    frame_botoes.pack(pady=10)

    btn_todos_os_livros = tk.Button(frame_botoes, text="Todos os Livros", command=lambda: todos_os_livros(texto_resultado))
    btn_todos_os_livros.grid(row=0, column=0, padx=5)

    btn_livros_autores = tk.Button(frame_botoes, text="Livros Autores", command=lambda: livros_autores(texto_resultado))
    btn_livros_autores.grid(row=0, column=1, padx=5)

    btn_livros_autoras = tk.Button(frame_botoes, text="Livros Autoras", command=lambda: livros_autoras(texto_resultado))
    btn_livros_autoras.grid(row=0, column=2, padx=5)

    btn_todos_os_dados = tk.Button(frame_botoes, text="Todos os Dados", command=lambda: todos_os_dados(texto_resultado))
    btn_todos_os_dados.grid(row=0, column=3, padx=5)

    btn_sair = tk.Button(frame_botoes, text="Sair", command=lambda: sair(root))
    btn_sair.grid(row=0, column=4, padx=5)

    root.mainloop()

if __name__ == "__main__":
    abrir_janela()
