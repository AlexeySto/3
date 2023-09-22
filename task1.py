# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

list1 = []
list2 = []

n = 0
while n < 1:
    n = int(input("Введите длинну первого множества: "))
for i in range(n):
    list1.append(int(input(f"Введите {i} член множества: ")))

m = 0
while m < 1:
    m = int(input("Введите длинну первого множества: "))
for i in range(m):
    list2.append(int(input(f"Введите {i} член множества: ")))

print(list1)
print(list2)

setResult = set(list1) | set(list2)
listResult = []
for i in setResult:
    listResult.append(i)

for i in range(len(listResult) - 1):
    for j in range(len(listResult) - i - 1):
        if listResult[j] > listResult[j + 1]:
            temp = listResult[j + 1]
            listResult[j + 1] = listResult[j]
            listResult[j] = temp

print(listResult)
