year=(int(input("enter the year  ")))

if (year%4)==0:
    if (year%100)==0:
        if(year%400)==0:
            print("is leap year",year)
        else:
                print("is not lea[ year",year)
    else: 
            print("is leap year",year)

else:
            print("is not leap year",year)            