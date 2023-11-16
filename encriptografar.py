# Encriptografar

import math
import random
import numpy as np


print ('Encriptografar\n ')
print ('\n Insira p:')
p = int(input())
print ('\n Insira q:')
q = int(input())
print ('\n Insira chave pública:')
k = int(input())

# Calcula n
n = p * q
print ('\n n = p * q =', n)

# Calcula phi de n (totiente de n)
phi = (p - 1) * (q - 1)
print ('\n phi = (p - 1) * (q - 1) =', phi)



# Acha todos os valores de D
i = 2
valores_d = []
while (i < phi):
    if math.gcd(i, phi) == 1:
        # armazena todos os valores de i
        valores_d.append(i)
    i = i + 1

# Determina um valor de d aleatório
d = random.choice(valores_d)

print ('\n d =', d)

# Calcula e
#(E * D) mod Z = 1 (Z = phi)
e = 0
valores_e = []
while (e < phi):
    if ((e * d) % phi == 1):
        valores_e.append(e)
    e = e + 1
# Determina um valor de e aleatório
e = random.choice(valores_e)
    
print ('\n e =', e)

# Calcula a chave privada
chave_privada = (n, d)
print ('\n Chave privada:', chave_privada)

# Calcula a chave pública
chave_publica = (n, e)
print ('\n Chave pública:', chave_publica)

# Insere texto a ser encriptografado
print ('\n Insira a mensagem:')
mensagem = input()

# Encriptografar pela tabela ASCII
mensagem_encriptografada = []
for letra in mensagem:
    mensagem_encriptografada.append((ord(letra) ** e )% n)

# Convertendo para string
mensagem_criptografada = []
for letra in mensagem_encriptografada:
    mensagem_criptografada.append(chr(letra))
    
print ('\n Mensagem desencriptografada:', "".join(mensagem_criptografada))

# Desencriptografar
mensagem_desencriptografada = []
for letra in mensagem_encriptografada:
    mensagem_desencriptografada.append(chr((letra ** d) % n))
print ('\n Mensagem desencriptografada:', "".join(mensagem_desencriptografada))


