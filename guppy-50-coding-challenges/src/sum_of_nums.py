# Calculate the sum of numbers from 1 to 10

# hard way
result = sum(range(1, 11))
print(result)
# "for" way
result = 0
for i in range(1, 11):
    result += i
print(result)
# labmda way
result = 0
result = sum(list(map(lambda x: x, range(1, 11))))
print(result)