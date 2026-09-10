import csv
import os

pasta_csv=r'C:\Users\arthurfreire\Desktop\dados_entrada_teste'

def heapify(arr, n, i):
    largest = i  
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  

        
        heapify(arr, n, largest)
def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

    return arr

def processo_ordenação_csv(pasta_csv):
    resultado_ordenacao = []
    for pasta_atual, subpastas, arquivos in os.walk(pasta_csv):
        for arquivo in arquivos:
            if arquivo.endswith('.csv'):
                caminho_arquivo = os.path.join(pasta_atual, arquivo)
                dados_entrada= []
                with open(caminho_arquivo, 'r') as arquivo_csv:
                    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
                    for linha in leitor_csv:
                        dados_entrada.extend([int(x) for x in linha])
                lista_ordenada = heap_sort(dados_entrada)
                print(f"Utilizado o arquivo: {arquivo}")
                print(f"Lista ordenada: {lista_ordenada}")

processo_ordenação_csv(pasta_csv)
