def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

arr = []
n = int(input("Tamaño de las lista: "))
for n in range(n):
    valor = input("Ingresa valor: ")
    arr.append(valor)

print("Lista ingresada antes de quicksort: ", arr)

ordenado_quick = quick_sort(arr)
print('Arreglo ordenado por QuickSort:', ordenado_quick)