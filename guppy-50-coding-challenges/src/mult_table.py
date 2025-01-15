# Print the multiplication table with 7
count = 0

while count <= 10:
    print("7 * {} = {}".format(count, 7*count))
    count += 1
# -----------
# Using list comprehension again to practice
[print("7 * {} = {}".format(x, 7*x)) for x in range(11)]