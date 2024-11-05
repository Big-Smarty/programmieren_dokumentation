import random


def bubble_sort(x):
    while True:
        possibly_sorted = True
        for i in range(0, len(x), 1):
            temp = 0
            if i < len(x) - 1:
                if x[i] > x[i + 1]:
                    possibly_sorted = False
                    temp = x[i]
                    x[i] = x[i + 1]
                    x[i + 1] = temp
        if possibly_sorted:
            return x


random.seed()
numbers = [random.randint(0, 999) for i in range(10)]
print("Unsorted:")
for i in numbers:
    print(i)
print("Sorted:")
for i in bubble_sort(numbers):
    print(i)
