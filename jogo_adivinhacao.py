import random, os

def gerar_palavra_secreta():
    try: 
        arq = open("palavras.txt", "r")
    except FileNotFoundError:
        print("Arquivo palavras.txt não existe, logo não é possível rodar o programa")
        quit()
    palavras = arq.read().split("\n")
    palavras = [palavra.strip() for palavra in palavras]

    index_aleatorio = random.randint(0, len(palavras) - 1)
    palavra_secreta = palavras[index_aleatorio]

    return palavra_secreta

def gerar_total_tentativas(palavra_secreta):
    if len(palavra_secreta) <= 6:
        return  5
    elif len(palavra_secreta) <= 10:
        return 7
    return 10

def gerar_palavra_formatada(palavra_secreta, letras_acertadas):
    palavra_formatada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        elif letra_secreta == ' ':
            palavra_formatada += " "
        else:
            palavra_formatada += '*'
    return palavra_formatada

def gerar_placar(tentativa, total_tentativas):
    if tentativa > total_tentativas:
            return 0
    if tentativa == total_tentativas:
        print("\nUltima tentativa")
    else:
        print(f"\nTentativa {tentativa} de {total_tentativas}")

def gerar_chute(letras_usadas, palavra_formatada):
    chute = input("Digite uma letra: ").lower()
    
    while not chute.isalpha():
        print("Digite apenas letras!\n")
        print(palavra_formatada)
        chute = input("Digite uma letra: ").lower()

    while chute in letras_usadas or len(chute) != 1:
        if chute in letras_usadas:
            print("Você já chutou essa letra!\n")
        else:
            print("Digite apenas uma letra!\n")
        print(palavra_formatada)
        chute = input("Digite uma letra: ").lower()

    return chute

def processar_chute(palavra_secreta, chute, palavra_formatada, letras_acertadas):
    if chute not in palavra_secreta:
        print(palavra_formatada)
        return 1
    letras_acertadas += chute
    return letras_acertadas

def num_jogos_ganhos(jogos_ganhos,vencedor=True):
    if vencedor and jogos_ganhos == 0:
        jogos_ganhos += 1
        print(f"Você ganhou {jogos_ganhos} jogo")
    elif jogos_ganhos == 1:
        print(f"Você ganhou {jogos_ganhos} jogo")
    else:
        print(f"Você ganhou {jogos_ganhos} jogos")
    
def gerar_mensagem_resultado(palavra_secreta, jogos_ganhos, vencedor=True):
    os.system('cls')
    if vencedor:
        print(f"Parabéns você acertou!! A palavra secreta era '{palavra_secreta}'\n")
    else:
        print(f"Infelizmente você gastou todas as suas tentativas. A palavra secreta era {palavra_secreta}\n")
    
    opcao = input("Você gostaria de jogar de novo? [s]im | [n]ão: ")
    if opcao == 's':
        os.system("cls")
        num_jogos_ganhos(jogos_ganhos, vencedor)
        jogos_ganhos += 1
        return 0
    elif opcao == 'n':
        os.system("cls")
        if vencedor:
            num_jogos_ganhos(jogos_ganhos, vencedor)
            print("Obrigado por jogar!")
        else:
            num_jogos_ganhos(jogos_ganhos)
            print("Obrigado por jogar!")
        return 1

jogos_ganhos = 0
while True:
    palavra_secreta = gerar_palavra_secreta()
    letras_usadas = ''
    letras_acertadas = ''
    palavra_formatada = ''
    total_tentativas = gerar_total_tentativas(palavra_secreta)
    tentativa = 1
    vencedor = True

    print("Bem vindo ao jogo de advinhação!")
    print("Tente adivinhar a palavra secreta.")

    while palavra_formatada != palavra_secreta:
        placar = gerar_placar(tentativa, total_tentativas)
        if placar == 0:
            os.system("cls")
            vencedor = False
            break

        chute = gerar_chute(letras_usadas, palavra_formatada)
        if chute == 1:
            continue
        letras_usadas += chute
        
        chute_processado = processar_chute(palavra_secreta, chute, palavra_formatada, letras_acertadas)
        if type(chute_processado) == int:
            tentativa += 1
            continue
        letras_acertadas += chute_processado

        palavra_formatada = gerar_palavra_formatada(palavra_secreta, letras_acertadas)
        print(palavra_formatada)
        
    resultado = gerar_mensagem_resultado(palavra_secreta, jogos_ganhos, vencedor)
    if resultado == 0:
        continue
    else:
        break