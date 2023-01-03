import random

def jogar():
    print("************************************")
    print("*Bem vindo ao jogo de Adivinhação!!*")
    print("************************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 1
    tentativa_atual = 1
    acertou = False
    print(numero_secreto)
    print("(1) Facil (2) Médio (3) Difícil")
    nivel = int(input(""))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    while (tentativa_atual <= total_tentativas and not acertou):

        print("Tentativa {} de {}".format(tentativa_atual, total_tentativas))
        chute_str = input("Insira um numero de 1 a 100 ")
        chute = int(chute_str)
        tentativa_atual = tentativa_atual + 1

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (chute < 1 or chute > 100):
            print("DIGITE SOMENTE DE 1 A 100")
            tentativa_atual = tentativa_atual - 1
            continue

        if (acertou):
            print("Parabens voce acertou!")
            acertou = True
        else:
            if (maior):
                print("Voce errou! O seu numero foi MAIOR que o numero secreto")
            elif (menor):
                print("Voce errou! O seu numero foi MENOR que o numero secreto")


    print("*************")
    print("*Fim do jogo*")
    print("*************")
if(__name__ == "__main__"):
    jogar()