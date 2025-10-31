numbers = [5, 12, 7, 3, 9, 21, 4]

print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))

numbers.append(15)
print(numbers)

numbers.insert(2, 99)
print(numbers)

numbers.remove(99)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(21))
print(numbers.count(7))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)