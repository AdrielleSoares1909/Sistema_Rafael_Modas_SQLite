
from database import buscar_roupa_db
from database import atualizar_estoque_db
from database import registrar_venda_db
from database import historico_vendas_db
from validacoes import ler_tamanho
from validacoes import ler_quantidade
from validacoes import ler_nome
from validacoes import ler_data




def registrar_venda():


    venda_roupa  = ler_nome("Digite o nome da roupa: ")

    venda_tamanho = ler_tamanho()

    
    roupa = buscar_roupa_db(venda_roupa, venda_tamanho)


    

    if roupa is None:
    
        print("ROUPA NÃO LOCALIZADA NO SISTEMA!")
    
        return

    estoque = roupa[3]
    preco = roupa[2]
    nome = roupa[1]
    tamanho = roupa[4]

    

    
    quantidade_vendida = ler_quantidade()

    if estoque < quantidade_vendida:

        print(f"ESTOQUE INSUFICIENTE! Disponível: {estoque} unidade(s).")

        return

    if estoque >= quantidade_vendida:

        novo_estoque = estoque - quantidade_vendida
        
        atualizar_estoque_db(nome, tamanho, novo_estoque)

    nome_cliente = ler_nome("Digite o nome do cliente: ")

    data_venda = ler_data()

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

   




def listar_historico_vendas():

    vendas = historico_vendas_db()



    if not vendas:
        print("Nenhuma venda registrada.")
        return

    for venda in vendas:


        print(f"----------------------")
        print(f"ID: {venda[0]}")
        print(f"PRODUTO: {venda[1]}")
        print(f"TAMANHO: {venda[2]}")
        print(f"QUANTIDADE VENDIDA: {venda[3]}")
        print(f"PREÇO DA UNIDADE: R${venda[4]}")
        print(f"PREÇO TOTAL DA VENDA: R$ {venda[5]:.2f}")
        print(f"CLIENTE: {venda[6]}")
        print(f"DATA DA VENDA: {venda[7]}")
        print(f"----------------------")
        
    return