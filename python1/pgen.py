import random
def passwordGenerator() :     # def func
      lower='abcdefghijklmnopqrstuvyxyz'
      upper ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      number = '0123456789'
      sp = "!@#$%^&*()"
      password=random.choice(lower)+random.choice(upper)+random.choice(number)+random.choice(sp)
      password=password*1
      return password
p=passwordGenerator();
print('Password is ::     ', p)    
