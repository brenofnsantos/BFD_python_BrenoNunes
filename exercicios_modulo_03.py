#Exercícios de Python para treino

# Conversões de tipos
# Exercício 1 - Converta a string "123" para int e depois para float. Imprima os dois resultados.


str_123 = "123"
str_to_int = int(str_123)
str_to_float = float(str_to_int)

print(str_to_int)
print(str_to_float)


# Operações com Strings
# Exercício 2 - Dada a string "Python é incrível!", faça o seguinte:
# • Conte quantos caracteres ela possui (incluindo espaços)
# • Converta toda a string para maiúsculas
# • Substitua a palavra ”incrível” por ”poderoso”


texto = "Python é incrível!"

num_caracteres = len(texto)
texto_maior = texto.upper()
troca_texto = texto.replace("incrível","poderoso")


print ("Esse é o total de caracteres da frase:", num_caracteres)
print ("Esse é o resultado maiusculo da frase:", texto_maior)
print ("Esse é o resultado da troca de palavras:", troca_texto)


# Listas e Indexação
# Exercício 3 - Dada a lista de numeros = [10, 20, 30, 40, 50], faça:
# • Acesse e imprima o terceiro elemento
# • Adicione o número 60 no final da lista
# • Remova o número 20 da lista

list_num = [10, 20, 30, 40, 50]
list_num.append(60)   #Se quiser adicionar em uma posição específica da lista, utiliza-se .insert(,) no qual dentro dela colocará na primeira parte dentro do parenteses a posição da lista que deseja incluir o novo valor e após a virgula o número que precisa inserir. Por exemplo: list_num..insert(1,60)
print(list_num[2])

list_num.remove(20)  #Utilizando o .remove() é preciso escolher dentro do parenteses o número específico ou itens específicos que deseja remover da lista. 
print(list_num)       

list_num.pop(1)   #É possível utilizar o .pop() para escolher o índice dele, como posição número 1, posição 2 e etc, para remoção.
print(list_num) 


# Dicionários
# Exercício 4 - Crie um dicionário chamado aluno com:
# • "nome": ”Maria”
# • "idade": 22
# • "curso": ”Engenharia”
# Depois:
# • Adicione uma nova chave "notas" com a lista [8.5, 7.0, 9.2]
# • Imprima apenas o valor da chave "curso"


aluno = {
    "nome": "Maria", 
    "idade": "22", 
    "curso": "Engenharia", 
}

aluno["notas"] = [8.5, 7.0, 9.2] #"notas" é a chave adicionada ao dicionário e a lista é o valor atribuído a essa chave.
print(aluno["curso"])


#Tuplas e Conjuntos
# Exercício 5 - Dada a tupla cores = ("vermelho", "verde", "azul", "verde"):
# • Converta-a em um conjunto para remover duplicatas
# • Adicione a cor "amarelo" ao conjunto


cores = ("vermelho", "verde", "azul", "verde")
conver_cores = set(cores) #set serve para converter a tupla em conjunto {}

conver_cores.add("amarelo") #.add serve para adicionar uma informação no conjunto que deseja. 
print(conver_cores)


# Exercício 6 - Operações Matemáticas
# Declare duas variáveis:
# • a = 15 (int)
# • b = 4 (int)
# Calcule e imprima:
# • A divisão inteira de a por b
# • O resto da divisão de a por b


a = 15 
b = 4

div = a // b
resto = a % b
print("Esse é o resultado da divisão:", div)
print("Esse é o resto da divisão:", resto)

# Exercício 7 - Verificação de Tipos
# Dada a lista dados = [42, 3.14, "Python", True, [1, 2]], percorra cada elemento e imprima seu tipo.

lista_dados = [42, 3.14, "Python", True, [1, 2]]
for elemento in lista_dados:
    print(elemento, "pertence ao tipo", type(elemento))


# Exercício 7 - Verificação de Tipos
# Dada a lista dados = [42, 3.14, "Python", True, [1, 2]], percorra cada elemento e imprima seu tipo.


