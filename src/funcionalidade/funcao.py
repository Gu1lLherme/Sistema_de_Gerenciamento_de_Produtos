# Funcionalidade de Menu de Exibição
def menu():
    print("=" * 8, "Sistema de Gerencimento de Produtos", "=" * 8)    
    print("1 - Cadastrar Produto")
    print("2 - Consultar Produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - SAIR")
    print("=" * 20)

# Funcionalidade Cadastrar Produtos 
def cadastrarProduto():
    print("=" * 20)
    nomeProduto = str(input("Nome do produto: "))
    quantidade = int(input("Quantidade do produto [UN]: "))
    
    # Menu para exibir os tipos de classificação de produtos
    print("=" * 8,"Tipo do produto", "=" * 8)
    print("1 - Perecivel")
    print("2 - Não perecivel")
    print("3 - Produto de limpeza")
    
    # Seleção para escolher a classificação do produto
    # NOTA: adicionar um Try para n querbrar o codigo
    escolhaTipoProduto = int(input("Tipo do produto: ")) 
    
    if escolhaTipoProduto == 1:
        tipoProduto = "Perecivel"
    elif escolhaTipoProduto == 2:
        tipoProduto = "Não perecivel"
    elif escolhaTipoProduto == 3:
        tipoProduto = "Produto de Limpeza"
    
    # Salvo/Adiciono as informações fornecidas pelo usuario em um arquivo .txt 
    with open("estoque.txt", "a") as file:
        file.write(f"Nome do produto: {nomeProduto} | Quantidade do produto [UN]: {quantidade} | Tipo do Produto: {tipoProduto}")
        
def consultarProduto():
    with open("estoque.txt", "rt") as file:
        leituraEstoque = file.read()
        print(leituraEstoque)
        
        
    