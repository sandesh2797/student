#file open usin file handling
f=open('template.txt',mode='r')

#create one list 
days=['monday','tuesday','wed','thrus','fri','sat','sunday']
temps=[]
for i in f:
    temps.append(float(i[:-1]))
temps_dict=dict(zip(days,temps))    
print(temps_dict)

def day_wise():
    '''this is function for day wise'''
    for temp in temps_dict:
        print(f"{temp} --->  {temps_dict[temp]}")
#day_wise()

def avg():
    z=0
    for temp in temps:
        z=z+temp
        return z/len(days)
    print(avg())    
    #return avg      

def min1():
    '''this function shows minimum temp'''
    min1=temps_dict['monday']
    day='monday'
    for temp in temps_dict:
        if temps_dict[temp]<min1:
            min1=temps_dict[temp]
            day=temp
    return min1,day        



def max2():
    '''this function shows max temp'''
    max2=temps_dict['monday']
    day='monday'
    for temp in temps_dict:
        if temps_dict[temp]>max2:
            max2=temps_dict[temp]
            day=temp
    return max2,day          
    

    
def below_zero():
        print("this function shows belo zero temp")
        for temp in temps_dict:
            if temps_dict[temp]<=0:
                print(temp)
def sep_temps():
    sep=float(input("enter the temp for sepration"))
    below_sep=[]
    above_sep=[]
    for temp in temps_dict:
        if temps_dict[temp]<sep:
            below_sep.append(temp)
        else:
            above_sep.append(temp)
        print("days having temp below",sep)
        for t in below_sep:
            print(t)
        print("days having above temp",sep)
        for t in above_sep:
            print(t)            

    
            

while True:
    print("select the following :")
    print("1. show dayswise temp\n 2.show avg of all temp\n 3.show minimum temp\n 4. show max temp\n 5.show days havin below 0 temp\n 6.show days using seprator")

    ch=int(input("enter the choice"))
    if ch==1:
        day_wise()
    elif ch==2:
        print("average of temp is ",avg())
    elif ch==3:
        minimum=min1()
        print(f"minimum temp is {minimum[0]} for day {minimum[1]}")
    elif ch==4:
        minimum=max2()
        print(f"maximum temp is {maximum[0]} for day {maximum[1]}")
    elif ch==5:
        below_zero()
    elif ch==6:
        sep_temps()
    else:
        print("invalid choise")
    ans=input("do you want to contineu (y/n)" ).lower()
    if ans!='y':
        break



f.close()

