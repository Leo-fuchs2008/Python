import sys
primeiro = int and float(input("Digite o primeiro número:\n"))#Pede o primeiro número ao usuário
segundo = int and float(input("Digite o segundo número:\n"))#Pede o segndo número ao usuário
terceiro = int and float(input("Digite o terceiro número:\n"))#Pede o terceiro número ao usuário
resultado1 = primeiro+segundo+terceiro#Soma
resultado2 = primeiro-segundo-terceiro#Subtração
resultado3 = primeiro*segundo*terceiro#Multiplicação
resultado4 = primeiro/segundo/terceiro#Divisão
resultado5 = primeiro%segundo#Resto da divisão
print('''Opções válidas:
Somar
Subtrair
Multiplicar
Dividir
Antecessor e Sucessor
Tabuada
Medidas
Quantidade
Fatorial
Resto
Maior ou Menor
Par ou Impar
Binario''')
escolha = input("Digite a sua escolha:\n")

if escolha == 'Somar':
 print(resultado1)
 exit()
elif escolha == 'Subtrair':
  print(resultado2)
  exit()
elif escolha == 'Multiplicar':
  print(resultado3)
  exit()
elif escolha == 'Dividir':
  print(resultado4)
  exit()
if escolha == 'Resto':
  print(resultado5)
  exit()
if escolha == 'Fatorial':
  from math import factorial
  n = int(input("Digite um número para calcular seu fatorial:\n"))
  f = factorial(n)
  print("O fatorial de {} é {}".format(n, f))
  exit()
if escolha == 'Binario':
 Value= numc=(1 or 2 or 3)
 num=int


 num = int(input('Número a ser convertido para  binário:\n'))

 if numc == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))


 elif numc == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)))


 elif numc == 3:
    print(' {} convertido para Hexadecimal é igual a {}'.format(num, hex(num)))


 else:
    print('Opção inválida. Tente novamente')
 exit()
if escolha == 'Antecessor e Sucessor':#Verifica o valor digitado pelo usuário e mostra seu anrtecessor e sucessor
 a = primeiro -1
 s = primeiro +1
 print("Analizando o valor {} , o seu antecessor é {}, e o seu sucessor é {}.".format(primeiro, a , s))
 exit()
if escolha == 'Tabuada':
 num2 = int(input("Digite um número inteiro para ver a sua tabuada:\n"))
 print("{} X {:2} = {:2}".format(num2, 1,num2*1))
 print("{} X {:2} = {:2}".format(num2, 2,num2*2))
 print("{} X {:2} = {:2}".format(num2, 3,num2*3))
 print("{} X {:2} = {:2}".format(num2, 4,num2*4))
 print("{} X {:2} = {:2}".format(num2, 5,num2*5))
 print("{} X {:2} = {:2}".format(num2, 6,num2*6))
 print("{} X {:2} = {:2}".format(num2, 7,num2*7))
 print("{} X {:2} = {:2}".format(num2, 8,num2*8))
 print("{} X {:2} = {:2}".format(num2, 9,num2*9))
 print("{} X {:2} = {:2}".format(num2, 10,num2*10))
if escolha == 'Quantidade':
   medida = int and float(input("Coloque o volume:\n"))
   resultado =  medida / 1000
   resultado =  medida / 100
   resultado = medida /10
   resultado =   medida * 1
   resultado =  medida *10
   resultado =  medida * 100
   resultado =  medida * 1000
   print('''Suas opções:
 [0]l
 [1]h
 [2]dam  
 [3]m
 [4]dm
 [5]cm
 [6]mm''')
   escolha3 = float(input("Sua escolha:\n"))
   if escolha3 == 0:
    print("Ok, então eu vou converter de {} para qual medida? ".format(escolha3))

   elif escolha3 == 1:
    print("Ok, então eu vou converter de {} para qual medida? ".format(escolha3))

   elif escolha3 == 2:
    print("Ok, então eu vou converter de {} para qual medida? ".format(escolha3))

   elif escolha3 == 3:
     print("Ok, então eu vou converter de {} para qual medida? ".format(escolha3))

   elif escolha3 == 4:
     print("Ok, então eu vou converter de {} para qual medida? ".format(escolha3))

   elif escolha3 == 5: 
     print("Ok, então eu vou converter de {} para qual medida? ".format(escolha3))
   elif escolha3 == 6:
     print("Ok, então eu vou converter de {} para qual medida? ".format(escolha3))

   opcao2 = {0,1,2,3,4,5,6}



   opcao2 == 0 == resultado
   opcao2 == 1 == resultado
   opcao2 == 2 == resultado
   opcao2 == 3 == resultado
   opcao2 == 4 == resultado
   opcao2 == 5 == resultado
   opcao2 == 6 == resultado

   print('''Suas opções:
 [0]l
 [1]hm
 [2]dam
 [3]ml
 [4]dm
 [5]cm
 [6]mm''')
   escolha4 = int and float(input("Para qual medida você deseja converter?\n"))
   if escolha4 == 0:
    print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

   elif escolha4 == 1:
      print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

   elif escolha4 == 2:
     print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

   elif escolha4 == 3:
      print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

   elif escolha4 == 4:
     print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

   elif escolha4 == 5: 
     print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))
   elif escolha4 == 6:
     print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

   else:
     print("Opção invalida. Tente novamente")
  
