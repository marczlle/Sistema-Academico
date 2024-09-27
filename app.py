# criando dicionario para os alunos
alunos = {}

# funções para funcionalidades do sistema

# verificação se o aluno está cadastrado no dicionário
def verificarAluno(nomeAluno): 
    if nomeAluno not in alunos:
        return False ##sai do loop principal se o aluno não estiver cadastrado

# adicionar o aluno(chave) e seu valores(notas, frequências)
def adicionarAluno(nome):
    alunos[nome] = {"notas": [], "frequencia": 0}

# procura o aluno existente e altera para nova frequência
def editarFrequencia(nomeAluno, novaFrequencia):
    alunos[nomeAluno]["frequencia"] = novaFrequencia

# itera dentro de alunos e notas
def editarNotas(nomeAluno):
    for i in range(len(alunos[nomeAluno]["notas"])):
        nota = float(input(f"Insira a nova nota {i + 1} (máximo 4): ")) ## loop para limite de notas ser quatro.
        alunos[nomeAluno]["notas"][i] = nota

# deleta o nome do aluno em alunos
def removerAluno(nomeAluno):
    del alunos[nomeAluno]


# adiciona notas ao aluno já adicionado
def definirNotas(nomeAluno):
    for i in range(4):
        nota = float(input(f"Insira a nota {i + 1} (máximo 4): ")) ## loop para limite de notas ser quatro.
        alunos[nomeAluno]["notas"].append(nota)

# adiciona a frequência ao aluno já adicionado
def definirFrequencia(nomeAluno, frequencia):
    alunos[nomeAluno]["frequencia"] = frequencia

# calcular média do aluno
def calcularMedia(nomeAluno):
    contador = 0
    soma = 0
    if alunos[nomeAluno]["notas"] == []:
        return 0
    for nota in alunos[nomeAluno]["notas"]:
        soma += nota
        contador += 1
    return soma/contador

# calcula a situação de frequência do aluno
def calcularSituacao(nomeAluno, cargaHoraria):
    media = calcularMedia(nomeAluno)
    if alunos[nomeAluno]["frequencia"] < (cargaHoraria * (75/100)): ## condição para conferir se passou do limite de faltas (75%)
        return "Reprovado por Falta"
    elif media >= 7:
        return "Aprovado"
    elif media < 7:
        return "Reprovado por Nota"

# imprime o relatório geral com as situações dos alunos
def imprimirRelatorioGeral():
    for aluno in alunos: ## itera os alunos cadastrados no dicionário
        media = calcularMedia(aluno)
        frequencia = alunos[aluno]["frequencia"]
        situacao = calcularSituacao(aluno, cargaHoraria)
        print(f"{aluno} - nota: {media} / frequência: {frequencia} aulas - ({situacao})") ## exibe todas as informações do aluno

# procura nota, frequência e situação para exibir o filtro
def imprimirRelatorioEspecifico(opcao2):
    for aluno in alunos:
        media = calcularMedia(aluno)
        frequencia = alunos[aluno]["frequencia"]
        situacao = calcularSituacao(aluno, cargaHoraria)
        if situacao == "Aprovado" and opcao2 == 1:
            print(f"{aluno} - nota: {media} / frequência: {frequencia} aulas - ({situacao})")
        elif situacao == "Reprovado por Falta" and opcao2 == 2:
            print(f"{aluno} - nota: {media} / frequência: {frequencia} aulas - ({situacao})")
        elif situacao == "Reprovado por Nota" and opcao2 == 3:
            print(f"{aluno} - nota: {media} / frequência: {frequencia} aulas - ({situacao})")

# variável utilizada posteriormente para calcular reprovação por falta ou não
cargaHoraria = int(input("Insira a carga horária da disciplina:\n "))

# entrando no loop do menu principal, para sempre retornar ao início
while (True):
    opcao1 = input("Qual operação deseja fazer: \n\t1. Adicionar Aluno\n\t2. Editar Informações\n\t3. Remover Aluno\n\t4. Adicionar nota\n\t5. Adicionar Frequência\n\t6. Imprimir Relatório Geral\n\t7. Imprimir Relatório Específico\n\t8. Sair do Programa\n")
    if opcao1 == '1':
        nomeAluno = input("Insira o nome do aluno: ")
        if verificarAluno(nomeAluno) == False:
            adicionarAluno(nomeAluno)
            print("Aluno cadastrado.\n")
        else:
            print("Aluno já cadastrado\n.")
    elif opcao1 == '2':
        nomeAluno = input("Insira o nome do aluno: ")
        if verificarAluno(nomeAluno) == False:
            opcao4 = int(input("Deseja Editar:\n\t1. Notas\n\t2. Frequência\n"))
            if opcao4 == 1:
              editarNotas(nomeAluno)
            elif opcao4 == 2:
             novaFrequencia = int(input("Insira a nova frequência: "))
             editarFrequencia(nomeAluno, novaFrequencia)
        else:
            print("Aluno não encontrado no sistema.\n")
    elif opcao1 == '3':
        nomeAluno = input("Insira o nome do aluno: ")
        if verificarAluno(nomeAluno) != False:
            removerAluno(nomeAluno)
            print("Aluno removido.\n")
        else:
            print("Aluno não encontrado no sistema.\n")
    elif opcao1 == '4':
        nomeAluno = input("Insira o nome do aluno: ")
        if verificarAluno(nomeAluno) != False:
            definirNotas(nomeAluno)
        else:
            print("Aluno não encontrado no sistema.\n")
    elif opcao1 == '5':
        nomeAluno = input("Insira o nome do aluno: ")
        if verificarAluno(nomeAluno) != False:
            frequencia = int(input("Insira a frequência do aluno: "))
            definirFrequencia(nomeAluno, frequencia)
        else:
            print("Aluno não encontrado no sistema.\n")
    elif opcao1 == '6':
        imprimirRelatorioGeral()
    elif opcao1 == '7':
        opcao2 = int(input("Deseja filtrar por:\n\t1. Aprovado\n\t2. Reprovado por Falta\n\t3. Reprovado por Nota \n"))
        if opcao2 == 1 or opcao2 == 2 or opcao2 == 3:
            imprimirRelatorioEspecifico(opcao2)
        else:
            print("Opção inválida.")
    elif opcao1 == '8':
        print("Saindo...")
        break
    else:
        print("Opção inválida, por favor tente de novo.\n\n")