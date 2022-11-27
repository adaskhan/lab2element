decimal_number = 0
binary_number = input()
for i in range(len(binary_number)):
    decimal_number += int(binary_number[i])*(2 ** i)
print(decimal_number)
