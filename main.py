# TODAS A FUNCIONALIDADES DO SISTEMA DE ADMINISTRAÇÃO ESCOLAR AINDA ESTÃO EM DESENVOLVIMENTO, PORTANTO,
# HÁ FUNCIONALIDADES AINDA INCOMPLETAS OU QUE PRECISAM SER MELHORADAS.
def exibir_menu():
    print("\n === Sitema de Adminstração Esscolar ===")
    print("1 - Matricular Aluno")
    print("2 - Turmas e horários")
    print("3 - Registro de Presenças")
    print("4 - Genrenciar de Notas")
    print("5 - Distriuição do materiais")
    print("6 - Portal dos Pais")
    print("7 - Pagamento das mensalidades")
    print("8 - Genrenciamento de Porvas")
    print("9 - Rastreamento do ônibus escolar")
    print("10 - Atividades Extracurriculares")
    print("11 - Sair")
    
    print("=========================================")
    
    
Alunos = []
presenças = {}
notas = {}
    
def matricular_aluno():
    nome = input("Digite o nome do aluno: ")
    id_aluno = len(Alunos) + 1
    Alunos.append({"id": id_aluno, "nome": nome})
    print(f"Aluno {nome} com sucesso matriculado com ID {id_aluno}.")
        
def gerenciar_turmas():
        turma = input("Digite o nome da turma: ")
        horario = input("Digite o horário da turma: ")
        print(f"Turma {turma} criada com sucesso no horário {horario}.")
            
def registrar_presenca():
    id_aluno = int(input("Digite o ID do aluno: "))
    dia = input("Digite a data (DD/MM/AAAA): ")
    if id_aluno not in presenças:
        presenca = input("O aluno está presente? (s/n): ")
        if presenca.lower() == 's':
            presenças[id_aluno] = []
            presenças[id_aluno].append(dia)
            print(f"Presença registrada para o aluno ID {id_aluno} na data (dia).")
    else:
        print("ID de aluno inválido.")
            
def gerenciar_notas():
    id_aluno = int(input("Digite o ID do aluno: "))
    if id_aluno not in notas:
        notas[id_aluno] = []
    nota = float(input("Digite a nota do aluno: "))
    notas[id_aluno].append(nota)
    print(f"Nota {nota} registrada para o aluno ID {id_aluno}.")
    
def distribuir_materiais():
    id_aluno = int(input("Digite o ID do aluno: "))
    material = input("Digite o material a ser distribuído: ")
    print(f"Material '{material}' distribuído para o aluno ID {id_aluno}.")
    
def portal_pais():
    id_aluno = int(input("Digite o ID do aluno: "))
    if id_aluno in Alunos:
        print(f"Portal dos pais acessado para o aluno ID {id_aluno}.")
    else:
        print("ID de aluno inválido.")
        
    # a ser melhorado com a adição das funcionalidades de pagamento
def pagamento_mensalidades():
    id_aluno = int(input("Digite o ID do aluno: "))
    print("Selecione a forma de pagamento:")
    print("1 - Cartão de crédito")
    print("2 - Boleto bancário")
    forma_pagamento = input("Digite a opção desejada (1 ou 2): ")
    if forma_pagamento == '1':
        print("Pagamento realizado com cartão de crédito.")
    elif forma_pagamento == '2':    
        print("Pagamento realizado com boleto bancário.") 
    else:
        print("Opção inválida. Pagamento não realizado.")
    if id_aluno in Alunos:
        print(f"Pagamento de mensalidade realizado para o aluno ID {id_aluno}.")
    else:
        print("ID de aluno inválido.")    
        
def gerenciar_provas():
    id_aluno = int(input("Digite o ID do aluno: "))
    if id_aluno in Alunos:
        prova = input("Digite o nome da prova: ")
        data = input("Digite a data da prova (DD/MM/AAAA): ")
        print(f"Prova '{prova}' agendada para o aluno ID {id_aluno} na data {data}.")
    else:
        print("ID de aluno inválido.")
        
def rastreamento_onibus():
    id_aluno = int(input("Digite o ID do aluno: "))
    if id_aluno in Alunos:
        print(f"Rastreamento do ônibus escolar para o aluno ID {id_aluno} iniciado.")
    else:
        print("ID de aluno inválido.")
        
def atividades_extracurriculares():
    id_aluno = int(input("Digite o ID do aluno: "))
    if id_aluno in Alunos:
        atividade = input("Digite a atividade extracurricular: ")
        print(f"Atividade '{atividade}' registrada para o aluno ID {id_aluno}.")
    else:
        print("ID de aluno inválido.")
    
def principal():
    print("Bem-vindo ao Sistema de Administração Escolar!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            matricular_aluno()
        elif opcao == '2':
            gerenciar_turmas()
        elif opcao == '3':
            registrar_presenca()
        elif opcao == '4':
            gerenciar_notas()
        elif opcao == '5':
            distribuir_materiais()
        elif opcao == '6':
            portal_pais()
        elif opcao == '7':
            pagamento_mensalidades()
        elif opcao == '8':
            gerenciar_provas()
        elif opcao == '9':
            rastreamento_onibus()
        elif opcao == '10':
            atividades_extracurriculares()
        elif opcao == '11':
            print("Saindo do sistema...")
            break
        else:

            print("Opção inválida. Tente novamente.")
        
if __name__ == "__main__":
    principal()