dados = [42, 3.14, "Python", True, [1, 2]]

for i in dados:
  print(type(i))


#Manipulação de Strings
# Exercício 8 - Dada a string "programação":
# • Inverta a string
# • Verifique se a string original é igual a string invertida


palavra = "programação"

palavra_invertida = "".join(reversed(palavra))     # 1. Inverter a string usando fatiamento pode ser feita com palavra_invertida = palavra[::-1]
print(palavra_invertida)

if palavra_invertida == palavra:
    print("True")
else:
    print("False")


# Listas Aninhadas
# Exercício 9  - Dada a lista matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
# • Acesse e imprima o número 5
# • Substitua o número 8 por 10


lista_matriz = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

local_num = lista_matriz[1][1]
print(local_num)

lista_matriz[2][1] = [10]
print(lista_matriz)



# Exercício 10 - Dicionário
# Crie um dicionário estoque com: 
# • "maça": 10
# • "banana": 5
# • "laranja": 8
# Faça o seguinte:
# • Adicione "pera" com quantidade 12
# • Remova "banana"
# • Imprima apenas os nomes dos itens (chaves)


estoque = {
    "maça": 10 , 
    "banana": 5, 
    "laranja": 8
}

estoque["pera"] = 12
del estoque["banana"]
print(estoque)
print(list(estoque.keys()))


# Exercício 11 - Classe
# Suponha que você faz parte de uma equipe de desenvolvimento para softwares de astronomia e irá criar um protótipo expansível de sistema solar, para isso siga as definições:
# A - Crie uma classe Planeta, ela deve ser inicializada com os parâmetros: nome, raio_equatorial, distancia_do_sol e composicao.
# B - O raio_equatorial deve ser em km, a distancia_do_sol em milhões de km e composição "Rochoso" ou "Gasoso".
# C - Adicione um método de apresentação, sem parâmetros, que mostre na tela as informações do planeta.
# D - Fora da classe, crie uma função que calcule e retorne o valor da distância do planeta instanciado até o SOL em UA (Unidades Astronômicas, representada pela distância da terra até o Sol, aproximadamente 150 milhões de km). Utilize a fórmula: distancia_do_sol / 150. Essa função deve receber como parâmetro o atributo distancia_do_sol da classe planeta, ou seja, deve funcionar para qualquer objeto do tipo planeta.
# Pesquisa na internet pelas informações de 3 planetas e as utilize para instanciar 3 objetos. Execute o método de apresentação e a função de distância para cada um dos objetos instanciados.

class Planeta:
    def __init__(self,nome,raio_equatorial:float,distancia_do_sol:float,composicao):
        self.nome = nome
        self.raio_equatorial = raio_equatorial
        self.distancia_do_sol = distancia_do_sol 
        self.composicao = composicao 

    def apresentacao_planeta(self): # Apresentações gerais dos resultados das informações dos planetas.
        return f"Características do Planeta\nNome: {self.nome}\nRaio Equatorial: {self.raio_equatorial} km\nDistância do Sol: {self.distancia_do_sol} milhões de km\nComposição: {self.composicao}"


def distancia_ua(ua): # Calculo para resultado de UA
    distancia = ua / 150
    return f"A distância em Unidades Astronômicas do planeta é de {distancia:.2f}." # Formatação para reduzir as casas decimais do resultado.

planeta1 = Planeta("Terra",6378.0,149.6,"Rochoso") 
planeta2 = Planeta("Mercurio",2439.7,58.0,"Rochoso")
planeta3 = Planeta("Saturno",60268.0,1400.0,"Gasoso")

print(planeta1.apresentacao_planeta())
print(distancia_ua(planeta1.distancia_do_sol))
print("=" *30) #Detalhe visual no print.
print(planeta2.apresentacao_planeta())
print(distancia_ua(planeta2.distancia_do_sol))
print("=" *30)
print(planeta3.apresentacao_planeta())
print(distancia_ua(planeta3.distancia_do_sol))
print("=" *30)
