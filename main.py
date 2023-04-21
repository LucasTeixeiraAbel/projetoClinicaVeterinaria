from entities import Cliente, Animal, Consulta
consultas = []

while True:
    print('BEM VINDO A CLÍNICA VETERINÁRIA PET-SAÚDE\n')
    print('Selecione uma das opções abaixo:\n')
    print('1º Cadastrar Cliente')
    print('2º Cadastrar Animal')
    print('3º Agendar uma Consulta')
    print('4º Exibir consultas agendadas')
    print('5º Pagamento')
    print('6º Sair')

    opcao = input('\nDigite a opção desejada: ')

    if opcao == '1':
        print('\nCadastro do cliente')
        nome_cliente = input('Nome: ')
        telefone_cliente = input('Telefone: ')
        email_cliente = input('Email: ')
        cliente = Cliente(nome_cliente, telefone_cliente, email_cliente)
        cliente.exibir_cliente()
        
    elif opcao == '2':
        print('\nCadastro do animal')
        nome_animal = input('Nome: ')
        especie_animal = input('Espécie: ')
        idade_animal = input('Idade: ')
        peso_animal = input('Peso: ')
        animal = Animal(nome_animal, especie_animal, idade_animal, peso_animal)
        animal.exibir_animal()
        
    elif opcao == '3':
        print('\nCadastro da consulta')
        data_consulta = input('Data (dd/mm/aaaa): ')
        motivo_consulta = input('Motivo: ')
        diagnostico_consulta = input('Diagnóstico: ')
        consulta = Consulta(cliente, animal, data_consulta, motivo_consulta, diagnostico_consulta)
        consulta.exibir_consulta()
        consultas.append(consulta)
        
    elif opcao == '4':
        print('\nConsultas cadastradas:\n')
        for consulta in consultas:
            consulta.exibir_consulta()
            
    elif opcao == '5':
        
            while True:
                print('1° Credito')
                print('2º Debito')
                print('3º Dinheiro')

                opcao_pagamento = input('Escolha sua opção de pagamento:')
                if opcao_pagamento == '1':
                    print('Escolhido Crédito, pagamento efetuado com juros!')
                    break
                elif opcao_pagamento == '2':
                    print('Escolhido Debito, pagamento efetuado!')
                    break
                elif opcao_pagamento == '3':
                    print('Escolhido Dinheiro, pagamento efetuado!')
                    break
                else:
                    print('Opção inválida, tente novamente!')
           
    elif opcao == '6':
        print('Fim')
        break
    else:
        print('Opção Inválida. Por favor, Tente Novamente')
    

