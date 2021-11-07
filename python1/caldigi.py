#Write a Python program that accepts a string and calculate the number of digits and letters.

str1=input("enter the string  ")

count_digit=0
count_letter=0

for i in str1:
    if i.isdigit():
       count_digit=+1
    elif i.isalpha():
        count_letter=+1
    else:
        pass
        print('digit is '  ,count_digit)
        print('leter is  ' ,count_letter)  


