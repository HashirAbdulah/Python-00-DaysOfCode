letter = "my name is {} and living in {}"
name = "Hashir"
country = "Pakistan"
print(letter.format(name,country))
# lengthy + not optimized,may cause bugs while for lengthy code
# so we use "F-String (f'(string inside with {argument1} .... {argument2},......)')" 

# for literal printing (Same as the given string we use double {} brackets on the argument)
print(f"Hy, My name is {{name}}, I'm {{age}} old,and living in {{city}}, {{country}},currently working at {{work_place}}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
country = input("Enter you country: ")
work_place = input("Enter your JobPlace: ")
print(f"Hy, My name is {name}, I'm {age} old,and living in {city}, {country},currently working at {work_place}")

print(f"{2*30}")