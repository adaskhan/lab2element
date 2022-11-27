def election(x, y, z):
    o_count = [x, y, z].count(1)
    return 1 if o_count > 1 else 0


print(election(0, 0, 1))
print(election(1, 0, 1))
print(election(0, 0, 0))
print(election(1, 1, 1))
