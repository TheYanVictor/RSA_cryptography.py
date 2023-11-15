# Encriptografar

import math

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



# Calcula D
i = 2
valores_d = []
while (i < phi):
    if math.gcd(i, phi) == 1:
        # armazena todos os valores de i
        valores_d.append(i)
    i = i + 1

# imprimir todos os valores de d
print ('\n Valores de d:')
for i in valores_d:
    print (i)
