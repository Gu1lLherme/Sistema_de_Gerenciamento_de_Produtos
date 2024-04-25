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
     # Função que faz o tratamento da escolha do usuria e realiza a funcionalidade escolhida
    print("==" * 20)

    if entrada == 1:
        cadastrarProduto()
    elif entrada == 2: 
        consultarProduto()
    elif entrada == 3:
        atualizarProduto()
    elif entrada == 4:
        deletarProduto()

def menuTipoProduto():
    # Função que faz o tratamento do Tipo do produto cadastrado 
    """
    Perecivel
    Nao perecivel
    Higiene Pessoal
    Produto de Limpeza
    Indeterminado
    """
    tipoProduto = str(input("Tipo do produto: ")) 

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

def atributosProduto(): 
    # lista para armazenar os atributos fornecidos do produto cadastrado
    atributosProdutoTratatos = list()
    # Atributos:  posicaoProduto, nomeProduto, quantidadeProduto, informacaoTipoProduto
    posicaoProduto = contadorLinhas()
    nomeProduto = str(input("Nome do produto: "))
    quantidadeProduto  = int(input("Quantidade do produto [UN]: "))
    # Exibi o menu de informaçoes sobre os Tipos de Produtos
    exibirInformacaoMenuTipoProduto()
    # Variavel para armazenar o valor obitido de menuTipoProduto
    informacaoTipoProduto = menuTipoProduto()
    # Adiciona ao  final da lista os atributos fornecidos do produto cadastrado
    atributosProdutoTratatos.append(posicaoProduto)
    atributosProdutoTratatos.append(nomeProduto) 
    atributosProdutoTratatos.append(quantidadeProduto)
    atributosProdutoTratatos.append(informacaoTipoProduto)
    
    return atributosProdutoTratatos
    
# Funcionalidade Cadastrar Produtos 

def cadastrarProduto():
    listaAtributos = atributosProduto()
    nomeclaturaProduto = f"{listaAtributos[0]} - Nome do produto: {listaAtributos[1]} | Quantidade do produto [UN]: {listaAtributos[2]} | Tipo do Produto: {listaAtributos[3]}\n"
    # Salvo/Adiciono as informações fornecidas pelo usuario em um arquivo .txt 
    with open(r"src\historico\estoque.txt", "a") as file:
        file.write(nomeclaturaProduto)



def consultarProduto():
    # Função consultarProduto, Exibe no Terminal um print do arquivo .txt a qual é armazenado as informações dos produtos       
    with open(r"src\historico\estoque.txt", "rt") as file:
        leituraEstoque = file.read()
        print(leituraEstoque)


def atualizarProduto():
    # Exibe o estoque na tela (você pode implementar a função consultarProduto() aqui)
    consultarProduto()
    # Conta o número total de linhas no arquivo
    numeroTotalLinhas = contadorLinhas()

    escolheLinhaAtualizar = int(input("Digite o número da linha para alterar: "))

    if escolheLinhaAtualizar <= numeroTotalLinhas:
       
        with open(r"src\historico\estoque.txt", "rt") as file:
            # Gera uma lista contendo todas as linhas do estoque com um indice
            linhas = file.readlines()
        
        # Verifica se a linha desejada existe
        if escolheLinhaAtualizar <= len(linhas):
            # Chama a função atributosProduto() para fazer uma atualização de algum produto existente
            atualizacaoProduto = atributosProduto()
            # Altera a linha desejada 
            nomeclaturaProduto = f"{escolheLinhaAtualizar} - Nome do produto: {atualizacaoProduto[1]} | Quantidade do produto [UN]: {atualizacaoProduto[2]}| Tipo do Produto: {atualizacaoProduto[3]}\n"

            if atualizacaoProduto is not None:
                linhas[escolheLinhaAtualizar - 1] = nomeclaturaProduto

                # Escreve as alterações de volta no arquivo
                with open(r"src\historico\estoque.txt", "w") as novoConteudoAdicionar:
                    novoConteudoAdicionar.writelines(linhas)
                novoConteudoAdicionar.close()
            else:
                print("Erro: Conteúdo inválido.")
        else:
            print("Erro: Linha não encontrada.")
    else:
        print("Erro: Número da linha inválido.")
    
        
def deletarProduto():
    pass