import conector

conexao = conector.conection_db()
cursor = conexao.cursor()

inicializa = input('Quer consultar o banco (Y/N): ').upper()

while inicializa == 'Y':
    
    def menu():
        print("Selecione uma opção:")
        print("1. Todos os livros")
        print("2. Livros autores")
        print("3. Livros autoras")
        print("4. Todos os dados da tabela")
        print("0. Sair do programa")

    while True:
        menu()
        comand = int(input('comando: '))

        if comand == 0:
            break
        elif comand == 1:
            cursor.execute("SELECT livro, autor, valor, editora FROM LIVROS")
        elif comand == 2:
            cursor.execute("SELECT livro, autor, valor, editora FROM LIVROS WHERE sexo = 'M'")
        elif comand == 3:
            cursor.execute("SELECT livro, autor, valor, editora FROM LIVROS WHERE sexo = 'F'")
        elif comand == 4:
            cursor.execute("SELECT * FROM LIVROS")

        selec_tabela = cursor.fetchall()
        print(selec_tabela)

    inicializa = input('Quer consultar o banco (Y/N): ').upper()

cursor.close()
conexao.close()
