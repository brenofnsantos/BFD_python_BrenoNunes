# 1 - Construa uma classe para armazenar informações de carros, cada objeto instanciado por essa classe deve ter os seguintes atributos:
# A - Modelo, marca, ano de lançamento, potência (1.0,1.6,etc), tipo de câmbio (manual ou automático), preço no lançamento.
# B - Crie um método para retornar cada atributo.
# Crie ao menos 3 instâncias de objeto, e execute todos os métodos para teste.


class Info_carros:
    def __init__(self,modelo,marca,ano_de_lancamento,potencia,cambio,preco):
        self.modelo = modelo
        self.marca = marca
        self.ano_de_lancamento = ano_de_lancamento
        self.potencia = potencia
        self.cambio = cambio
        self.preco = preco

    def retorne_modelo(self):
        return self.modelo
    
    def retorne_marca(self):
        return self.marca
    
    def retorne_ano_lancamento(self):
        return self.ano_de_lancamento
    
    def retorne_potencia(self):
        return self.potencia
    
    def retorne_cambio(self):
        return self.cambio
    
    def retorne_preco(self):
        return self.preco

    def informacoes_veiculo(self):
        return f"Modelo:{self.modelo}.\nMarca:{self.marca}.\nAno de Lançamento:{self.ano_de_lancamento}.\nPotência:{self.potencia}.\nTipo de Câmbio:{self.cambio}.\nPreço de Lançamento:R${self.preco}."

carro1 = Info_carros(modelo = "Uno Mille EX Smart 4p", marca = "Fiat",ano_de_lancamento = 2001,potencia = "1.0",cambio = "Manual",preco = "13.064,00")
carro2 = Info_carros(modelo = "Fiesta Titanium 1.6 16V Flex Mec",marca = "Ford",ano_de_lancamento = 2017,potencia = "1.6",cambio = "Manual",preco = "55.914,00")
carro3 = Info_carros(modelo = "Civic Sedan EX 2.0 Flex 16V Aut.4p", marca = "Honda",ano_de_lancamento = 2021,potencia = "2.0",cambio = "Automático",preco = "124.283,00")
carro4 = Info_carros(modelo = "Etios XS 1.5 Flex 16V 5p Auto", marca = "Toyota",ano_de_lancamento = 2018,potencia = "1.5",cambio = "Automático",preco = "60.978,00")


print("Dados do veículo 1:")
print(carro1.retorne_modelo())
print(carro1.retorne_marca())
print(carro1.retorne_ano_lancamento())
print(carro1.retorne_potencia())
print(carro1.retorne_cambio())
print(carro1.retorne_preco())
print("=" *30) #Detalhe visual no print.

print("Dados do veículo 2:")
print(carro2.retorne_modelo())
print(carro2.retorne_marca())
print(carro2.retorne_ano_lancamento())
print(carro2.retorne_potencia())
print(carro2.retorne_cambio())
print(carro2.retorne_preco())
print("=" *30)

print("Dados do veículo 3:")
print(carro3.retorne_modelo())
print(carro3.retorne_marca())
print(carro3.retorne_ano_lancamento())
print(carro3.retorne_potencia())
print(carro3.retorne_cambio())
print(carro3.retorne_preco())
print("=" *30)

print("Dados do veículo 4:")
print(carro4.retorne_modelo())
print(carro4.retorne_marca())
print(carro4.retorne_ano_lancamento())
print(carro4.retorne_potencia())
print(carro4.retorne_cambio())
print(carro4.retorne_preco())
print("=" *30)

print("Informações gerais dos veículos:")
print(carro1.informacoes_veiculo())
print("." *30)
print(carro2.informacoes_veiculo())
print("." *30)
print(carro3.informacoes_veiculo())
print("." *30)
print(carro4.informacoes_veiculo())
print("=" *30)



# 2 - Suponha que estamos desenvolvendo um sistema para um banco. Este sistema deve obedecer as seguintes restrições:
# A - Uma classe pai chamada Cliente, com os atributos: nome, cpf, endereço.
# B - Uma classe filha chamada Conta_Corrente que deve herdar os atributos da classe pai mais o atributo "saldo". Este atributo deve ser privado.
# C - O sistema precisa ser capaz de: depositar, sacar, consultar saldo, consultar informações dos clientes e alterar informações dos clientes. 
# Não deve ser possível ter saldo negativo, nem sacar além do saldo.
# Crie ao menos 1 instância de Conta_Corrente, execute todos os métodos para teste.



class Cliente:
    def __init__(self,nome,cpf,endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def consultar_info_cliente(self):
        return f"Dados do usuário:\nNome do usuário:{self.nome}\nCPF:{self.cpf}\nEndereço:{self.endereco}"
    
    def alterar_nome(self,alterar_nome):
        self.nome = alterar_nome
        return f"Nome alterado com sucesso para:{alterar_nome}"
    
    def alterar_cpf(self,alterar_cpf):
        self.cpf = alterar_cpf
        return f"CPF alterado com sucesso para:{alterar_cpf}"

    def alterar_endereco(self,alterar_endereco):
        self.endereco = alterar_endereco
        return f"Endereço alterado com sucesso para:{alterar_endereco}"

    
class Conta_corrente(Cliente):
    def __init__(self, nome, cpf, endereco, saldo: float):
        super().__init__(nome, cpf, endereco)
        self.__saldo = saldo

    def consultar_saldo(self):
        return f"O saldo da conta é de R${self.__saldo:.2f}."
    
    def depositar(self, add_saldo: float):
        self.__saldo += add_saldo
        return f"O valor R${add_saldo:.2f} foi depositado em sua conta. Saldo atual R${self.__saldo:.2f}."
    
    def sacar(self, retirar_saldo):
        if self.__saldo >= retirar_saldo:
            self.__saldo -= retirar_saldo
            return f"O valor de R${retirar_saldo:.2f} foi retirado de sua conta. Saldo atual R${self.__saldo:.2f}."
        else:
            return f"Tentativa de saque no valor de R${retirar_saldo:.2f}. Saldo insuficiente!"
    
    def consultar_saldo(self):
        return f"O saldo atual da conta: R${self.__saldo:.2f}."
    
    def consultar_info_cliente(self):
        return f"Nome do usuário:{self.nome}\nCPF:{self.cpf}\nEndereço:{self.endereco}\nSaldo total da conta: R${self.__saldo:.2f}"


cliente1 = Conta_corrente("Jefferson Duarte","012.345.678-90","Minas Gerais - MG",100)

print(cliente1.consultar_info_cliente()) #Apresentação após inserção dos dados e saldo inicial da conta.
print("."*30) #Detalhe visual no print.
print(cliente1.alterar_nome("Jefferson Pereira"))
print(cliente1.alterar_cpf("098.765.432-10"))
print(cliente1.alterar_endereco("Rio de Janeiro - RJ"))
print("."*30)
print(cliente1.consultar_info_cliente()) #Apresentação de dados atualizados e saldo atual.
print("."*30)
print(cliente1.depositar(500.50))
print("."*30)
print(cliente1.sacar(2000.90))
print("."*30)
print(cliente1.sacar(500.00))
print("."*30)
print(cliente1.consultar_info_cliente()) #Apresentação de dados atualizados com saldo final.
