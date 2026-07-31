

from database import cadastrar_roupa
from database import listar_roupas_db
from database import buscar_roupa_db
from database import alterar_preco_db
from database import deletar_roupa_db
from database import valor_total_estoque_db
from validacoes import ler_nome
from validacoes import ler_preco
from validacoes import ler_estoque
from validacoes import ler_tamanho


def cadastrar_roupas():

    nome = ler_nome("Digite o nome da roupa: ")
    preco = ler_preco()
    estoque = ler_estoque()
    tamanho = ler_tamanho()

    cadastrar_roupa(nome, preco, estoque, tamanho)

    print("✅ Roupa cadastrada com sucesso!")

    

def listar_roupas(): # mostra na tela.

    roupas =  listar_roupas_db()

    if not roupas:

        print("LISTA VAZIA")
        return # usando para sair da função

    for roupa in roupas:
        print(f"ID: {roupa[0]}")
        print(f"Nome: {roupa[1]}")
        print(f"Preço: R$ {roupa[2]:.2f}")
        print(f"Estoque: {roupa[3]}")
        print(f"Tamanho: {roupa[4]}")

    

def buscar_roupa():

    localizar_roupa = ler_nome("Digite o nome da roupa: ")

    localizar_tamanho = ler_tamanho()

    

    roupa = buscar_roupa_db(localizar_roupa ,localizar_tamanho)

    if roupa == None:

        print("ROUPA NÃO LOCALIZADA NO SISTEMA!")
    
    else:
        print(f"ID: {roupa[0]}")
        print(f"Nome: {roupa[1]}")
        print(f"Preço: R$ {roupa[2]:.2f}")
        print(f"Estoque: {roupa[3]}")
        print(f"Tamanho: {roupa[4]}")

            
    

def remover_roupa():

    nome = ler_nome("Digite o nome da roupa que deseja remover: ")

    excluir_tamanho = ler_tamanho()

    linhas = deletar_roupa_db(nome, excluir_tamanho)

    if linhas == 0:
    
        print("ROUPA NÃO ENCONTRADA")
    
    else:
            
        print("ROUPA REMOVIDA COM SUCESSO")


def alterar_preco():

    nome = ler_nome("Digite o nome da roupa que deseja alterar: ")

    alterar_tamanho = ler_tamanho()

    novo_preco = ler_preco()

    linhas = alterar_preco_db(nome, alterar_tamanho, novo_preco)

    if linhas == 0:

        print("ROUPA NÃO ENCONTRADA")

    else:
        
        print("PREÇO ALTERADO COM SUCESSO")
            


def valor_total_estoque():

    total_estoque = valor_total_estoque_db()

    if total_estoque is None:

        total_estoque = 0

    print(f"Valor total do estoque: R$ {total_estoque:.2f}")
    

    