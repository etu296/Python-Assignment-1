# 10.Python Program to Reverse a String in Multiple Ways
text = "Python"
# using slicing
print("Reversed text using slicing:", text[::-1])

#using for loop
reversed_number = ""
for char in text:
    reversed_number = char + reversed_number
print("Reversed text using loop:", reversed_number)

#Using reversed function
text1 = "Hello"
reversed_text1 = ''.join(reversed(text1))
print("Reversed (reversed() function):", reversed_text1)

# 11.Python Program to Find the Largest Element in a List
# 12.Python Program to Find the Smallest Element in a List
list1 = [1,11,2,2,3,5,4,44,55]
largest = max(list1)
minimum = min(list1)
print("Largest:", largest)
print("Minimum:", minimum)

# 13.Python Program to Sort a List in Ascending Order
print("list in ascending order:", sorted(list1))
# 14.Python Program to Sort a List in Descending Order
print("list in descending order:", sorted(list1, reverse=True))
# 15.Python Program to Find the Sum of Elements in a List
print("sum of the elements in list1:", sum(list1))
# 16.Python Program to Multiply All Elements in a List
item = 1
for num in list1:
    item *= num
print("multiplication of the elements in list1:", item)
# 17.Python Program to Remove Duplicates from a List
unique_list = list(set(list1))
print("list without duplicate value:", unique_list)
List2=[1,1,2,3,3,4]
unique_list1 = list(dict.fromkeys(List2))
print("list without duplicate value using fromkeys:", unique_list1)

# 18.Python Program to Find the Second Largest Element in a List
list3 = [11,32,22,44,54,34,98]
sorted_list = sorted(list3)
print("sorted list:", sorted_list)
print("2nd largest number from the list3:", sorted_list[-2])
# 19.Python Program to Find the Intersection of Two Lists
List4=[1,22,8,9,10,11,12,13,14,54]
intersection = list(set(List4).intersection(list3))
print("intersection list:", intersection)
# 20. Python Program to Find the Union of Two Lists
union = list(set(List4).union(list3))
print("union list:", union)
