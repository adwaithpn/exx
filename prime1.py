i=int(input("enter the lower limit :"))
u=int(input("enter the upper limit :"))
for num in range(i,u+1):
   if num > 1:
       for i in range(2,num):
           if (num%i) == 0:
               break
       else:
           print(num)
