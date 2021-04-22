# function to merge dict using update() method
def Merge(dict1, dict2):
    return(dict2.update(dict1))
     
# Dictonaries
dict1 = {'Name': 'Aishwarya', 'Surname': 'Mulkipatil'}
dict2 = {'College': 'KLE', 'CGPA': 8.9}
 
#Calling Merge function to merge two dictonaries
Merge(dict1, dict2)
 
# It prints changes made in dict2
print(dict2)