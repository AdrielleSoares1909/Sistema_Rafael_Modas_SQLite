

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

def criar_tabela_roupas():

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


def criar_tabela_vendas():

    conexao = criar_conexao()
    cursor = conexao.cursor()

   

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tamanho TEXT NOT NULL,
        quantidade_vendida INTEGER NOT NULL,
        preco_unitario REAL NOT NULL,
        valor_total REAL NOT NULL,
        nome_cliente TEXT NOT NULL,
        data_venda TEXT NOT NULL
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
    
def alterar_preco_db(nome, tamanho, preco):

    conexao = criar_conexao()
    cursor = conexao.cursor()

    

    cursor.execute("""

        UPDATE  roupas
                   
        SET preco = ?

        WHERE nome = ?

        AND tamanho = ? 
                   
    """,

        (preco, nome, tamanho)                    

   )
    
    
    conexao.commit()
   

    linhas_alteradas = cursor.rowcount

    conexao.close()

    return linhas_alteradas

def deletar_roupa_db(nome, tamanho):

    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("""
    
        DELETE FROM  roupas
                       
        WHERE nome = ?
    
        AND tamanho = ? 
                       
        """,
    
        (nome, tamanho)                    
    
       )
        
    

    conexao.commit()
       
    
    linhas_alteradas = cursor.rowcount
    
    conexao.close()
    
    return linhas_alteradas


def registrar_venda_db(
        nome,
        tamanho,
        quantidade_vendida,
        preco_unitario,
        valor_total,
        nome_cliente,
        data_venda
    ):

    conexao = criar_conexao()
    cursor = conexao.cursor()

    cursor.execute("""
                       
        INSERT INTO  vendas (nome,tamanho,quantidade_vendida,preco_unitario,valor_total,nome_cliente,data_venda)
                       
        VALUES (?, ?, ?, ?, ?, ?, ?) 
                       
        """,
        (nome, tamanho, quantidade_vendida, preco_unitario,valor_total,nome_cliente,data_venda)
        
        ) 

    conexao.commit()
    conexao.close()

def atualizar_estoque_db(nome, tamanho, novo_estoque):

    conexao = criar_conexao()
    cursor = conexao.cursor()
    
        
    
    cursor.execute("""
    
        UPDATE  roupas
                       
        SET estoque = ?

        WHERE nome = ?
    
        AND tamanho = ? 
                       
        """,
    
            (novo_estoque, nome, tamanho)   
    
       )
        
        
    conexao.commit()
       
    
    linhas_alteradas = cursor.rowcount
    
    conexao.close()
    
    return linhas_alteradas


def historico_vendas_db():

    conexao = criar_conexao()
    cursor = conexao.cursor()
    
    cursor.execute("""
    
        SELECT * FROM vendas
    
    """)
    
    vendas = cursor.fetchall()
        
    conexao.close()
    return vendas



def valor_total_estoque_db():

    conexao = criar_conexao()
    cursor = conexao.cursor()
        
    cursor.execute("""
        
        SELECT SUM(preco * estoque)

        FROM roupas

        
        
    """)
        
    total = cursor.fetchone()
            
    conexao.close()
    return total[0]