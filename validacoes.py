from datetime import datetime



def ler_opcao():
     
    while True:

        try:
        
            opcao = int(input("Digite a opcao desejada: "))

        except ValueError:
             
            print("Digite apenas números.")

            continue

        if opcao < 1 or opcao > 9:
            
            print("❌ A opcao deve ser entre 1 e 9.")
            
            continue

        return opcao


def ler_preco():


    while True:

        try:

            preco = float(input("Digite o preço da roupa: "))

        except ValueError:

            print("Preço inválido! Digite apenas números.")

            continue

        if preco <= 0:

            print("❌ O preço deve ser maior que zero.")

            continue
            
        return preco


def ler_quantidade():

    while True:
    
            try:
    
                quantidade = int(input("Digite a quantidade de peça comprada: "))
    
            except ValueError:
    
                print("Quantidade inválida! Digite apenas números.")
    
                continue
    
            if quantidade <= 0:
    
                print("❌ A quantidade deve ser maior que zero.")
    
                continue
                
            return quantidade

def ler_estoque():


    while True:
        
                try:
        
                    estoque = int(input("Digite o estoque de peça comprada: "))
        
                except ValueError:
        
                    print("❌ Estoque inválido! Digite apenas números.")
        
                    continue
        
                if estoque <= 0:
        
                    print("❌ O estoque deve ser maior que zero.")
        
                    continue
                    
                return estoque


def ler_nome(mensagem):


    while True:
             
            
        nome = input(mensagem)
                    
        if nome.strip() == "":

            print("❌ O nome não pode estar vazio.")

            continue

        return nome.strip()


def ler_tamanho():


    TAMANHOS_VALIDOS = [
    "PP",
    "P",
    "M",
    "G",
    "GG",
    "GG1",
    "GG2",
    "XG",
    "XXG",
    "EXG",
    "EG",
    "36",
    "38",
    "40",
    "42",
    "44",
    "46",
    "48",
    "50",
    "52",
    "54",
    "56",
    "58",
    "60"
]

    while True:
                  
                 
            tamanho = input("Digite o tamanho da peça: ").strip().upper()
                         
            if tamanho == "":
     
                print("❌ O tamanho não pode estar vazio.")
     
                continue

            if tamanho not in TAMANHOS_VALIDOS:

               print("❌ O tamanho não pode ser cadastrado.")

               continue  
     
            return tamanho


        

def ler_data():

    while True:

        data = input("Digite a data da compra realizada: ")

        if data.strip() == "":
        
            print("❌ Data vazia.")

            continue

        try:
  
                 
            datetime.strptime(data, "%d/%m/%Y")


        except ValueError:
        
            print("❌  Data inválida. Digite no formato dd/mm/aaaa..")
                
            continue

        return data
     

        

            

        




   