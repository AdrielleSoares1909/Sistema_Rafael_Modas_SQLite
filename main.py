""" 

    📦 Projeto: Sistema Rafael Modas 

    Etapas do projeto: 
    -----------------------------
    Etapa 1 (CRUD)

    ✅ Cadastrar roupa
    ✅ Listar roupas
    ✅ Buscar roupa
    🔜 Remover roupa
    ------------------------------
    Etapa 2

    Alterar preço
    Alterar estoque
    Registrar venda
    Repor estoque
    ------------------------------
    Etapa 3

    Calcular valor total do estoque
    Produto mais caro
    Produto mais barato
    -----------------------------
    Etapa 4

    Salvar em arquivo .txt
    Ler arquivo .txt
    ----------------------------------
    Etapa 5

    Organizar tudo em funções
    Deixar o código limpo

---------------------------------------------------------------------------------------
    OBS:::: >>> # break,ele realmente interrompe alguma coisa. 
                #Só que ele interrompe apenas loops (for e while). Sai do for.

# Mas a função continua executando o restante do código depois do for. 
# Para sair da função.Quando o Python encontra o return, 
# ele para de executar a função e volta para quem a chamou (no seu caso, o menu).
# >>>> Resumindo<<<<<
# break → sai de um for ou while.
# return → sai de uma função.
    
"""

from estoque import cadastrar_roupas
from  estoque import listar_roupas
from estoque import buscar_roupa
from estoque import remover_roupa
from estoque import alterar_preco
from estoque import valor_total_estoque
from vendas import registrar_venda
from vendas import listar_historico_vendas
from database import criar_tabela_roupas
from database import criar_tabela_vendas
from validacoes import ler_opcao




criar_tabela_roupas()
criar_tabela_vendas()

while True:
    

    print("------- MENU --------")
    print("1 = CADASTRAR ROUPA ")
    print("2 = LISTAR ROUPAS ")
    print("3 = BUSCAR ROUPA ")
    print("4 = REMOVER ROUPA ")
    print("5 = ALTERAR PRECO ")
    print("6 = REGISTRAR VENDA ")
    print("7 = VALOR TOTAL DO ESTOQUE")
    print("8 = LISTAR HISTORICO DE VENDAS ")
    print("9 = SAIR ")

    opcao = ler_opcao()

    if opcao == 1:

        cadastrar_roupas()
       

    elif opcao == 2:

        listar_roupas()
     
    
    elif opcao == 3:

        buscar_roupa()
        

    elif opcao == 4:

        remover_roupa()
        

    elif opcao == 5:

        alterar_preco()
        

    elif opcao == 6:

        registrar_venda()
        
    elif opcao == 7:

        valor_total_estoque()

    elif opcao == 8:

        listar_historico_vendas()
        
    elif opcao == 9:

        print("Saindo do sistema!")
        break

   



