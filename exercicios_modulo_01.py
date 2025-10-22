# Exercícios de fixação do modulo 01:

# 1- Crie um programa que exiba a mensagem "Olá, Mundo!" na tela.

"""print("Olá, Mundo!")"""

# 2- Crie uma variável para armazenar seu nome e em seguida exiba uma mensagem de boas-vindas que inclua seu nome.

"""nome = "Breno."
msg = "Seja bem vindo!"

print(nome, msg)"""


# 3- Crie duas variáveis com números inteiros e exiba a soma delas.

"""n1 = 2
n2 = 4

soma = n1 + n2

print(soma)"""

# 4- Peça ao usuário para digitar seu nome e em seguida exiba uma mensagem de boas-vindas com o nome fornecido.

"""nome_user = input("Digite o seu nome:")
msg_bemvindo = "Seja bem vindo!"

print(nome_user, msg_bemvindo)"""

# 5- Peça ao usuário para digitar o ano em que nasceu, calcule e exiba sua idade aproximada.

"""ano_user = int(input("Digite o ano em que nasceu:"))
ano_atual = 2025

idade_user = ano_atual - ano_user

print("Sua idade atual é:", idade_user)"""

# 6- Peça ao usuário para inserir duas notas, calcule a média e exiba o resultado.

"""av1 = float(input("Digite aqui a nota da primeira avaliação:"))
av2 = float(input("Digite aqui a nota da segunda avaliação:"))

total_avs = av1 + av2
result_avs = total_avs / 2

print("Sua nota final foi:", result_avs)"""

# 7- Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais).

"""idade_user = int(input("Insira sua idade:"))
if idade_user >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade!")"""


# 8- Peça um número e verifique se ele é positivo, negativo ou zero.

"""num_request = float(input("Digite um número aqui:"))
if num_request > 0:
    print("Esse número é positivo!")
elif num_request == 0:
    print("Esse número é zero!")
else:
    print("Esse número é negativo!")"""


# 9- Peça um número e informe se ele é par ou ímpar.

"""num_teste = int(input("Insira aqui um número:"))
resto_verif = num_teste % 2


if resto_verif == 0:
    print("Esse número é par!")
else:
    print("Esse número é ímpar!")"""


# 10- Crie uma senha (ex: "1234") e peça para o usuário digitá-la. Informe se a senha está correta ou incorreta.

"""ins_senha = int(input("Digite aqui sua senha:"))
senha = 1234

if ins_senha != senha:
    print("Sua senha está incorreta!")
else:
    print("Sua senha está correta!")"""

# 11- Peça o valor de uma compra e, se for maior que R$ 100,00, aplique um desconto de 10%. Exiba o valor final.

"""valor_original = float(input("Insira o valor da peça:"))
valor = 100
desconto = 0.10

if valor_original > valor:
    descont_app = desconto * valor_original
    valor_final = valor_original - descont_app
    print("O valor do produto com desconto é de:", valor_final)
else:
    print("O valor do produto é de:", valor_original)"""

# 12- Peça uma letra ao usuário e verifique se é uma vogal ou uma consoante.

"""vogal_user = input("Insira uma letra:")
vogais = ["a","e","i","o","u"]

if vogal_user in vogais:
    print("Essa letra é uma vogal!")
else:
    print("Essa letra é uma consoante!")"""


# 13- Peça dois números e informe qual deles é o maior, ou se são iguais.

"""num1_user = float(input("Insira um número:"))
num2_user = float(input("Insira outro número:"))

if num1_user > num2_user:
    print("O seu número maior é:",num1_user)
elif num1_user == num2_user:
    print("Ambos os números são iguais!")
else:
    print("O seu número maior é:", num2_user)"""


# 14- Crie um programa que exiba os números de 1 a 10.

"""for i in range (11):
    print(i)"""


# 15- Peça um número ao usuário e exiba a tabuada de multiplicação desse número, de 1 a 10.

"""n_user = int(input("Insira um número aqui:"))
for multiplicação in range(1,11):
    print(multiplicação * n_user)"""


# 16- Peça números ao usuário até que ele digite 0. Ao final, exiba a soma de todos os números digitados.

"""gatilho_while = 0 #Crio a variável que vai disparar o while (looping) para que seja possível o usuário ir tentando adicionar os números até que atinga algo que irei declarar dentro dele depois. 
acumulador = [] #Como a pessoa vai ficar tentando digitar números até atingir a variável que eu preciso, no caso o nº zero, eu crio uma lista para acumular esses dados/números que ele for informando. 

while gatilho_while == 0:
    num = int(input("Digite aqui um número:"))
    if num != 0: #Declarando que enquanto o num digitado for diferente de zero, ele irá continuar retornando. 
        acumulador.append (num) #O uso do .append é uma forma de adicionar a lista acumulador aquele número digitado dentro do while e testado pelo if. 
    else:
        gatilho_while = 1  #O else aqui serve para fechar o looping, encerrando ele. Pois transformará o gatilho inicial em um dado diferente de 0 e isso fara com que o while == 0 dê FALSE e encerre o ciclo.

print(sum(acumulador)) #O uso do SUM serve para somar os dados na lista acumulador que foi declarada antes do looping para ser possível armazenar os dados."""

#Também daria para fazer da seguinte forma: 

