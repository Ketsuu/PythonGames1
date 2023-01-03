import forca
import adivinhacao

print("******************")
print("*Escolha seu Jogo*")
print("******************")

print ("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo?"))

if(jogo == 1):
    print("Iniciando forca")
    forca.jogar()
elif(jogo == 2):
    print("Iniciando adivinhacao")
    adivinhacao.jogar()