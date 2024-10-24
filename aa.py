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