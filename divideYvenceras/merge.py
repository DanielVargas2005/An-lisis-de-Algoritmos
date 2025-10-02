def merge_sort(arr):
    # Condición de parada: si tiene 1 o 0 elementos, ya está "ordenado"
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamadas recursivas para dividir
        merge_sort(left_half)
        merge_sort(right_half)

        # Función de mezcla y ordenación
        merge(arr, left_half, right_half)
    
    # Se retorna el array modificado (aunque en Python el cambio es in-place dentro del array original que se pasa como argumento)
    return arr

def merge(arr, left_half, right_half):
    i = j = k = 0

    # Copia los datos a los arrays temporales left_half[] y right_half[]
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Comprobación de si quedan elementos en left_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    # Comprobación de si quedan elementos en right_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

arr = []
n = int(input("Tamaño de las lista: "))
for n in range(n):
    valor = input("Ingresa valor: ")
    arr.append(valor)

print("Lista ingresada antes de mergesort: ", arr)

ordenado_merge = merge_sort(arr)
print('Arreglo ordenado por MergeSort:', ordenado_merge)