#média das notas
nome = input('Digite seu nome: ')
idade =  int(input('Digite sua idade: '))
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2


if media >= 7.0:
    print('Aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Reprovado')
