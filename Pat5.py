original = [1, 2, 3, 4, 5, 6]
even = [x for x in original if x % 2 == 0]
odd = [x for x in original if x % 2 != 0]
print(even)
print(odd)