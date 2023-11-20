#encriptografar

import math
import random
#import numpy as np



def encriptografar(mensagem, e, n):
    mensagem_encriptografada = []
    for letra in mensagem:
        mensagem_encriptografada.append((ord(letra)** e) % n)
    return mensagem_encriptografada



    