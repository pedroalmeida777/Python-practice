#Exercicio 1 - Atividade Avaliativa Cap. 3

#variável que servirá para receber a opção digitada pelo usuário
i = 0
op = -1
resp = str
print("Olá! Estamos realizando uma votação interna com nossos colaboradores afim de defirmos um dia fixo na semana para as lives exclusivas \ncom o nosso Time de Mentoria.\nPor favor, responda a pesquisa abaixo.")

qtd = int(input("Quantos colaboradores irão participar da votação?\nR:"))

#enquanto o usuário não digitar a opção 4, o programa será executado
    #exibição das opções do menu
while (i != qtd):
    i = i + 1
    print("Colaborador Nº{}".format(i))
    print("")
    print("Qual seria o melhor dia da semana para você acompanhar as lives com o nosso Time de Mentoria?")
    print("---------------------------------------------------------------------------------------------")
    print("1 - Segunda-Feira")
    print("2 - Terça-Feira")
    print("3 - Quarta-Feira")
    print("4 - Quinta-Feira")
    print("5 - Sexta-Feira")

    op = int(input("Informe sua disponibilidade: "))

    #verificação das opções disponíveis 
    if op == 1:
    #o que ocorrerá se a opção for 1
        print("Perfeito! O dia da semana escolhida foi Segunda-Feira.")
    elif op == 2:
    #o que ocorrerá se a opção for 1
        print("Perfeito! O dia da semana escolhida foi Terça-Feira.")
    elif op == 3:
    #o que ocorrerá se a opção for 1
        print("Perfeito! O dia da semana escolhida foi Quarta-Feira.")
    elif op == 4:
    #o que ocorrerá se a opção for 1
        print("Perfeito! O dia da semana escolhida foi Quinta-Feira.")
    elif op == 5:
    #o que ocorrerá se a opção for 1
        print("Perfeito! O dia da semana escolhida foi Sexta-Feira.")
    #Quando o loop for finalizado, deve exibir a mensagem
    

        