if escolha == 'Medidas':
 medida = float(input("Coloque uma distância:\n"))
 resultado =  medida / 1000
 resultado =  medida / 100
 resultado = medida /10
 resultado =   medida * 1
 resultado =  medida *10
 resultado =  medida * 100
 resultado =  medida * 1000
 print('''Suas opções:
 [0]l
 [1]hl
 [2]dam  
 [3]ml
 [4]dl
 [5]cl
 [6]ml''')
 escolha1 = int(input("Sua escolha:\n"))
 if escolha1 == 0:
   print("Ok, então eu vou converter de {} para qual medida? ".format(escolha))

 elif escolha1 == 1:
   print("Ok, então eu vou converter de {} para qual medida? ".format(escolha))

 elif escolha1 == 2:
   print("Ok, então eu vou converter de {} para qual medida? ".format(escolha))

 elif escolha1 == 3:
    print("Ok, então eu vou converter de {} para qual medida? ".format(escolha))

 elif escolha1 == 4:
   print("Ok, então eu vou converter de {} para qual medida? ".format(escolha))

 elif escolha1 == 5: 
   print("Ok, então eu vou converter de {} para qual medida? ".format(escolha))
 elif escolha1 == 6:
   print("Ok, então eu vou converter de {} para qual medida? ".format(escolha))

 opcao2 = {0,1,2,3,4,5,6}



 opcao2 == 0 == resultado
 opcao2 == 1 == resultado
 opcao2 == 2 == resultado
 opcao2 == 3 == resultado
 opcao2 == 4 == resultado
 opcao2 == 5 == resultado
 opcao2 == 6 == resultado

 print('''Suas opções:
 [0]km
 [1]hm
 [2]dam
 [3]m
 [4]dm
 [5]cm
 [6]mm''')
 opcao2 = int(input("Para qual medida você deseja converter?\n"))
 if escolha1 == 0:
  print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

 elif escolha1 == 1:
  print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

 elif escolha1 == 2:
  print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

 elif escolha1 == 3:
  print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

 elif escolha1 == 4:
  print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

 elif escolha1 == 5: 
  print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))
 elif escolha1 == 6:
  print("{} convertido para {} é igual a {}".format(medida,escolha,resultado))

 else:
  print("Opção invalida. Tente novamente")
 exit()

if escolha == 'Par ou Impar':#Verifica se os números digitados pelo usuário são par ou ímpar
  if primeiro % 2 == 0:
    print("O número {} é PAR.".format(primeiro))
  else:
      print("O número {} é IMPAR.".format(primeiro))
  if segundo % 2== 0:
    print("O número {} é PAR.".format(segundo))
  else:
    print("O número {} é IMPAR.".format(segundo))
  if terceiro % 2 == 0:
    print("O número {} é PAR.".format(terceiro))
  else:
    print("O número {} é IMPAR.".format(terceiro))
if escolha == 'Maior ou Menor':#Verifica se os números digitados pelo usuário são maiores, menores ou iguais
 if primeiro == segundo and primeiro == terceiro:
  iguais = primeiro
 if segundo == primeiro and segundo == terceiro:
  iguais = segundo
 if terceiro == primeiro and terceiro == segundo:
  iguais = terceiro
 if primeiro <= segundo and primeiro <= terceiro:
  menor = primeiro
 if segundo <= primeiro and segundo <= terceiro:
  menor = segundo
 if terceiro <= primeiro and terceiro <= segundo:
    menor = terceiro
 if primeiro >= segundo and primeiro >= terceiro:
    maior = terceiro
 if segundo >= primeiro and segundo >= terceiro:
  maior = segundo
 if terceiro >= primeiro and terceiro >= segundo:
  maior = terceiro
 
 if primeiro != segundo and primeiro != terceiro:
  iguais = None
 if segundo != primeiro and segundo != terceiro:
  iguais = None
 if terceiro != primeiro and terceiro != segundo:
  iguais = None
 print("O menor valor digitado foi {}\nO maior valor digitado foi {}\nE os valores digitados igualmente são {}.".format(menor,maior,iguais))
 exit()
