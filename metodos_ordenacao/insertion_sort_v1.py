def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

tamanho= input()
valores= input()
lista=[int(x) for x in valores.split()]
print("Lista ordenada: ", insertion_sort(lista))