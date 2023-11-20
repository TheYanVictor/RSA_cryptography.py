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

# Primes verification
def verifica_primos(p, q):
    """
    Verifies if two numbers p and q are prime.

    Parameters:
    p (int): The first number to be checked.
    q (int): The second number to be checked.

    Returns:
    bool: True if both p and q are prime, False otherwise.
    """
    # Initial values
    flag_p = True
    flag_q = True
    if p > 1 and q > 1:
        for i in range (2, p):
            if p % i == 0:
                flag_p = False
        for i in range (2, q):
            if q % i == 0:
                flag_q = False
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
    d = 0
    valores_d = []
    while d < phi:
        test = math.gcd(d, phi) == 1
        if test:
            valores_d.append(d)
        d += 1
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
    return n, d, e