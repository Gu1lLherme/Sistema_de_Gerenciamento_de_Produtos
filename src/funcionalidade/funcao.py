def exibirInformacaoMenuPricipal():
    # Funcionalidade de Menu de Exibição

    print("=" * 8, "Sistema de Gerencimento de Produtos", "=" * 8)    
    print("1 - Cadastrar Produto")
    print("2 - Consultar Produto")
    print("3 - Atualizar Produto")
    print("4 - Deletar Produto")
    print("5 - SAIR")
    print("==" * 25)


def exibirInformacaoMenuTipoProduto():
    # Menu para exibir os tipos de classificação de produtos
    print("==" * 8,"Tipo do produto", "==" * 8)
    print("1 - Perecivel")
    print("2 - Não perecivel")
    print("3 - Higiene Pessoal")
    print("4 - Produto de limpeza")
    print("==" * 25)

def menuPricipal(entrada):
     
    print("==" * 20)

    if entrada == 1:
        cadastrarProduto()
    elif entrada == 2: 
        consultarProduto()
    elif entrada == 3:
        atualizarProduto()
    elif entrada == 4:
        deletarProduto()

def menuTipoProduto(tipoProduto):
    if tipoProduto == '1':
        classificacao = "Perecivel"
    elif tipoProduto ==  '2':
        classificacao = "Nao perecivel"
    elif tipoProduto == '3':
        classificacao = "Higiene Pessoal"
    elif tipoProduto == '4':
        classificacao = "Produto de Limpeza"
    else:
        classificacao = "Indeterminado"
    return classificacao

def contadorLinhas():
    # retorna valor total do número de linhas existentes no arquivo .txt
    # Contagem de Linhas para determinar a ultima posição das linhas enumerada
    with open(r"src\historico\estoque.txt", "r") as file:
        numeroLinha = file.readlines()
        ultimaLinha = len(numeroLinha)
        ultimaLinha += 1
        return ultimaLinha

# Função que salva as informações fornecidas do produto no estoque
def salvarEstoque(posicaoProduto, nomeProduto, quantidadeProduto, tipoProduto):

 # Salvo/Adiciono as informações fornecidas pelo usuario em um arquivo .txt 
    with open(r"src\historico\estoque.txt", "a") as file:
        file.write(f"{posicaoProduto} - Nome do produto: {nomeProduto} | Quantidade do produto [UN]: {quantidadeProduto} | Tipo do Produto: {tipoProduto}\n")


# Funcionalidade Cadastrar Produtos 
def cadastrarProduto():

    nomeProduto = str(input("Nome do produto: "))
    quantidade  = int(input("Quantidade do produto [UN]: "))
    posicao = contadorLinhas()
    
    exibirInformacaoMenuTipoProduto()
    
    # NOTA: adicionar um Try para n querbrar o codigo
    escolhaUsuarioTipoProduto = str(input("Tipo do produto: ")) 
    # Função que escolher a classificação do produto
    # Variavel para armazenar o valor obitido de menuTipoProduto
    informacaoTipoProduto = menuTipoProduto(escolhaUsuarioTipoProduto)
    # Salvo/Adiciono as informações fornecidas pelo usuario em um arquivo .txt 
    salvarEstoque(posicao, nomeProduto, quantidade, informacaoTipoProduto)
 
# Função consultarProduto, Exibe no Terminal um print do arquivo .txt a qual é armazenado as informações dos produtos       
def consultarProduto():
    with open(r"src\historico\estoque.txt", "rt") as file:
        leituraEstoque = file.read()
        print(leituraEstoque)



def atualizarProduto():
    # Exibe o estoque na tela 
    consultarProduto()
     # Conta o número total de linhas no arquivo
    numeroTotalLinhas = contadorLinhas()

    escolheLinhaAtualizar = int(input("Digite o número da linha para alterar: "))
    
    if escolheLinhaAtualizar <= numeroTotalLinhas:

        linhas = contadorLinhas()
        print(linhas)
        # Verifica se a linha desejada existe
        if escolheLinhaAtualizar <= linhas:
            # Altera a linha desejada
            linhas[escolheLinhaAtualizar - 1] = cadastrarProduto()
            
            # Escreve as alterações de volta no arquivo
            with open(r"src\historico\estoque.txt", "w") as file:
                file.writelines(linhas)
        else:
            print("Erro: Linha não encontrada.")
    else:
        print("Erro: Número da linha inválido.")
    
        
def deletarProduto():
    pass