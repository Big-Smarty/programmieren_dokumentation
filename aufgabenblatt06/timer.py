from random import randint
from time import process_time_ns

numbers1 = [randint(0, 999) for i in range(1000)]

numbers2 = [randint(0, 999) for i in range(100000)]

numbers3 = [randint(0, 999) for i in range(10000000)]

start = process_time_ns()
numbers1 = sorted(numbers1)
end = process_time_ns()
print("Benötigte Zeit bei 1000 Elementen:" + str(end - start))

start = process_time_ns()
numbers2 = sorted(numbers2)
end = process_time_ns()
print("Benötigte Zeit bei 100000 Elementen:" + str(end - start))

start = process_time_ns()
numbers3 = sorted(numbers3)
end = process_time_ns()
print("Benötigte Zeit bei 10000000 Elementen:" + str(end - start))
