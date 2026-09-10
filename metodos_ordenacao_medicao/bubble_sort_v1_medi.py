import csv
import os
import time
import psutil

pasta_csv=r'C:\Users\arthurfreire\Desktop\dados_entrada_teste'

def bubble_sort(elemento):
    n = len(elemento)
    for i in range(n):
        for j in range(0, n-i-1):
            if elemento[j] > elemento[j+1]:
                elemento[j], elemento[j+1] = elemento[j+1], elemento[j]
    return elemento

def processo_ordenação_csv(pasta_csv):
    for pasta_atual, _, arquivos in os.walk(pasta_csv):
        for arquivo in arquivos:
            if arquivo.endswith('.csv'):
                caminho_arquivo = os.path.join(pasta_atual, arquivo)
                dados_entrada= []
                with open(caminho_arquivo, 'r') as arquivo_csv:
                    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
                    for linha in leitor_csv:
                        dados_entrada.extend([int(x) for x in linha])
                tempo_duration_inicio = time.perf_counter()#Inicia a contagem do tempo de duração
                tempo_cpu_inicio = psutil.cpu_times() #Inicia a contagem do tempo de CPU

                lista_ordenada = bubble_sort(dados_entrada)

                tempo_duration_fim = time.perf_counter()#Finaliza a contagem do tempo de duração
                tempo_cpu_fim = psutil.cpu_times()#Finaliza a contagem do tempo de CPU

                duration_time = tempo_duration_fim - tempo_duration_inicio #Calcula o tempo de duração real
                user_time = tempo_cpu_fim.user - tempo_cpu_inicio.user #Calcula o tempo de CPU gasto em modo usuário
                system_time = tempo_cpu_fim.system - tempo_cpu_inicio.system #Calcula o tempo de CPU gasto em modo sistema

                print(f"Utilizado o arquivo: {arquivo}")
                print(f"Lista ordenada: {lista_ordenada}")
                print(f"Tempo de duração: {duration_time:.6f} segundos")
                print(f"Tempo do usuário: {user_time:.6f} segundos")
                print(f"Tempo do sistema: {system_time:.6f} segundos")
                print(f"Tempo de CPU: {(user_time + system_time):.6f} segundos\n")
processo_ordenação_csv(pasta_csv)