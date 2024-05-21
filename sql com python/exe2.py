import conector  

def insert_db(titulo_livro, nome_autor, sexo_autor, numero_paginas, valor_livro, estado_autor, ano_publicacao, editora):
    conexao = conector.conection_db()
    cursor = conexao.cursor()

    insere = """
        INSERT INTO LIVROS (livro, autor, sexo, paginas, valor, estado, ano, editora) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (titulo_livro, nome_autor, sexo_autor, numero_paginas, valor_livro, estado_autor, ano_publicacao, editora)
    cursor.execute(insere, valores)
    conexao.commit()

    cursor.execute("SELECT * FROM LIVROS")
    result = cursor.fetchall()
    print(result)

    cursor.close()
    conexao.close()
