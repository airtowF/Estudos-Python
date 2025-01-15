# Calculate the sum of numbers in an array of numbers
def sum_array(arr):
    return sum(arr)

list1 = [1, 2, 3, 4, 5]
print(sum_array(list1))

# learning *args
def sum_array(*args):
    return sum(args)

print(sum_array(1, 2, 3, 4, 5))

# using kwarg to solve it would be funny
def sum_array(**kwargs):
    return sum(kwargs.values())

print(sum_array(a=1, b=2, c=3, d=4, e=5))
