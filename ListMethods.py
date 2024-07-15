list = [1,2,3,4,5,6]
print(list)
# Append method: Add a elements at the last index of a List 
list.append(7)
print("Appended list:",list)

# Sort method: Sorts the element of the List in ascending order
list1 = [1,7,3,4,6,0,2]
print(list1)
list1.sort()
print("Ascending Sorted List:",list1)

# Sort(reverse = True) method: Sorts the element of the List in Descending order
list2 = [1,7,3,4,6,0,2]
print(list2)
list2.sort(reverse=True)
print("Descending Sorted List",list2)

# Reverse method: Reverse the elements of the list
list3 = [1,2,3,4,5,6]
list3.reverse()
print("Reversed List: ",list3)

# Insert method : Element insertion at specific Index
list4 = [1,2,3,4,5,6]
list4.insert(1,7)
print("After Insertion List:",list4)

