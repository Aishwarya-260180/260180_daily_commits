#initializing lists
test_list1 = ["Details", 'College', 'Average']
test_list2 = ['Name', 'College_Name', 'CGPA']
test_list3 = ['Aishwarya', 'KLEIT', 8.9]
  
# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
print("The original list 3 is : " + str(test_list3))
  
# Convert Lists to Nestings Dictionary
# Using list comprehension + zip()
res = [{a: {b: c}} for (a, b, c) in zip(test_list1, test_list2, test_list3)]
  
# printing Dictionary
print("The constructed dictionary : " + str(res)) 
