number=(4,3,55,6,7,8,9,0,77,5,4,34,88,99,24)

count_even=0
count_odd=0

for i in number:
   
        if not i%2:
            count_even+=1
        else:
                count_odd+=1

print("no of even is ",count_even)
print("no of odd is ",count_odd)


