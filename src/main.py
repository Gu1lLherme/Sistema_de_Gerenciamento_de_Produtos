# Sistema de Gerencimento de Produtos

"""Sistema de Gerencimento de Produtos que tem como objetivo gerenciar produtos 
de uma mercearia, contendo as funcionalidades de Cadastrar, Consultar, Atualizar e Deletar Produtos
sem atulização de banco de dados (Praticar um CRUD)"""

# Programa Principal
from funcionalidade import funcao

while True:
    
    # Menu de Exibição 
    funcao.menuPricipal()
    # Variavel para escolha das opções de menu
    entrada = int(input("Escolha uma das opções acima: "))
    print("==" * 20)
    if entrada == 1:
        
        funcao.cadastrarProduto()
        
    if entrada == 2: 
        funcao.consultarProduto()
    if entrada == 3:
        funcao.atualizarProduto()
    if entrada == 4:
        funcao.deletarProduto()
    elif entrada >= 5:
        break