n=int(input("HOW MANY PIZZA SLICES DO YOU NEED:"))
if(n>0):
 if(n%2==0):
    s=n*120.00
    print("TOTAL PRICE IS:",s)
 else:
    s=n*123.00
    print("TOTAL PRICE IS:",s)
else:
  print("INVALID NUMBER")

