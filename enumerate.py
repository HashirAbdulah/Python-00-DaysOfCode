# Enumerate function gives the index with the iteration values
# for example ===>  
fruits = ["apple","mango","Banana"]
for index,fruit in enumerate(fruits):
    print(f"{index} {fruit}")


number = [10,20,30]
print([(index, value) for index, value in enumerate(number)])

animals = ["cat", "dog", "lion", "tiger"]

for index, animal in enumerate(animals):
    if animal == "lion":
        print(index,animal)
        break