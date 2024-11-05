def fibonacci(x):
    if (x == 1) or (x == 2):
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)


for i in range(3, 24, 1):
    print(
        "f_"
        + str(i)
        + " = "
        + str(fibonacci(i))
        + " "
        + str(fibonacci(i) / fibonacci(i - 1))
    )
