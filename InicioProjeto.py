import os
os.system("cls")

opc=0
cont=0
qt_r=0

def add():
    if t_c=="T":
        with open('treinos.txt','w') as arquivotxt:
            try:
                data = input("Digite a data da ocasião (formato DD-MM-YYYY): ")
                distancia = float(input("Digite a distância percorrida (em KM): "))
                tempo = float(input("Digite o tempo de duração (em Horas): "))
                localizacao = input("Digite a localização do lugar: ")
                condicoes_climaticas =input("Digite a condição climática (Neve, Chuva, Ensolarado ou Nublado): ")
                for i in range(qt_r):
                    arquivotxt.write(f"{i+1}ªTREINO->|Data: {data}|Distância: {distancia}|Tempo de duração: {tempo}|Localização: {localizacao}|Condição climática: {condicoes_climaticas}|")
                    i+=1
            except ValueError:
                print("Alguma informação digitada é inválida")
    elif t_c=="C":
        with open('competicoes.txt','w') as arquivotxt:
            try:
                data = input(" Digite a data da ocasião (formato DD-MM-YYYY): ")
                distancia = float(input(" Digite a distância percorrida (em KM): "))
                tempo = float(input(" Digite o tempo de duração (em Horas): "))
                localizacao = input(" Digite a localização do lugar: ")
                condicoes_climaticas =input("Digite a condição climática (Neve, Chuva, Ensolarado ou Nublado): ")
                for i in range(qt_r):
                    arquivotxt.write(f"{i+1}ªCompetição \nData: {data} \nDistância: {distancia} \nTempo de duração: {tempo} \nLocalização: {localizacao} \nCondição climática: {condicoes_climaticas}")
                    i+=1
            except:
                print("Alguma informação digitada é inválida")

def vizu():
    with open('treinos.txt','r') as arquivotxt:
        for i in arquivotxt:
            print(i)

print("Digite 1 para fazer um registro")
print("Digite 2 para visualizar os registros")
print("Digite 3 para atualizar os registros")
print("Digite 4 para excluir um registro")
print("Digite 5 para parar")

while opc!=5:
    opc=int(input("Digite o que você quer fazer: "))
    qt_r+=1

    if opc==1:
        print("Digite T para treino \nDigite C para competição")
        t_c=input("Quer registrar treino ou competição?: ")
        add()
    if opc==2:
        vizu()

    
