# Checking numbers of zeros
a = (7,0,8,0,0,9)
count = 0
for i in a:
    if i == 0:
        count = count+1

print(count)



# Giving students numbers + sorting
array = []

for i in range(7):
    marks = int(input(f"Enter marks of the students {i+1}:"))
    array.append(marks)

array.sort()

print("Sorted array in ascending order:", array)


# Sum of adjecent elements
numbers = [1, 2, 3, 4]
total = 0
for num in numbers:
    total += num

print(total)


