import os
os.system("cls")

i=0
j=0
treino_comp=[]
opc=0
v_data=[]
v_tempo=[]
v_dist=[]
v_loc=[]
v_condc=[]

print("Digite 1 para fazer um registro \nDigite 2 para visualizar os registros \nDigite 3 para atualizar algum registro \nDigite 4 para excluir algum registro \nDigite 5 para parar")
while opc!=5:
    opc=int(input("\nO que você deseja fazer: "))
    if opc==1:
        print("Digite t para registrar um treino \nDigite c para registrar uma competição")
        adc=str(input("Quer registrar um treino ou uma competição?: "))
        if adc=="t":
            treino_comp.append(f"T{i+1}")
            data = input("Digite a data (formato DD-MM-YYYY): ")
            v_data.append(data) 
            distancia = float(input("Digite a distância percorrida (em KM): "))
            v_dist.append(distancia)
            tempo = float(input("Digite o tempo de duração (em Horas): "))
            v_tempo.append(tempo)
            localizacao = input("Digite a localização: ")
            v_loc.append(localizacao)
            condicoes_climaticas = (input("\tNEVE \tCHUVA \tNUBLADO \tENSOLARADO \nDigite a condição climática: "))
            v_condc.append(condicoes_climaticas)
            if len(data)==10 and data[2]=='-' and data[5]=='-':
                ano=int(data[6:10])
                mes=int(data[3:5])
                dia=int(data[0:2])

                if 0<mes<13 and 0<dia<32:
                    print(f"Data: {dia}/{mes}/{ano}")
                else:
                    print("Data inválida")
            else:
                print("Formato inválido")

            print(f"Distância: {distancia}Km")
            print(f"Tempo de duração: {tempo}h")
            print(f"Localização: {localizacao}")
            print(f"Condição climática: {condicoes_climaticas}")
            i+=1
        if adc=="c":
            treino_comp.append(f"C{j+1}")
            data = input(" Digite a data da ocasião (formato DD-MM-YYYY): ") 
            distancia = float(input(" Digite a distância percorrida (em KM): "))
            tempo = float(input(" Digite o tempo de duração (em Horas): "))
            localizacao = input(" Digite a localização do lugar: ")
            condicoes_climaticas =input("\tNEVE \tCHUVA \tENSOLARADO \tNUBLADO \nDigite a condição climática: ")

            if len(data) == 10 and data[2] == '-' and data[5] == '-':
                ano = int(data[6:10])
                mes = int(data[3:5])
                dia = int(data[0:2])

                if 0 < mes < 13 and 0 < dia < 32:
                    print(f" A data da ocasião é {dia}/{mes}/{ano}")
                else:
                    print(" Data inválida ")
            else:
                print(" Formato inválido ")

            print(f" Distância: {distancia} Km ")
            print(f" O tempo de duração da ocasião será de {tempo} horas ")
            print(f" A localização da ocasião será na {localizacao} ")
            print(f" Condição climática: {condicoes_climaticas}")
            j+=1
    elif opc==2:
        for i in treino_comp:
            print(i,end=" ")
        print("\nData:")
        for i in v_data:
            print(i)
        print("Distância: ")
        for i in v_dist:
            print(i)
        print("Tempo: ")
        for i in v_tempo:
            print(i)
        print("Localização: ")
        for i in v_loc:
            print(i)
        print("Condição climática: ")
        for i in v_condc:
            print(i)

    elif opc==3:
        updt=int(input(("Digite qual registro você deseja atualizar: ")))
        nv=(input("Digite o novo registro: "))
        treino_comp[updt-1]=nv
    elif opc==4:
        exc=(input("Digite qual o registro que você deseja excluir: "))
        treino_comp.remove(exc)
    elif opc==5:
        break
    else:
        print("Código inválido")