"""
gatilho_while = 0
acumulador = 0  #Declarando zero aqui, esse dado não vai influenciar na soma posterior do acumular += num e servirá para que no print final ele apresente apenas a soma de tudo que foi acumulado.

while gatilho_while == 0:
    num = int(input("Digite aqui um número:"))
    if num != 0: 
        acumulador += num 
    else:
        gatilho_while = 1  

print(acumulador) """



# 17- Crie um programa que peça uma senha ao usuário. Enquanto a senha não for "1234", continue pedindo.

"""user_codigo = int(input("Insira sua senha:"))

while (user_codigo != 1234):
    print("Senha incorreta!")
    user_codigo = int(input("Insira sua senha:"))

else:
    print("Você acertou, seja bem vindo!")"""

# 18- Crie um programa que faça uma contagem regressiva de 10 até 0.

"""lista_10 = [1,2,3,4,5,6,7,8,9,10]

lista_10.sort(reverse = True)  #Utilizando o .sort ele vai organizar de forma crescente a lista. O reverse = True vai inverter essa organização crescente. 
print(lista_10)

lista_10.reverse() #Ele vai inverter a lista, porém mantendo os valores em suas posições conforme está na listagem de forma invertida.
print(lista_10)

for i in range(11):
    listagem = 10
    listagem -= i  #Ou listagem = listagem - i
    print(listagem)"""



# 19- Crie um número secreto e peça ao usuário para adivinhar. Dê dicas se o palpite foi maior ou menor, até ele acertar.


"""
chave_secreta = 10
control = 0 

while control == 0:
    senha = int(input("Digite seu número secreto:"))
    if senha < 10:
        print("O número precisa ser maior! Tente novamente:")
    elif senha > 10:
        print("O número precisa ser menor! Tente novamente:")
    else:
        print("Parabéns você acertou!")
        control = 1
        """



# 20- Crie um programa que itere de 1 a 20 e exiba apenas os números pares.


"""for iteracao in range(2, 21, 2):
    print(iteracao)"""

"""lista_exemplo = [] #Também pode ser feito, se quiser criar uma lista com os números pares.

for iteracao in range(2, 21, 2):
    lista_exemplo.append(iteracao)

print(lista_exemplo)"""

# 21- Peça um número e calcule o seu fatorial (ex: 5! = 5 * 4 * 3 * 2 * 1).

"""pedir_num = int(input("Informe um número:"))
multiplicacao = 1

for fatorial in range(1, pedir_num + 1):
    multiplicacao = multiplicacao * fatorial

print("Total do calculo fatorial:", multiplicacao)"""

# 22- Crie uma lista com 5 nomes de frutas e exiba cada fruta da lista.

"""frutas = ["Laranja","Pêra", "Uva", "Banana"]

for lista_de_frutas in frutas:
    print(lista_de_frutas)"""

# 23- Crie uma lista vazia e peça ao usuário para inserir 5 itens de uma lista de compras. Ao final, exiba a lista completa.

"""lista_vazia = []
total_itens = 5

for lista_de_compras in range(total_itens):
    itens_do_usuario = input("Insira um produto na lista:")
    lista_vazia.append (itens_do_usuario)

print(f"Lista de compras do usuário: {lista_vazia}")"""


# 24- Dada uma lista de notas [7, 8, 5, 9, 6], calcule a média e exiba o resultado.

"""lista_de_notas = [7, 8, 5, 9, 6]
calc_media = sum(lista_de_notas) / len(lista_de_notas)
print("A média de notas foi de:", calc_media)"""

# 25- Dada uma lista de números [10, 23, 4, 7, 15], encontre e exiba o maior e o menor número.

"""lista_de_numeros = [10, 23, 4, 7, 15]

print(max(lista_de_numeros))
print(min(lista_de_numeros))"""


"""#Ou pode ser feito da forma de:
 lista_de_numeros.sort() #.sort para organizar a lista em ordem crescente.
print(lista_de_numeros[0])
print(lista_de_numeros[-1])"""

# 26- Crie uma lista de nomes e peça um nome ao usuário. Verifique se o nome está na lista e exiba uma mensagem correspondente.

"""lista_nomes = ["Leandro","Paulo","João","Guilherme"]
user_nome = input("Verifique se o nome está na lista:")

if user_nome in lista_nomes:
    print("Seu nome está na lista, parabéns!")
else:
    print("Seu nome não está na lista.")"""
    
# 27- Crie uma função que exiba a mensagem "Bem-vindo ao programa!" e em seguida chame essa função.

"""def boas_vindas ():
    print("Bem-vindo ao programa!")

boas_vindas()"""


# 28- Crie uma função que receba um nome como parâmetro e exiba uma saudação personalizada.


"""def nome_parametro (saudacao):
    print("Olá,", saudacao)

nome_usuario = input("Digite o seu nome:")

nome_parametro(nome_usuario)"""



# 29- Crie uma função que receba dois números como parâmetros e retorne a soma deles.

"""def dois_num(n1,n2):
    print(n1 + n2)


pedido1 = int(input("Insira o primeiro número:"))
pedido2 = int(input("Insira o segundo número:"))

dois_num(pedido1, pedido2)"""

# 30- Crie uma função que receba uma lista de números como parâmetro e retorne a média dos valores.


"""def lista_parametro (med_lista):
    total_med = sum(med_lista) / len(med_lista)
    print("Média dos valores:",total_med)

num_listagem = [5,2,4,3]

lista_parametro(num_listagem)"""