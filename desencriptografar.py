# desencriptografar



import os


def desencriptografar():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Inicializa a mensagem desencriptografada
    mensagem_desencriptografada = []

    # Abrir e ler o arquivo com as chaves
    with open('chaves_priv.txt', 'r', encoding='utf-8') as arquivo_chave:
        # Armazena d e n que estao no arquivo
        lines = arquivo_chave.readlines()
        d = int(lines[0])
        n = int(lines[1])

    # Converte a mensagem encriptografada em uma lista de inteiros
    
    
    # Abrir e ler o arquivo com a mensagem encriptografada
    with open('mensagem_encriptografada.txt', 'r', encoding='utf-8') as arquivo:
        mensagem_encriptografada = [int(e) for e in arquivo.read().split('-') if e.isnumeric()]
    # Desencriptografa a mensagem
    for item in mensagem_encriptografada:
        mensagem_desencriptografada.append(chr((item ** d) % n))

    
    # Transforma a lista em string
    mensagem_desencriptografada = ''.join(mensagem_desencriptografada)

    # Escreve a mensagem desencriptografada em um arquivo
    with open('mensagem_desencriptografada.txt', 'w', encoding='utf-8') as arquivo_desencriptografado:
        arquivo_desencriptografado.write(mensagem_desencriptografada)