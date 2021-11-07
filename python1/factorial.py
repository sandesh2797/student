num2=int(input("enter the number  "))
fact=1
if num2<0:
    print("sorry no negative number try..positive number ")
elif num2==0:
    print("0 factorial is 1")

else:
    for i in range(1,num2+1):
        fact=fact*i
    print("factorial is ",fact)    