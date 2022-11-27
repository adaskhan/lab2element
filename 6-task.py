def power(a, n):
    power_sum = 1
    for i in range(n):
        power_sum *= a
    return power_sum


print(power(2, 2))