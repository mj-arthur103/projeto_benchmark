import bisect
import csv
import os

#Insertion V2, utilizamos o bisect para fazer uma busca na base binária, para alterar a posição, caso necessário
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        pos = bisect.bisect_right(arr, key, 0, i)
        arr.insert(pos, arr.pop(i)) #Remove o elemento na posição atual e adiciona na posição correta
    return arr

pasta_csv= "entrada.csv"
lista= []


with open(pasta_csv, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    for linha in leitor_csv:
        lista.append([int(x) for x in linha])

print("Lista ordenada: ", insertion_sort(lista))