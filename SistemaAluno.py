def Cadastrar_aluno(): 
    nome = input("escreva o nome do aluno: ")
    notas = []
    for i in range(1, 5):
        nota = float(input(f"escreva a nota do {i}° semestre do aluno {nome}: "))
        notas.append(nota)
    
    frequencia = int(input("escreva o percentual de frequencia: "))
    return (nome, notas, frequencia)

Lista_alunos = {
    "roberto": {"nota": [8, 7, 6, 9], "frequencia": 76},
}

def Calcular_frequencia(frequencia):
    if frequencia <= 75:
        return "aluno reprovado por falta"
    else:
        return "aluno com frequencia boa"

def calcular_media(notas):
    return sum(notas) / len(notas)

def Calcular_situacaoNota(media):
    if media >= 7:
        return "aluno aprovado por nota"
    elif 4 <= media < 7:
        return "aluno em recuperação"
    else: 
        return "aluno reprovado por nota"

def relatorio_aluno(nome):
    if nome in Lista_alunos:
        notas = Lista_alunos[nome]["nota"]
        frequencia = Lista_alunos[nome]["frequencia"]
        
        media = calcular_media(notas)
        situacao_nota = Calcular_situacaoNota(media)
        situacao_frequencia = Calcular_frequencia(frequencia)
        
        print(f"{nome} está com média {media} e sua situação é '{situacao_nota}' e frequência de {frequencia}% está '{situacao_frequencia}' ")
    else: 
        print("Aluno não encontrado.")