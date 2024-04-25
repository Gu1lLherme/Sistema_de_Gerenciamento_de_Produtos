# Sistema de Gerencimento de Produtos

"""Sistema de Gerencimento de Produtos que tem como objetivo gerenciar produtos 
de uma mercearia, contendo as funcionalidades de Cadastrar, Consultar, Atualizar e Deletar Produtos
sem atulização de banco de dados (Praticar um CRUD)"""

# Programa Principal
from funcionalidade import funcao, menu


while True:
    
# Menu de Exibição          
    menu.exibirInformacaoMenuPricipal()
    # Variavel para escolha das opções de menu
    entradaUsuario = int(input("Escolha uma das opções acima: "))
    
    if entradaUsuario <= 4:
        funcao.menuPricipal(entrada=entradaUsuario)
    else:
        break
