import csv
import os



def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

pasta_csv= "entrada.csv"
lista= []


with open(pasta_csv, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    for linha in leitor_csv:
        lista.append([int(x) for x in linha])

print("Lista ordenada: ", selection_sort(lista))