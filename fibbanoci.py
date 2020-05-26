def fibanocci(n):
   if n<0:
     print("Incorrect input")
   elif n==1:
     return 0
   elif n==2:
     return 1
   else:
     return fibanocci(n-1)+fibanocci(n-2)
    
print(fibanocci(9))

