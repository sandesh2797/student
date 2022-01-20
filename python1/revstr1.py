import re

test_str=input("enter the string")


print("the orignal string is "+str(test_str))

temp=re.compile("([a-zA-Z]+)([0-9]+)")
res=temp.match(test_str).group()

print("after split:"+str(res))

y=reversed(str(res))
print(tuple(y))




"""
Take an input, it can be a mixture of alphaNumeric 
Segregate Numbers and alphabets
just print vowels in ascending

"""