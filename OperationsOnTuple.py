tupple = ("Pakistan","Palestine","Canada","India","Banglasdesh")
print(tupple)
temp_list = list(tupple)  
print("Converted Tuple in List:",temp_list)
# convert tuple into list
temp_list.append("Australia")
tupple = tuple(temp_list)
# convert list into tuple
print(tupple)

# First change the tuple to list then add element at the end then change the list again to tuple

# Concatination of tuples:
tuple1 = ("Pakistan","Palestine","Canada")
tuple2 = ("America","UAE","England")
tuple3 = ("Iran","Sharjah","Bangladesh")
concatinatedTuple = tuple1 + tuple2 + tuple3
print(concatinatedTuple)


# Count Method : Counts the Occurance of the element
tpl = (1,1,1,4,5,6,8,9,3,3,3,5)
res = tpl.count(3)
print(res)

# Index Method: Give the element first occurance of the Particular element in ()

res2 = tpl.index(5)
print(res2)

# Len Method : Gives the Length of the Tuple
res3 = len(tpl)
print(res3)

# You can use every list method on tuple by converting the tuple to the list