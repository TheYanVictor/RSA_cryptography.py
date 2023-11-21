#main 

import encriptografar as encript
import desencriptografar as descript
import criarChaves as create
import prettytable as pt

from menu import menu


#main function
def main(): 
    
    # Opções de ação
    print('\n')
    menu_choice = menu()

    # Encriptografar
    if menu_choice == 1:
        # Entrada de dados
        p, q = create.input_dados()
        
        # Cria as chaves
        n, d, e = create.cria_chaves(p, q)
    
        # Imprime as chaves em um quadro
        print('\n')
        table = pt.PrettyTable(['Chave pública', 'Chave privada'])
        table._max_width = {'Chave pública': 50, 'Chave privada': 50}
        table.add_row([str(e) + ', ' + str(n), str(d) + ', ' + str(n)])
        print(table)
        
        # Input mensagem
        print('\nInsira mensagem:')
        mensagem = input()
        
        # Encriptografa a mensagem
        mensagem_encriptografada = encript.encriptografar(mensagem, e, n)
        
        # Mostra a mensagem encriptografada
        table_encrip = pt.PrettyTable(['Mensagem original', 'Mensagem encriptografada'])
        table_encrip._max_width = {'Mensagem original': 50, 'Mensagem encriptografada': 50}
        table_encrip.add_row([mensagem, mensagem_encriptografada])
    
    # Desincriptografar
    elif menu_choice== 2:
        # Chama a função desencriptografar
        descript.desencriptografar()
        
        # Abre os arquivos com as mensagens
        with open('mensagem_encriptografada.txt', 'r', encoding='utf-8') as arquivo_encriptografado:
            mensagem_encriptografada_txt = arquivo_encriptografado.readlines()
        with open('mensagem_desencriptografada.txt', 'r', encoding='utf-8') as arquivo_desencriptografado:
            mensagem_desencriptografada_txt = arquivo_desencriptografado.readlines()
        
        # Mostra a mensagem encriptografada e desencriptografada
        table2 = pt.PrettyTable(['Mensagem encriptografada', 'Mensagem desencriptografada'])
        table2._max_width = {'Mensagem encriptografada': 50, 'Mensagem desencriptografada': 50}
        table2.add_row([mensagem_encriptografada_txt, mensagem_desencriptografada_txt])
        print(table2)
        
    # Sair
    elif menu_choice == 3:
        print('Saindo...')
        exit()

main()