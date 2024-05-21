# exe_consulta2.py

import conector

def livros():
    conexao = conector.conection_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT livro, autor, valor, editora FROM LIVROS")
    results = cursor.fetchall()
    cursor.close()
    conexao.close()
    return results

def autores():
    conexao = conector.conection_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT livro, autor, valor, editora FROM LIVROS WHERE sexo = 'M'")
    results = cursor.fetchall()
    cursor.close()
    conexao.close()
    return results

def autoras():
    conexao = conector.conection_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT livro, autor, valor, editora FROM LIVROS WHERE sexo = 'F'")
    results = cursor.fetchall()
    cursor.close()
    conexao.close()
    return results

def dados():
    conexao = conector.conection_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM LIVROS")
    results = cursor.fetchall()
    cursor.close()
    conexao.close()
    return results
