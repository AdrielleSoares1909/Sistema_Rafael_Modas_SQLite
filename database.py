

import sqlite3

conexao = sqlite3.connect("app.db") # conecao variavel , a chave para entrar no banco de dados

cursor = conexao.cursor() # "Se o cursor vai trabalhar com essa conexão... então ele deve nascer da conexão."

""" 
cursor.execute(  # executa o comando.
CREATE TABLE IF NOT EXISTS roupas ( # CREATE TABLE = cria uma tabela.# IF NOT EXISTS = só cria se ela ainda não existir. # roupas = nome da tabela.
    id INTEGER PRIMARY KEY AUTOINCREMENT, # identificador único que aumenta automaticamente.
    nome TEXT NOT NULL, # texto.
    preco REAL NOT NULL, # número decimal.
    estoque INTEGER NOT NULL, # número inteiro.
    tamanho TEXT NOT NULL # texto.
    )
"""

def criar_conexao():
    conexao = sqlite3.connect("app.db")
    return conexao

def criar_tabela():

    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roupas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL,
        tamanho TEXT NOT NULL
    )
    """)

    conexao.commit()
    conexao.close()

# >>>> Os ? são substituídos automaticamente pelos valores das variáveis.

def cadastrar_roupa(nome, preco, estoque, tamanho):

    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("""
                   
    INSERT INTO  roupas (nome, preco, estoque, tamanho)
                   
    VALUES (?, ?, ?, ?) 
                   
    """,
    (nome, preco, estoque, tamanho)
    
    ) 

    conexao.commit()
    conexao.close()


def listar_roupas_db(): # busca no banco.

    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("""

        SELECT * FROM roupas

    """)

    roupas = cursor.fetchall()
    
    conexao.close()
    return roupas


def buscar_roupa_db(nome, tamanho):

    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("""

        SELECT * FROM roupas

        WHERE nome = ?

        AND tamanho = ? 
                   
    """,

        (nome, tamanho)                    

   )

    roupa = cursor.fetchone()

   

    conexao.close()
    return roupa
    


