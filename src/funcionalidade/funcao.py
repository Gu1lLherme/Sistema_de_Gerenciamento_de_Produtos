# Funcionalidade de Menu de Exibição
def menuPricipal():
    print("=" * 8, "Sistema de Gerencimento de Produtos", "=" * 8)    
    print("1 - Cadastrar Produto")
    print("2 - Consultar Produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - SAIR")
    print("==" * 25)

def menuTipoProduto():
    # Menu para exibir os tipos de classificação de produtos
    print("==" * 8,"Tipo do produto", "==" * 8)
    print("1 - Perecivel")
    print("2 - Não perecivel")
    print("3 - Higiene Pessoal")
    print("4 - Produto de limpeza")
    print("==" * 25)

def contadorLinhas():
    # retorna valor total do número de linhas existentes no arquivo .txt
    # Contagem de Linhas para determinar a ultima posição das linhas enumerada
    with open("src\historico\estoque.txt", "r") as file:
        numeroLinha = file.readlines()
        ultimaLinha = len(numeroLinha)
        ultimaLinha += 1
        return ultimaLinha
    
# Funcionalidade Cadastrar Produtos 
def cadastrarProduto():

    nomeProduto = str(input("Nome do produto: "))
    quantidade  = int(input("Quantidade do produto [UN]: "))
    posicao = contadorLinhas()
    
    menuTipoProduto()
    
    # NOTA: adicionar um Try para n querbrar o codigo
    escolhaTipoProduto = str(input("Tipo do produto: ")) 
    # Seleção para escolher a classificação do produto
    if escolhaTipoProduto == '1':
        tipoProduto = "Perecivel"
    elif escolhaTipoProduto ==  '2':
        tipoProduto = "Nao perecivel"
    elif escolhaTipoProduto == '3':
        tipoProduto = "Higiene Pessoal"
    elif escolhaTipoProduto == '4':
        tipoProduto = "Produto de Limpeza"
    else:
        tipoProduto = "Indeterminado"
    
    # Salvo/Adiciono as informações fornecidas pelo usuario em um arquivo .txt 
    with open("src\historico\estoque.txt", "a") as file:
        file.write(f"{posicao} - Nome do produto: {nomeProduto} | Quantidade do produto [UN]: {quantidade} | Tipo do Produto: {tipoProduto}\n")
 
 
# Função consultarProduto, Exibe no Terminal um print do arquivo .txt a qual é armazenado as informações dos produtos       
def consultarProduto():
    with open("src\historico\estoque.txt", "rt") as file:
        leituraEstoque = file.read()
        print(leituraEstoque)



def atualizarProduto():
    # Exibe o estoque na tela 
    consultarProduto()
     # Conta o número total de linhas no arquivo
    numeroTotalLinhas = contadorLinhas()
    novaLinhaAtualizada = int(input("Digite o número da linha para alterar: "))
    
    if novaLinhaAtualizada <= numeroTotalLinhas:
        with open("src\historico\estoque.txt", "r") as file:
            linhas = file.readlines()

        # Verifica se a linha desejada existe
        if novaLinhaAtualizada <= len(linhas):
            # Altera a linha desejada
            linhas[novaLinhaAtualizada - 1] = cadastrarProduto()
            
            # Escreve as alterações de volta no arquivo
            with open("src\historico\estoque.txt", "w") as file:
                file.writelines(linhas)
        else:
            print("Erro: Linha não encontrada.")
    else:
        print("Erro: Número da linha inválido.")
    
        
    