import os
os.system('cls')

meta_anual = float(input("Pedro, qual é a sua meta anual de corrida (em km)? ")) 

total_corrido = 0

def atualizar_progresso(km_corrido, meta_anual, total_corrido):
    total_corrido += km_corrido
    km_restante = meta_anual - total_corrido
    if km_restante > 0:
        print(f"Faltam {km_restante} km para cumprir a meta anual.")
    else:
        print(f"Parabéns, Pedro! Você já atingiu a meta anual com {total_corrido} km percorridos.")
    return total_corrido

km_jan = float(input("Quantos km você correu em janeiro? "))
total_corrido = atualizar_progresso(km_jan, meta_anual, total_corrido)

km_fev = float(input("Quantos km você correu em fevereiro? "))
total_corrido = atualizar_progresso(km_fev, meta_anual, total_corrido)

km_mar = float(input("Quantos km você correu em março? "))
total_corrido = atualizar_progresso(km_mar, meta_anual, total_corrido)

km_abr = float(input("Quantos km você correu em abril? "))
total_corrido = atualizar_progresso(km_abr, meta_anual, total_corrido)

km_maio = float(input("Quantos km você correu em maio? "))
total_corrido = atualizar_progresso(km_maio, meta_anual, total_corrido)

km_jun = float(input("Quantos km você correu em junho? "))
total_corrido = atualizar_progresso(km_jun, meta_anual, total_corrido)

km_jul = float(input("Quantos km você correu em julho? "))
total_corrido = atualizar_progresso(km_jul, meta_anual, total_corrido)

km_ago = float(input("Quantos km você correu em agosto? "))
total_corrido = atualizar_progresso(km_ago, meta_anual, total_corrido)

km_set = float(input("Quantos km você correu em setembro? "))
total_corrido = atualizar_progresso(km_set, meta_anual, total_corrido)

km_out = float(input("Quantos km você correu em outubro? "))
total_corrido = atualizar_progresso(km_out, meta_anual, total_corrido)

km_nov = float(input("Quantos km você correu em novembro? "))
total_corrido = atualizar_progresso(km_nov, meta_anual, total_corrido)

km_dez = float(input("Quantos km você correu em dezembro? "))
total_corrido = atualizar_progresso(km_dez, meta_anual, total_corrido)
