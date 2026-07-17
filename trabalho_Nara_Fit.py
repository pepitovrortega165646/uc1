## Criando lista - armazenará os alunos cadastrados ##
alunos = {
    "nomes": [],
    "idades": [],
    "pesos": [],
    "alturas": [],
    "imc": [],
    "classificacoes": [],
    "sexo": [],
    "ciclo_vida": [],
    }

## MENU - NARA FIT ##

print("=" * 60)
print("BEM-VINDO AO NARA FIT ".center(60))
print("=" * 60)


nome_usuario = input("Bem vindo ao Nara Fit. Informe o seu login de usuário: ")

## 1 - Função - Calcular o IMC ##
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

## 2- Função - Classificar o IMC ##
def classificar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc <= 24.9:
        return "peso normal"
    elif imc <= 29.9:
        return "sobrepeso"
    else:
        return "obesidade"

### 3- FUNÇÃO PARA LER UM NÚMERO INT ####
def ler_numero_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor <= 0:
                print("Digite um número maior que zero!")
            else:
                return valor # Sai do loop e retorna o valor correto
        except ValueError:
            print("Entrada inválida. Digite um número inteiro!")
                
### 4- FUNÇÃO PARA LER UM NÚMERO FLOAT ####
def ler_numero_float(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            if numero <= 0:
                raise ValueError
            return numero
        except ValueError:
            print("Digite um número maior que zero!")
            
### 5- FUNÇÃO PARA LER SEXO ####
def ler_sexo(mensagem):
    while True:
        try:
            sexo = input(mensagem).strip().upper()
            if sexo not in ["F", "M"]:
                raise ValueError
            return sexo
        except ValueError:
            print("Digite apenas F para feminino ou M para masculino.")
            
### 6- FUNÇÃO PARA CLASSIFICAR CICLO DE VIDA ####
### Criança (0-12) | Adolescente (13-19) | Adulto (20 a 59 anos) | Idoso (60 anos ou mais)
def classificar_ciclo_vida(idade):
    if idade <= 12:
        return "criança"
    elif idade <= 19:
        return "adolescente"
    elif idade <60:
        return "adulto"
    else:
        return "idoso"
    
### 7 - FUNÇÃO PARA ESCOLHA DO MENU###
def escolher_menu(nome_usuario):
    while True:
        opcao = ler_numero_int(f"Olá, {nome_usuario}. Como deseja prosseguir? \n 1 - Cadastrar aluno \n 2 - Listar alunos \n 3 - Estatísticas \n 4 - Sair \n") \n 1 - Cadastrar aluno \n 2 - Listar alunos \n 3 - Estatísticas \n 4 - Sair \n")
        if 1 <= opcao <= 4:
            return opcao
        print("Digite uma opção entre 1 e 4.")
## Escolhendo o menu ##
while True:
    escolha_menu = escolher_menu(nome_usuario)
    # Verifica qual opção foi escolhida pelo usuário
    match escolha_menu:
        case 1:
            print("----- Iniciando o cadastro do aluno -----")
            nome = input("Informe o nome completo do aluno: ")
            sexo = ler_sexo("Informe sexo do aluno: F (feminino) | M (masculino) ")
            idade = ler_numero_int("Informe a idade do aluno: ")
            peso = ler_numero_int("Informe o peso (kg) do aluno: ") 


        


    
