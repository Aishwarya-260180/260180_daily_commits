set1 = []
# number of elemetns as input
n = int(input("Enter number of elements : "))
print("ENTER NUMBERS OF SET:")
# iterating till the range
for i in range(0, n):
        ele = int(input())
        set1.append(ele)
print("MAXIMUM VALUE IN THE SET IS",max(set1))
print("MINIMUM VALUE IN THE SET IS",min(set1))
