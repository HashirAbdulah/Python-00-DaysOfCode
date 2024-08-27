tup = (1,2,4,6,"English",True,)
print(type(tup))
for i in range(0,len(tup)):
    print(tup[i])
    
    # Tuples are same as Lists(Arrays) but are immutable and can not be changed
    # Tuples can only be changed ,adding,removing only after converting into list and then again for secure lists change into tuple

#  legal way to turn this tuple: (1,2,3) into this tuple:(1,2,3,1,2,3)?
tuple1 = (1,2,3)
tuple1 = tuple1 * 2
print(tuple1)
