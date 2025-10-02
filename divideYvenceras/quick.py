def quick_sort(arr):
    # Caso base: listas de 0 o 1 elementos ya están ordenadas
    if len(arr) <= 1:
        return arr

    # Selecciona el pivote (aquí usamos el elemento central)
    pivot = arr[len(arr) // 2]

    # Elementos menores al pivote
    left = [x for x in arr if x < pivot]
    # Elementos iguales al pivote
    middle = [x for x in arr if x == pivot]
    # Elementos mayores al pivote
    right = [x for x in arr if x > pivot]

    # Llamadas recursivas
    return quick_sort(left) + middle + quick_sort(right)

arr = []
n = int(input("Tamaño de las lista: "))
for n in range(n):
    valor = input("Ingresa valor: ")
    arr.append(valor)

print("Lista ingresada antes de quicksort: ", arr)

ordenado_quick = quick_sort(arr)
print('Arreglo ordenado por QuickSort:', ordenado_quick)