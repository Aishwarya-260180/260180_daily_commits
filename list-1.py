def find_len(list1):
    
    list1.sort()
    
    print("Second Smallest element is:", list1[1])
  
if __name__=="__main__":
    list1 = []
# number of elemetns as input
    n = int(input("Enter number of elements : "))
# iterating till the range
    for i in range(0, n):
        ele = int(input())
        list1.append(ele)
    find_len(list1)
