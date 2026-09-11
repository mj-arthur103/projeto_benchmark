import csv
import os

pasta_csv=r'..\dados_entrada_gerados'

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
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
                lista_ordenada = selection_sort(dados_entrada)
                print(f"Utilizado o arquivo: {arquivo}")
                print(f"Lista ordenada: {lista_ordenada}")

processo_ordenação_csv(pasta_csv)
