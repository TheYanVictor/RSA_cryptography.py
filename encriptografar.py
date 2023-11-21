#encriptografar

def encriptografar(mensagem, e, n):
    mensagem_encriptografada = []
    for letra in mensagem:
        mensagem_encriptografada.append((ord(letra)** e) % n)
    # Escrever a mensagem encriptografada em um arquivo
    arquivo = open('mensagem_encriptografada.txt', 'w', encoding='utf-8')
    for item in mensagem_encriptografada:
        arquivo.write(str(item) + '-')
    arquivo.close()
    return mensagem_encriptografada