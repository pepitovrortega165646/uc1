alunos[]
print('#' *20, 'Bem vindo a academia  Nara Fit', '#' *20)

while True:
    opcao
    print("1- Cadastrar novo aluno.")
    print("2- Listar todos os alunos.")
    print("3- Ver estatísticas da academia.")
    print("4- Sair")

    if opcao == 1:
        nome_aluno = input("Digite o seu nome: ").title()
        idade_aluno = input("Digite sua idade")
        peso_aluno = input("Digite seu peso")
        altura_aluno = input("Digite sua altura")
        alunos.append()

        imc = peso / (altura ** 2)

        if imc < 18.5:
            print("Abaixo do peso.")

        elif imc < 25:
            print("Peso normal.")

        elif imc < 30:
            print("Sobrepeso.")
        else:
        print("Obesidade")


        


    