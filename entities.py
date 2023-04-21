class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
    def exibir_cliente(self):
        print('\nDados do cliente:')
        print('Nome:', self.nome)
        print('Telefone:', self.telefone)
        print('Email:', self.email)

class Animal:
    def __init__(self, nome, especie, idade, peso):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
    
    def exibir_animal(self):
        print('\nDados do animal:')
        print('Nome:', self.nome)
        print('Espécie:', self.especie)
        print('Idade:', self.idade)
        print('Peso:', self.peso)

class Consulta:
    def __init__(self, cliente, animal, data, motivo, diagnostico):
        self.cliente = cliente
        self.animal = animal
        self.data = data
        self.motivo = motivo
        self.diagnostico = diagnostico
    
    def exibir_consulta(self):
        print('\nDados da consulta:')
        self.cliente.exibir_cliente()
        self.animal.exibir_animal()
        print('Data:', self.data)
        print('Motivo:', self.motivo)
        print('Diagnóstico:', self.diagnostico)


