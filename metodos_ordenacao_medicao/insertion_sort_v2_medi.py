import bisect #Biblioteca para realizar a busca binária para encontrar a posição correta do elemento a ser inserido
import csv
import os
import time
import psutil

diretorio_script = os.path.dirname(os.path.abspath(__file__)) #Indetifica o diretório para referenciar o caminho relativo do arquivo CSV ("Provavel solução para não está entrando no os.walk()")
pasta_csv = os.path.join(diretorio_script, '..', 'dados_entrada_gerados')


#Insertion V2, utilizamos o bisect para fazer uma busca na base binária, para alterar a posição, caso necessário
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        pos = bisect.bisect_right(arr, key, 0, i)
        arr.insert(pos, arr.pop(i)) #Remove o elemento na posição atual e adiciona na posição correta
    return arr

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

                lista_ordenada = insertion_sort(dados_entrada)

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
