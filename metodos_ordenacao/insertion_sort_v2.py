import bisect
import csv
import os

pasta_csv=r'C:\Users\arthurfreire\Desktop\dados_entrada_teste'

#Insertion V2, utilizamos o bisect para fazer uma busca na base binária, para alterar a posição, caso necessário
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        pos = bisect.bisect_right(arr, key, 0, i)
        arr.insert(pos, arr.pop(i)) #Remove o elemento na posição atual e adiciona na posição correta
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
