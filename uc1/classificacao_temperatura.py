temp = []

for i in range(6):
    temp_amb = int(input("Digite a temperatura: "))
    if temp_amb < 15:
        print("Frio")
    elif (temp_amb < 28):
        print("Agradável")
    else:
        print("Quente")


