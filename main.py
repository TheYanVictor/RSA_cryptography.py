#main 

import encriptografar as encript
import desencriptografar as descript


#main function
def main():
    
    
    #entrada de dados
    p, q, mensagem = encript.input_dados()
    
    #confere se p e q são primos
    if (encript.verifica_primos(p, q) == False):
        print ('\n p e q precisam ser primos')
        p, q, k, mensagem = encript.input_dados()
        
    # Cria as chaves
    n, e, d = encript.cria_chaves(p, q)
    
    # mostra as chaves
    print ('\n Chave pública: ' + str(e) + ', ' + str(n))
    print ('\n Chave privada: ' + str(d) + ', ' + str(n))
    
    
    # ecnriptografa a mensagem
    mensagem_encriptografada = encript.encriptografar(mensagem, e, n)

    # mostra a mensagem encriptografada
    print ('\n Mensagem encriptografada: ')
    print (mensagem_encriptografada)

    print ('\n ------------------------------------ \n')
    print ('\n Mensagem desencriptografada: ')
    print (descript.desencriptografar(mensagem_encriptografada, d, n))

main()