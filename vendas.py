
from database import buscar_roupa_db
from database import atualizar_estoque_db
from database import registrar_venda_db





def registrar_venda():


    venda_roupa = input("Qual item do estoque foi vendido: ")

    venda_tamanho = input("Qual tamanho do item  do estoque foi vendido: ")

    roupa = buscar_roupa_db(venda_roupa, venda_tamanho)

    estoque = roupa[3]
    preco = roupa[2]
    nome = roupa[1]
    tamanho = roupa[4]

    if roupa is None:

        print("ROUPA NÃO LOCALIZADA NO SISTEMA!")

        return

    
    quantidade_vendida = int(input("Qual quantidade  do item  do estoque foi vendido: "))

    if estoque < quantidade_vendida:
            print(f"ESTOQUE INSUFICIENTE! Disponível: {estoque} unidade(s).")
            return

    if estoque >= quantidade_vendida:

        novo_estoque = estoque - quantidade_vendida
        
        atualizar_estoque_db(nome, tamanho, novo_estoque)

    nome_cliente = input("Digite o nome do cliente: ")

    data_venda = input("Digite a data da venda: ")

    valor_total =  preco * quantidade_vendida
        
    venda = registrar_venda_db(
        nome,
        tamanho,
        quantidade_vendida,
        preco,
        valor_total,
        nome_cliente,
        data_venda
    )

    print("COMPRA REALIZADA COM SUCESSO!")

   




           

                
        
    


def historico_vendas(vendas,roupa,nome_do_cliente,data_da_venda,quantidade_vendida):

    
        
    venda = {

        "nome": roupa["nome"],

        "tamanho": roupa["tamanho"],

        "quantidade_vendida" : quantidade_vendida, # Se a informação já está em uma variável, use a variável.

        "preco" : roupa["preco"],

        "valor_total" : roupa["preco"] * quantidade_vendida, # Se a informação já está em uma variável, use a variável.

        "nome_do_cliente" : nome_do_cliente,

        "data_da_venda" : data_da_venda,

    }

    vendas.append(venda)


def listar_historico_vendas(vendas):

    for venda in vendas:


        print(f"----------------------")
        print(f"PRODUTO: {venda['nome']}")
        print(f"TAMANHO: {venda['tamanho']}")
        print(f"QUANTIDADE VENDIDA: {venda['quantidade_vendida']}")
        print(f"PREÇO DA UNIDADE: R${venda['preco']}")
        print(f"PREÇO TOTAL DA VENDA: R${venda['valor_total']}")
        print(f"CLIENTE: {venda['nome_do_cliente']}")
        print(f"DATA DA VENDA: {venda['data_da_venda']}")
        print(f"----------------------")


    if not vendas:
        print("Nenhuma venda registrada.")
    return