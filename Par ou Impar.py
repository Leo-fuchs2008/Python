from sys import exit
from random import randint
jogador = int(input("Digite um valor\n"))
computador = randint(0,11)
total = jogador + computador
if jogador > 10:
  print("Você não pode colocar números maiores do que 10.")
  exit()
print("Você jogou {} e o computador jogou {}. Total de {}".format(jogador,computador,total))

if total % 2 == 0:
 print("PAR!\nVocê ganhou.")
else:
  print("IMPAR!\nVocê perdeu.")
