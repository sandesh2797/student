# take word from user and reverse it

str(input("enter the word   "))

word=str.split('')

print(word)
word=word[-1::-1]
print(word)
outputstr=''.join(word)

print(outputstr)