num1=int(input("enter the number "))

if num1>1:
    for i in range(2,int(num1/2)+1):
        if (num1%i)==0:
            print(num1,"it is not prime")
        break
    else:
        print("it is prime",num1)  
else:
    print("it is mot prime number",num1)          