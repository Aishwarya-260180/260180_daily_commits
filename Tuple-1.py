values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)

rep = []
for t in tuple:
     found = 0
     for r in rep:
          if(r[0] == t):
               r[1] += 1
               found = 1
               break
     
     if(not found):
        rep.append([t, 1])

num = 0
count = 0
for r in rep:
     if(r[1] > count):
         count = r[1]
         num = r[0]

if(count > 1):
    print("Repeated number : " + str(num) + " Repeat times : " + str(count))
else:
    print("No number repeated!")
