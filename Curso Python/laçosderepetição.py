# Laços de Repetição (for e While)

# Imagine que você precisa pedir para alguém contar de 1 a 100
# e escrever cada número em um papel. Fazer isso manualmente
# seria muito cansativo e demorado, né?

# Agora, imagine que um programa pode fazer essa contagem automaticamente, 
# sem precisar repetir o mesmo comando 100 vezes. É exatamente isso 
# que os laços de repetição fazem!

# Os laços de repetição são usados para executar um bloco de código
# várias vezes, até que uma condição seja atingida.

# Python tem dois tipos principais de laõs:

# for > Quando sabemos quantas vezes queremos repetir algo.
# while > Quando queremos repetir algo qté que uma condição se torne falso.

# FOR

# O FOR é usado quando sabemos quantas vezes queremos repetir um bloco de código.
# Ele percorre uma sequeência de valores, como uma lista, um intervalo de números
# ou até mesmo letras de uma palavra.

# Estrutura:

# for variável in sequência: 
#     # Código a ser repetido

# Contando de 1 a 5 com o FOR

# for numero in range(1, 6): 
    # print(numero)

    # O range(1,6) gera os números de 1 a 5, o último número do range não é incluído
    # [1, 2, 3, 4, 5]

# Percorrendo uma lsta de compras 

# compras = ["Arroz", "Feijão", "Leite", "Ovos"]

# for item in compras: 
#     print(f" Comprar: {item}")


# # Percorrendo as letras de uma palavra

# palavra = "Python"

# for letra in palavra:
#     print(letra)



# while
# O while é usado quando não sabemos quantas vezes a repetição vai acontecer,
# mas sabemos a condição que deve ser atendida para continuar.

# while condição:
#     # Código a ser repetido enquanto a condição for verdadeira

# obs: Cuidado com loops infinitos!
# Se a condição nunca mudar para False, o código nunca para de rodar.

# Contagem regressiva

# contador = 5

# while contador > 0:
#     print(contador)
#     contador -= 1 # Diminui 1 do contador a cada repetição

# print("Fogo")

# Pedindo senha até acertar

senha_correta = "1234"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")

print("Acesso permitido!")