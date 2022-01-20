# without function sort vowels
# a b c d e f g h i j k l m n o p q r s t u v w x y z 
x="sdafsdoiofn34sdaui"
digit_storage=[]
alpha_storage=[]
vowels=[]
      
for i in x:
       if  i.isdigit():
           digit_storage.append(i)
       else:
           alpha_storage.append(i)    
for i in x: 
    if(i == "a" or i == "e" or
           i == "i" or i == 'o' or i == "u"):
           vowels.append(i)
#print("is digit ---",digit_storage)
#print("is alpha---- ",alpha_storage)      
vowels.sort()
#vowels.reverse()
#vowels[::-1]
print("is vowels",vowels)




# 