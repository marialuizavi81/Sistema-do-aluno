from SistemaAluno import *

while True: 
    opcao = int(input("1 - Adicionar Aluno\n"
                      "2 - Deletar um aluno\n"
                      "3 - Edição de notas em aluno existente\n"
                      "4 - Edição de frequência em aluno existente\n"
                      "5 - Imprimir relatório de aluno existente\n"
                      "6 - Impressão específica de aluno\n"
                      "7 - Imprimir a lista de alunos \n"
                      "8 - Sair do programa\n"
                      "escreva: "))
    
    if opcao == 1:
        nome, notas, frequencia = Cadastrar_aluno()
        Lista_alunos[nome] = {"nota": notas, "frequencia": frequencia}
        print(f"Aluno {nome} cadastrado com sucesso!")
        
    elif opcao == 2:
        nome = input("Escreva o nome do aluno que deseja deletar: ")
        if nome in Lista_alunos:
            del Lista_alunos[nome]
            print(f"Aluno {nome} deletado com sucesso.")
        else:
            print("Aluno não encontrado.")
    
    elif opcao == 3:
        nome = input("Escreva o nome do aluno existente: ")
        if nome in Lista_alunos:
            notas = []
            for i in range(1, 5):
                nota = float(input(f"Escreva a nova nota do {i}° semestre do aluno {nome}: "))
                notas.append(nota)
            Lista_alunos[nome]["nota"] = notas  
            print("As novas notas foram adicionadas com sucesso.")
        else: 
            print("Aluno não encontrado.")
    
    elif opcao == 4:
        nome = input("Escreva o nome do aluno existente: ")
        if nome in Lista_alunos:
            frequencia = int(input("Escreva a nova frequência: "))
            Lista_alunos[nome]["frequencia"] = frequencia  
            print("A nova frequência foi atualizada com sucesso.")
        else:
            print("Aluno não encontrado.")
    
    elif opcao == 5: 
        nome = input("Escreva o nome do aluno existente: ")
        relatorio_aluno(nome)
    
    elif opcao == 6:
        nome = input("Escreva o nome do aluno existente: ")
        if nome in Lista_alunos:
            opikao2 = int(input("Você quer saber o que do aluno?\n"
                                "1 - Qual sua situação de média?\n"
                                "2 - Qual sua situação de frequência?\n"
                                "escreva: "))
            if opikao2 == 1:
                media = calcular_media(Lista_alunos[nome]["nota"])
                situacao_nota = Calcular_situacaoNota(media)  # Calcular a situação da nota
                print(f"A média do aluno {nome} é: {media:.2f} e o aluno está {situacao_nota}")     
                
            if opikao2 == 2:
                frequencia = Lista_alunos[nome]["frequencia"]
                situacao_frequencia = Calcular_frequencia(frequencia)
                print(f"A situação de frequência do aluno {nome} é: {situacao_frequencia}")
            else: 
                print("aluno nao encontrado.")
            
            
    elif opcao == 7:
        print(Lista_alunos)
        
    elif opcao == 8: 
        print("Saindo do programa...")
        break
    
    else: 
        print("Opção inválida.")