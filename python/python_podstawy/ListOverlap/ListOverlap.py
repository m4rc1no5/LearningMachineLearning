from random import *

a = [int(element*random()*10) for element in range(1, 100)]
b = [int(element*random()*10) for element in range(1, 100)]

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 34, 456, 21]

c = []

for element in a:
	if element in b and element not in c:
		c.append(element)

print([element for element in a if element in b and element not in c c.append(element)])

print(c)
