import conector

conexao = conector.conection_db()
cursor = conexao.cursor()

def insert_db(livro, autor, sexo, paginas, valor, estado, ano, editora):
    insere = "INSERT INTO LIVROS (livro, autor, sexo, paginas, valor, estado, ano, editora) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (livro, autor, sexo, paginas, valor, estado, ano, editora)
    cursor.execute(insere, valores)
    conexao.commit()

livro = input('Livro: ').lower()
autor = input('Autor: ').lower()
sexo = input('Sexo autor (M/F): ').upper()
paginas = int(input('Número de páginas: '))
valor = float(input('Valor do livro: '))
estado = input('Estado do autor: ').upper()
ano = int(input('Ano de publicação: '))
editora = input('Editora: ').lower()

insert_db(livro, autor, sexo, paginas, valor, estado, ano, editora)

cursor.execute("SELECT * FROM LIVROS")
result = cursor.fetchall()
print(result)

cursor.close()
conexao.close()
