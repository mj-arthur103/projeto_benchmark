def bubble_sort(elemento):
    n = len(elemento)
    for i in range(n):
        for j in range(0, n-i-1):
            if elemento[j] > elemento[j+1]:
                elemento[j], elemento[j+1] = elemento[j+1], elemento[j]
    return elemento

tamanho= input()
valores= input()
lista=[int(x) for x in valores.split()]

print("Lista ordenada: ", bubble_sort(lista))