

from database import cadastrar_roupa
from database import listar_roupas_db
from database import buscar_roupa_db
from database import alterar_preco_db
from database import deletar_roupa_db

def cadastrar_roupas(roupas):

    nome = input("Digite o nome da peça de roupa a ser cadastrada: ").strip().lower()
    preco = float(input("Digite o preço da peca de roupa a ser cadastrada: "))
    estoque = int(input("Digite a quantidade em estoque disponivel : "))
    tamanho = input("Digite o tamanho da peca de roupa a ser cadastrada: ").strip().lower()

    roupa = {

        "nome": nome,
        "preco" : preco,
        "estoque" : estoque,
        "tamanho": tamanho
    }

    cadastrar_roupa(nome, preco, estoque, tamanho) # database

    

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

    localizar_roupa = input("Qual roupa deseja localizar:  ").strip().lower()

    localizar_tamanho = input("Digite o tamanho da roupa a ser localizada: ").strip().lower()

    

    roupa = buscar_roupa_db(localizar_roupa ,localizar_tamanho)

    if roupa == None:

        print("ROUPA NÃO LOCALIZADA NO SISTEMA!")
    
    else:
        print(f"ID: {roupa[0]}")
        print(f"Nome: {roupa[1]}")
        print(f"Preço: R$ {roupa[2]:.2f}")
        print(f"Estoque: {roupa[3]}")
        print(f"Tamanho: {roupa[4]}")

            
    
def encontrar_roupa(roupas):



    buscar_roupa = input("Digite o nome da roupa: ").strip().lower()

    roupa_encontrada = False

    for roupa in roupas:

        
        if roupa["nome"].strip().lower() == buscar_roupa:

            roupa_encontrada = True

            print("---------------------")
            print(f"Nome: {roupa['nome']}")
            print(f"Preço: R${roupa['preco']}")
            print(f"Estoque: {roupa['estoque']}")
            print(f"Tamanho: {roupa['tamanho']}")
            print("---------------------")

            
            
    if not roupa_encontrada:
        print("ROUPA NÃO ENCONTRADA!")






def remover_roupa():

    excluir_roupa = input("Qual roupa deseja excluir do sistema: ")

    excluir_tamanho = input("Qual tamanho  deseja excluir do sistema: ")

    linhas = deletar_roupa_db(excluir_roupa, excluir_tamanho)

    if linhas == 0:
    
        print("ROUPA NÃO ENCONTRADA")
    
    else:
            
        print("ROUPA REMOVIDA COM SUCESSO")


def alterar_preco():

    alterar_roupa = input("Qual roupa deseja alterar no sistema: ")

    alterar_tamanho = input("Qual tamanho  deseja alterar no sistema: ")

    novo_preco = float(input("Qual sera o novo preco a ser cadastrado no sistema: "))

    linhas = alterar_preco_db(alterar_roupa, alterar_tamanho, novo_preco)

    if linhas == 0:

        print("ROUPA NÃO ENCONTRADA")

    else:
        
        print("PREÇO ALTERADO COM SUCESSO")
            


def valor_total_estoque(roupas):

    total_estoque = 0

    for roupa in roupas:

        total_estoque += roupa["estoque"] * roupa["preco"] 

    print(f"Valor total do estoque: R$ {total_estoque:.2f}")