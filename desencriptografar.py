#desencriptografar


#desencriptografa a mensagem
#import numpy as np


def desencriptografar(mensagem_encriptografada, d, n):
    mensagem_desencriptografada = []
    for number in mensagem_encriptografada:
        mensagem_desencriptografada.append(chr((number ** d) % n)) 
    mensagem_desencriptografada = ''.join(mensagem_desencriptografada)
    return mensagem_desencriptografada