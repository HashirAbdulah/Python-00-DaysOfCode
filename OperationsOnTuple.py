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