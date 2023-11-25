print("Bem Vindo ao Prontuário Eletrônico by Adaptive Dialogs\n")

lista_pacientes = []
lista_prontuario = []

sair = 1
while sair != 0:
    opcao = int(input("Selecione uma opção:\n"
                      "1 - Cadastrar Paciente\n"
                      "2 - Listar Pacientes Cadastrados\n"
                      "3 - Criar novo Prontuário (Apenas com Pacientes já cadastrados)\n"
                      "4 - Pesquisar Prontuário via ID\n"
                      "5 - Visualizar Médicos Disponíveis\n"
                      "6 - Visualizar Médicos em Atendimento\n"))

    # PEDRO FAZER UMA LOGICA PARA AS OPCOES 5 e 6

    if opcao == 1:
        print("Você selecionou: Cadastrar Paciente")
        sairCadPacie = 1
        cod = 0
        while sairCadPacie != 0:
            # Adicionar dicionário para criar prontuário
            cod += 1
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            idade = int(input("Idade: "))
            email = input("Email: ")
            sexo = input("Sexo: [M - Masc | F - Fem] ").upper()
            tipo_sang = input("Tipo Sanguíneo: ").upper()

            dados_paciente = {'ID': cod, 'Nome': nome, 'Sobrenome': sobrenome, 'Idade': idade, 'Email': email, 'Sexo': sexo, 'Tipo_sang': tipo_sang}

            lista_pacientes.append(dados_paciente)
            print("Paciente Cadastrado com Sucesso!")

            sairCadPacie = int(input("Deseja continuar? (1 - SIM | 0 - NÃO) "))

    elif opcao == 2:
        print("Você selecionou: Listar Pacientes Cadastrados")
        for i in range(len(lista_pacientes)):
            print("-="*30)
            print(f"PACIENTE nº{lista_pacientes[i]['ID']}\n"
                  f"NONE: {lista_pacientes[i]['Nome']}\n"
                  f"SOBRENOME: {lista_pacientes[i]['Sobrenome']}\n"
                  f"IDADE: {lista_pacientes[i]['Idade']}\n"
                  f"EMAIL: {lista_pacientes[i]['Email']}\n"
                  f"SEXO: {lista_pacientes[i]['Sexo']}\n"
                  f"TIPO SANGUÍNEO: {lista_pacientes[i]['Tipo_sang']}")
            print("-="*30)

    elif opcao == 3:

        print("Você selecionou: Criar novo Prontuário")
        id_pacie = int(input("Informe o ID do paciente: "))
        cod_prontu = 0
        for i in range(len(lista_pacientes)):
            if id_pacie == lista_pacientes[i]['ID']:
                nome_pacie = lista_pacientes[i]['Nome']
                sobrenome_pacie = lista_pacientes[i]['Sobrenome']
                idade_pacie = lista_pacientes[i]['Idade']

                cod_prontu += 1
                historico = []
                antecedentes_familiares = []
                medicamentos = []

                sairProntu_hist = 1
                while sairProntu_hist != 0:
                    historico.append(input("Informe seu histórico médico: "))
                    sairProntu_hist = int(input("Adicionar mais informações ao histórico? [1 - SIM | 0 - NÃO] "))

                sairProntu_anteced = 1
                while sairProntu_anteced != 0:
                    antecedentes_familiares.append(input("Informe antecedentes familiares: "))
                    sairProntu_anteced = int(input("Adicionar mais informações ao antecedente familiar? [1 - SIM | 0 - NÃO] "))

                sairProntu_medicamento = 1
                while sairProntu_medicamento != 0:
                    medicamentos.append(input("Informe medicamentos que utiliza: "))
                    sairProntu_medicamento = int(input("Adicionar mais informações ao antecedente familiar? [1 - SIM | 0 - NÃO] "))

                dados_prontu = {'ID_prontu': cod_prontu, 'Nome': nome_pacie, 'Sobrenome': sobrenome_pacie, 'Idade': idade_pacie, 'Historico': historico, 'Antecedentes_famil': antecedentes_familiares, 'Medicamentos': medicamentos}

                lista_prontuario.append(dados_prontu)
                print("Prontuário Cadastrado com Sucesso!")

            else:
                print("Informe o ID do paciente válido!")

    elif opcao == 4:
        print("Você selecionou: Pesquisar Prontuário via ID")
        id_prontu = int(input("Informe o ID do Prontuário: "))

        for i in range(len(lista_prontuario)):
            if id_prontu == lista_prontuario[i]['ID_prontu']:
                print("-=" * 30)
                print(f"PRONTUÁRIO nº{lista_prontuario[i]['ID_prontu']}\n"
                      f"NOME: {lista_prontuario[i]['Nome']}\n"
                      f"SOBRENOME: {lista_prontuario[i]['Sobrenome']}\n"
                      f"IDADE: {lista_prontuario[i]['Idade']}\n"
                      f"HISTÓRICO: {lista_prontuario[i]['Historico']}\n"
                      f"ANTECEDENTES FAMILIARES: {lista_prontuario[i]['Antecedentes_famil']}\n"
                      f"MEDICAMENTOS: {lista_prontuario[i]['Medicamentos']}")
                print("-="*30)

            else:
                print("Prontuário não Cadastrado")

    # PEDRO OPCOES 5 E 6
'''    elif opcao == 5:
    elif opcao == 6:'''

    sair = int(input("Deseja finalizar o programa? (1 - NÃO | 0 - SIM) "))
    print("Obrigado pela preferência de utilizar o Prontuário Eletrônico by Adaptive Dialogs")
