#main 

import encriptografar as encript
import desencriptografar as descript
import criarChaves as create
import prettytable as pt


#main function
def main(): 
    
    #entrada de dados
    p, q = create.input_dados()
        
    # Cria as chaves
    n, e, d = create.cria_chaves(p, q)
    
    # Imprime as chaves em um quadro
    print('\n')
    table = pt.PrettyTable(['Chave pública', 'Chave privada'])
    table._max_width = {'Chave pública': 50, 'Chave privada': 50}
    table.add_row([str(e) + ', ' + str(n), str(d) + ', ' + str(n)])
    print(table)    
    
    # Encriptografa a mensagem
    mensagem_encriptografada = encript.encriptografar(e, n)
    
    # Desencriptografa a mensagem
    mensagem_desencriptografada = descript.desencriptografar(mensagem_encriptografada, d, n)

    # Mostra a mensagem encriptografada
    print('\n')
    table2 = pt.PrettyTable(['Mensagem encriptografada', 'Mensagem desencriptografada'])
    table2._max_width = {'Mensagem encriptografada': 50, 'Mensagem desencriptografada': 50}
    table2.add_row([mensagem_encriptografada, mensagem_desencriptografada])  
    print(table2)
    
main()