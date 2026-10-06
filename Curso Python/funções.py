# # funções 

# # Funções são blocos de código reutilizáveis que realizam
# # uma tarefa esoecífica. Em vez de escrever o mesmo código
# # várias vezes, criamos uma função e apenas a chamamos sempre que necessário.

# # Exemplo "Real"
# # Imagine que você tem que calcular o imposto de vários produtos em uma loja.
# # Em vez de repetir a mesma conta vároas vezes, você pode criar uma função
# # chamada calcular_imposto() e usá-la sempre que precisar.


# def saudacao(nome):
#     print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

# saudacao("Maria")

# Retorno de valores

# def somar(a, b):
#     return a +b

# # Camando a função e armazenando o resultado
# resultado = somar(5, 3)
# print(f"A soma é {resultado}")

# Função com vários parametros

def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

# Chamando a função
resultado = calcular_media(8, 9, 7)
print(f"A média é {resultado:.2f}")

