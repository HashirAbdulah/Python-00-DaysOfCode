# Sets in Python is ( Well defined objects ){Do not take repeated values} it is created by "{}" curly brackets
# For Example {2,5,6,6,6,7,8,9,0,0,1,5}
# output will be = {0, 1, 2, 5, 6, 7, 8, 9}
# It Doesnt maintain the order
# it doesnt change


set_var = {2, 5, 6, 6, 6, 7, 8, 9, 0, 0, 1, 5}
print(set_var)

value = {False, "Carlo",19,5.1,19}
for char in value:
    print(char)

hashir = {}
print(type(hashir)) 
# As dictionary is also initialize by {} brackets so the answer will be class dict

# For empty set we use 
hashir = set()
print(type(hashir)) 