import csv
import os



def bubble_sort(elemento):
    n = len(elemento)
    for i in range(n):
        for j in range(0, n-i-1):
            if elemento[j] > elemento[j+1]:
                elemento[j], elemento[j+1] = elemento[j+1], elemento[j]
                swapped = True # Add Swapped para indicar se houve troca ou não, para quando não houver troca, o loop será interrompido
                               # Reduzindo o tempo de execução do algoritmo
        if not swapped: 
            break
    return elemento

pasta_csv= "entrada.csv"
lista= []


with open(pasta_csv, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')
    for linha in leitor_csv:
        lista.append([int(x) for x in linha])

print("Lista ordenada: ", bubble_sort(lista))