import csv
import os

pasta_csv=r'C:\Users\arthurfreire\Desktop\dados_entrada_teste'

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def processo_ordenação_csv(pasta_csv):
    for pasta_atual, subpastas, arquivos in os.walk(pasta_csv):
        for arquivo in arquivos:
            if arquivo.endswith('.csv'):
                caminho_arquivo = os.path.join(pasta_atual, arquivo)
                dados_entrada= []
                with open(caminho_arquivo, 'r') as arquivo_csv:
                    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
                    for linha in leitor_csv:
                        dados_entrada.extend([int(x) for x in linha])
                lista_ordenada = insertion_sort(dados_entrada)
                print(f"Utilizado o arquivo: {arquivo}")
    return lista_ordenada

print("Lista ordenada: ", processo_ordenação_csv(pasta_csv))
