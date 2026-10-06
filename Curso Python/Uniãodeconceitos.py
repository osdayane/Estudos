# União de Conceitos

# Todas as estruturas podem ser usadas separadamente, mas
# em um programa "real", vamos unindo todas essas estruturas
# para criarmos os cenários que precisamos para resolver um problema

# Exemplhos:

# Você quer saber se uma palavra contém a letra Y 

palavra = "Python"

for letra in palavra:
   if letra == "y":
    print("Essa palavra tem a letra Y!")

Também pode ser usado a variavel "letraprocurada", assim
não é necessário trocar em dois lugares 

letraProcurada = "Y"

for letra in palavra:
   if letra == letraProcurada:
    print("Essa palavra tem a letra Y!")
