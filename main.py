from random import randint
el = 10
arr = []
for i in range(el):
    arr.append(randint(-20,20))
print("Элементы:"+str(arr))
for i in range(el):
    for j in range(el - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Сортировка:"+str(arr))
