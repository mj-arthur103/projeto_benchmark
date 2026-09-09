import csv
import os



def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

pasta_csv= "entrada.csv"
lista= []


with open(pasta_csv, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    for linha in leitor_csv:
        lista.append([int(x) for x in linha])

print("Lista ordenada: ", insertion_sort(lista))