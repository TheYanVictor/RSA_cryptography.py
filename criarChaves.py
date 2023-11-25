import math
import random

def input_dados():
    print('\n Insira p:')
    p = int(input())
    print('\n Insira q:')
    q = int(input())
    if verifica_primos(p, q) == False:
        print ('\n p e q precisam ser primos')
        input_dados()
    return p, q

# Verifica se p e q são primos
def verifica_primos(p, q):

    # Initial values
    flag_p = True
    flag_q = True
    if p > 1 and q > 1:
        for i in range (2, p):
            if p % i == 0:
                flag_p = False
                break
        for i in range (2, q):
            if q % i == 0:
                flag_q = False
                break
    if flag_p == False or flag_q == False:
        return False
    else:
        return True

# Calcula n 
def calcula_n(p, q):
    return p * q

# Calcula phi de n (totiente de n) => Z = phi
# Quantos numeros são primos relativos a n
def calcula_phi(p, q):
    return (p - 1) * (q - 1)

# Acha valores de D
def acha_valores_d(phi):
    d = 2
    valores_d = []
    while d < phi:
        test = math.gcd(d, phi) == 1
        if test:
            valores_d.append(d)
        d += 1
    print('\n Valores de d: ', valores_d)
    return random.choice(valores_d)

def calcula_e(phi, d):
    e = 1
    while e:
        test = (e * d) % phi == 1
        if test:
            return e
        e += 1

def cria_chaves(p, q):
    n = calcula_n(p, q)
    phi = calcula_phi(p, q)
    d = acha_valores_d(phi)
    e = calcula_e(phi, d)
    
    # Armazena as chaves privadas em um arquivo
    with open('chaves_priv.txt', 'w', encoding='iso-8859-1' ) as arquivo:
        arquivo.write(str(d) + '\n' + str(n))
    # Armazena as chaves publicas em um arquivo
    with open('chaves_pub.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(str(e) + '\n' + str(n))
    return n, d, e