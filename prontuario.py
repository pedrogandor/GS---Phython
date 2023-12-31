print("Bem Vindo ao Prontuário Eletrônico by MedIAssist\n")

lista_pacientes = []
lista_prontuario = []
medicos = [
    {"nome": "Dr. João Camargo", "crm": "17335", "area_atuacao": "Clínica Geral", "em_atendimento": True},
    {"nome": "Dra. Maria Alves", "crm": "67890", "area_atuacao": "Cardiologia", "em_atendimento": False},
    {"nome": "Dr. Carlos Zamago", "crm": "54321", "area_atuacao": "Dermatologia", "em_atendimento": True},
    {"nome": "Dra. Ana Nardelli", "crm": "98765", "area_atuacao": "Pediatria", "em_atendimento": False},
    {"nome": "Dra. Laura Padial", "crm": "45678", "area_atuacao": "Ortopedia", "em_atendimento": True},
    {"nome": "Dr. Pedro Gandor", "crm": "23456", "area_atuacao": "Ginecologia", "em_atendimento": False},
    {"nome": "Dra. Fernanda Paif", "crm": "78901", "area_atuacao": "Neurologia", "em_atendimento": True},
    {"nome": "Dr. Ricardo Gourlat", "crm": "56789", "area_atuacao": "Oftalmologia", "em_atendimento": False},
    {"nome": "Dra. Camila Silva", "crm": "34567", "area_atuacao": "Urologia", "em_atendimento": True},
    {"nome": "Dr. André Jr", "crm": "89012", "area_atuacao": "Endocrinologia", "em_atendimento": False},
    {"nome": "Dra. Luiza Betchold", "crm": "67890", "area_atuacao": "Cardiologia", "em_atendimento": True},
    {"nome": "Dr. Guilherme Bocallini", "crm": "12345", "area_atuacao": "Clínica Geral", "em_atendimento": False},
]

def handle_cadastrar_paciente():
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

def handle_listar_pacientes():
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

def handle_criar_prontuario(id_pacie):
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
                sairProntu_medicamento = int(input("Adicionar mais medicamentos? [1 - SIM | 0 - NÃO] "))

            dados_prontu = {'ID_prontu': cod_prontu, 'Nome': nome_pacie, 'Sobrenome': sobrenome_pacie, 'Idade': idade_pacie, 'Historico': historico, 'Antecedentes_famil': antecedentes_familiares, 'Medicamentos': medicamentos}

            lista_prontuario.append(dados_prontu)
            print("Prontuário Cadastrado com Sucesso!")

        else:
            print("Informe o ID do paciente válido!")

def handle_procurar_prontuario_por_id(id_prontu):
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

def handle_medicos_disponiveis():
    for medico in [medico for medico in medicos if not medico["em_atendimento"]]:
        print("-=" * 30)
        print(f"MÉDICO\n"
                f"NOME: {medico['nome']}\n"
                f"CRM: {medico['crm']}\n"
                f"ÁREA DE ATUAÇÃO: {medico['area_atuacao']}")
        print("-=" * 30)

def handle_medicos_atendimento():
    for medico in [medico for medico in medicos if medico["em_atendimento"]]:
        print("-=" * 30)
        print(f"MÉDICO\n"
                f"NOME: {medico['nome']}\n"
                f"CRM: {medico['crm']}\n"
                f"ÁREA DE ATUAÇÃO: {medico['area_atuacao']}\n"
                f"STATUS DE ATENDIMENTO: {'Em Atendimento' if medico['em_atendimento'] else 'Disponível'}")
        print("-=" * 30)

sair = 1
while sair != 0:
    opcao = int(input("Selecione uma opção:\n"
                      "1 - Cadastrar Paciente\n"
                      "2 - Listar Pacientes Cadastrados\n"
                      "3 - Criar novo Prontuário (Apenas com Pacientes já cadastrados)\n"
                      "4 - Pesquisar Prontuário via ID\n"
                      "5 - Visualizar Médicos Disponíveis\n"
                      "6 - Visualizar Médicos em Atendimento\n"))

    if opcao == 1:
        print("Você selecionou: Cadastrar Paciente")
        handle_cadastrar_paciente()

    elif opcao == 2:
        print("Você selecionou: Listar Pacientes Cadastrados")
        handle_listar_pacientes()

    elif opcao == 3:
        print("Você selecionou: Criar novo Prontuário")
        id_pacie = int(input("Informe o ID do paciente: "))
        handle_criar_prontuario(id_pacie)

    elif opcao == 4:
        print("Você selecionou: Pesquisar Prontuário via ID")
        id_prontu = int(input("Informe o ID do Prontuário: "))
        handle_procurar_prontuario_por_id(id_prontu)

    elif opcao == 5:
        print("Você selecionou: Visualizar Médicos Disponíveis")
        print("Médicos Disponíveis:")
        handle_medicos_disponiveis()

    elif opcao == 6:
        print("Você selecionou: Visualizar Médicos em Atendimento")
        print("Médicos em Atendimento:")
        handle_medicos_atendimento()

    sair = int(input("Deseja finalizar o programa? (1 - NÃO | 0 - SIM) "))
    print("Obrigado pela preferência de utilizar o Prontuário Eletrônico by MedIAssist")
