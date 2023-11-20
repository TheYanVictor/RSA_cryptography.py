import math
import random

def input_dados():
    print('\n Insira p:')
    p = int(input())
    print('\n Insira q:')
    q = int(input())
    print('\n Insira mensagem:')
    mensagem = input()
    return p, q, mensagem

# Verifica se p e q são primos
def verifica_primos(p, q):
    
    return math.gcd(p, q) == 1

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