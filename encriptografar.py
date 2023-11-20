#encriptografar

def encriptografar(e, n):
    print('\nInsira mensagem:')
    mensagem = input()
    mensagem_encriptografada = []
    for letra in mensagem:
        mensagem_encriptografada.append((ord(letra)** e) % n)
    # Escrever a mensagem encriptografada em um arquivo
    # Escrever a mensagem encriptografada em um arquivo
    arquivo = open('mensagem_encriptografada.txt', 'w')
    for item in mensagem_encriptografada:
        arquivo.write("%s\n" % item)
    arquivo.close()
    return mensagem_encriptografada



    