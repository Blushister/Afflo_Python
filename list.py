import random


def generate_list():
    a = []
    for i in range(1, 101):
        a.append(random.randint(0, 10000))
    return a


def sort_list(a):
    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a


a = generate_list()
print(a)
i = 0
max = a[i]
for i in range(0, len(a)):
    if a[i] > max:
        max = a[i]
        temp1 = i

print(max)
sort_list(a)
print(a)
print(type(True))
