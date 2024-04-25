from funcionalidade import menu

def menuPricipal(entrada):
     # Função que faz o tratamento da escolha do usuria e realiza a funcionalidade escolhida
    print("==" * 20)

    if entrada == 1:
        cadastrarProduto()
    elif entrada == 2: 
        consultarProdutoCadastrado()
    elif entrada == 3:
        atualizarProdutoEstoque()
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
   
    # Atributos: nomeProduto, quantidadeProduto, informacaoTipoProduto
    nomeProduto = str(input("Nome do produto: "))
    quantidadeProduto  = int(input("Quantidade do produto [UN]: "))
    posicao = contadorLinhas()
   
    # Exibi o menu de informaçoes sobre os Tipos de Produtos
    menu.exibirInformacaoMenuTipoProduto()
   
    # Variavel para armazenar o valor obitido de menuTipoProduto
    informacaoTipoProduto = menuTipoProduto()
   
    # Adiciona ao  final da lista os atributos fornecidos do produto cadastrado
    atributosProdutoTratatos.append(posicao)
    atributosProdutoTratatos.append(nomeProduto) 
    atributosProdutoTratatos.append(quantidadeProduto)
    atributosProdutoTratatos.append(informacaoTipoProduto)
    
    return atributosProdutoTratatos
    
# Funcionalidade Cadastrar Produtos 
def cadastrarProduto():
    try:
        atualizacaoProduto = atributosProduto()
        textoForamatadoEstoque = f"{atualizacaoProduto[0]} - Nome do produto: {atualizacaoProduto[1]} | Quantidade do produto [UN]: {atualizacaoProduto[2]} | Tipo do Produ{atualizacaoProduto[3]}\n"
        textoFormatadoCadastro = f"Nome do produto: {atualizacaoProduto[1]} | Quantidade do produto [UN]: {atualizacaoProduto[2]} | Tipo do Produto: {atualizacaoProduto[3]}\n"
        # Salvo/Adiciono as informações fornecidas pelo usuario no estoque.txt 
        with open(r"src\historico\estoque.txt", "a") as file:
            file.write(textoForamatadoEstoque)

        # Salvo/Adiciono as informações fornecidas pelo usuario no arquivo exibirProdutos.txt 
        with open(r"src\historico\exibirProduto.txt", "a") as file:
            file.write(textoFormatadoCadastro)
    except:
        print("Nenhum produto cadastrado")

# Funcionalidade Consultar Produto Cadastrado
def consultarProdutoCadastrado():
    # Função consultarProduto, Exibe no Terminal um print do arquivo .txt a qual é armazenado as informações dos produtos       
    with open(r"src\historico\exibirProduto.txt", "rt") as file:
        leituraProdutoCadastrado = file.read()
        print(leituraProdutoCadastrado)
       

# Funcionalidade Exibir Estoque de Produtos Cadastrados
def consultarEstoqueProduto():
    with open(r"src\historico\estoque.txt", "rt") as file:
            leituraEstoque = file.read()
            print(leituraEstoque)

def atualizarProdutoEstoque():
    # Exibe o estoque na tela (você pode implementar a função consultarProduto() aqui)
    consultarEstoqueProduto()
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

                # Escreve as alterações de volta no arquivo estoque.txt  
                with open(r"src\historico\estoque.txt", "w") as novoConteudoAdicionar:
                    novoConteudoAdicionar.writelines(linhas)
                novoConteudoAdicionar.close()
                

            else:
                print("Erro: Conteúdo inválido.")
        else:
            print("Erro: Linha não encontrada.")
    else:
        print("Erro: Número da linha inválido.")


"""def atualizarProduto():
# Funcionalidade Atualizar Produtos 
    # Exibe o estoque na tela (você pode implementar a função consultarProduto() aqui)
    consultarEstoqueProduto()
    # Conta o número total de linhas no arquivo
    numeroTotalLinhas = contadorLinhas()

    escolheLinhaAtualizar = int(input("Digite o número da linha para alterar: "))

    if escolheLinhaAtualizar <= numeroTotalLinhas:
       
        with open(r"src\historico\exibirProduto.txt", "rt") as file:
            # Gera uma lista contendo todas as linhas do estoque com um indice
            linhas = file.readlines()
        
        # Verifica se a linha desejada existe
        if escolheLinhaAtualizar <= len(linhas):
            # Chama a função atributosProduto() para fazer uma atualização de algum produto existente
            atualizacaoProduto = atributosProduto()
            # Altera a linha desejada 
            
            # Salva a Atualização no arquivo exibirProduto.txt 
            textoFormatadoConsultaProduto = f"Nome do produto: {atualizacaoProduto[1]} | Quantidade do produto [UN]: {atualizacaoProduto[2]} | Tipo do Produto: {atualizacaoProduto[3]}\n"  

            if atualizacaoProduto is not None:
                # Grava as atualizações no exibirProduto.txt                 
                linhas[escolheLinhaAtualizar - 1] = textoFormatadoConsultaProduto
                with open(r"src\historico\exibirProduto.txt", "w") as file:
                    file.write(textoFormatadoConsultaProduto)
                file.close()
                # Grava as atualizações no exibirProduto.txt 

            else:
                print("Erro: Conteúdo inválido.")
        else:
            print("Erro: Linha não encontrada.")
    else:
        print("Erro: Número da linha inválido.")"""

# Fucionalidade Deletar Produto
def deletarProduto():
    consultarEstoqueProduto()
    numeroLinhaTotal = contadorLinhas()
    try:
        escolheLinhaDeletar = int(input("Digite o valor da linha que deseja deletar: "))
        
        if escolheLinhaDeletar <= numeroLinhaTotal:
            posiçãoDeletar = escolheLinhaDeletar - 1

            with open(r"src\historico\estoque.txt", "rt") as file:
                listaLinhas = file.readlines()
                print(f"Linha {listaLinhas[posiçãoDeletar]} excluida")
                remover = listaLinhas.pop(posiçãoDeletar)
            file.close()
           
                
            # reescreve a lista sem o item deletado
            with open(r"src\historico\estoque.txt", "w") as arquivo:
                print(arquivo.writelines(listaLinhas))


    except ValueError:
        print("Erro: Digite um número de linhas validos")
   