# Variáveis e tipos de dados "básicos"

# Uma variável é um espaço na memória onde armazena um valor.

# <nome da var> = <valor>

nome = "Dayane" # variável do tipo string (texto), sempre entre aspas ("" OU '')
idade = 32 # variável do tipo interiro (núm sem casas decimais)
altura = 1.68 # variável do tipo float (núm com casas decimais)
dev = True # variável do tipo boleana, valores lógicos (True/false)

# print (f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")

nome = input("Digite seu nome: ") # Entrada de texto
idade = int(input("Digite sua idade: ")) #Entrada de texto convertida para int
altura = float(input("Digite sua altura: ")) #Entrada convertida para float

#print(f"Olá, {nome}! Você tem {idade} anos e mede {altura}m.")

# Modelo interativo, onde aparece o valor para o usuário

nome = input("Digite seu nome: ") # Entrada de texto
print(f"Valor da var nome: {nome}")
idade = int(input("Digite sua idade: ")) #Entrada de texto convertida para inteiro
print(f"Valor da var idade: {idade}")
altura = float(input("Digite sua altura: ")) #Entrada convertida para float
print(f"Valor da var altura: {altura}")