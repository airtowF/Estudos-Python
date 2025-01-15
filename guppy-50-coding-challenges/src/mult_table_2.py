# Print all the multiplication tables with numbers from 1 to 10 side by side
for i in range(1, 11):
    for j in range(11):
        print("{} * {} = {}".format(i, j, i*j))
print("------------------")
# meanwhile using list comprehension isn't easy
[[print("{} * {} = {}".format(i, j, i*j)) for j in range(11)] for i in range(1, 11)]