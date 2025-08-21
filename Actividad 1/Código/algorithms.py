import random

def linear_search(list, x):
    for index, value in enumerate(list):
        if value == x:
            return index
    return -1

def binary_search(list, x):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == x:
            return mid
        elif list[mid] < x:
            low = mid + 1  
        else:
            high = mid - 1  
    return -1  


def generate_data(num_data):
    data_list = random.sample(range(1, (num_data + 1) * 10), num_data)
    return data_list