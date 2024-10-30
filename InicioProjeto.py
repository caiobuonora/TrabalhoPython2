import os
os.system("cls")

opc=0
cont=0
qt_rT=0
qt_rC=0

def add():
    if t_c=="T":
        with open('treinos.txt','w') as arquivotxt:
            try:
                data = input("Digite a data da ocasião (formato DD-MM-YYYY): ")
                distancia = float(input("Digite a distância percorrida (em KM): "))
                tempo = float(input("Digite o tempo de duração (em Horas): "))
                localizacao = input("Digite a localização do lugar: ")
                condicoes_climaticas =input("Digite a condição climática (Neve, Chuva, Ensolarado ou Nublado): ")
                for i in range(qt_rT):
                    arquivotxt.write(f"{i+1}º TREINO->|Data: {data}|Distância: {distancia}km |Tempo de duração: {tempo}h|Localização: {localizacao}|Condição climática: {condicoes_climaticas}|")
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
                for i in range(qt_rC):
                    arquivotxt.write(f"{i+1}º COMPETIÇÃO-> |Data: {data} |Distância: {distancia}km |Tempo de duração: {tempo}h |Localização: {localizacao} |Condição climática: {condicoes_climaticas}|")
                    i+=1
            except ValueError:
                print("Alguma informação digitada é inválida")

def vizu1():
    with open('treinos.txt','r') as arquivotxt:
        for i in arquivotxt:
            print(i)

def vizu2():
    with open('competicoes.txt','r') as arquivotxt:
        for i in arquivotxt:
            print(i)

print("Digite 1 para fazer um registro")
print("Digite 2 para visualizar os registros")
print("Digite 3 para atualizar os registros")
print("Digite 4 para excluir um registro")
print("Digite 5 para parar")

while opc!=5:
    opc=int(input("Digite o que você quer fazer: "))
    

    if opc==1:
        print("Digite T para treino \nDigite C para competição")
        t_c=input("Quer registrar treino ou competição?: ")
        if t_c=="T":
            qt_rT+=1
        elif t_c=="C":
            qt_rC+=1
        else:
            print("Opção inválida")
        add()
    if opc==2:
        vizu1()
        vizu2()

    
