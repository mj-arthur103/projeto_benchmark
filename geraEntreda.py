import random
import csv
import os

def sorteia(n):
    return random.randint(0, n - 1)

def troca(v, i, j):
    v[i], v[j] = v[j], v[i]

def init_vector(n):
    return list(range(1, n + 1))

def shuffle_vector(v, n, times):
    while times > 0:
        i1 = sorteia(n)
        i2 = sorteia(n)
        troca(v, i1, i2)
        times -= 1

def gerar_csv():
    entrada = input("Digite a quantidade de números que deseja no CSV: ")
    
    n = int(entrada)

    v = init_vector(n)
    shuffle_vector(v, n, 2 * n)
    
    nome_arquivo = f"dados_{n}.csv"
    
    caminho_completo = os.path.join(r'C:\Users\arthurfreire\Desktop\dados_entrada_teste', nome_arquivo)
    
    with open(caminho_completo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        for numero in v:
            escritor.writerow([numero])
            
    print(f"Foi gerado: '{nome_arquivo}', com: {n}")

gerar_csv()