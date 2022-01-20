u = ["B", "D", "A", "F", "C"]

y=[]

count=0

while len(y)<len(u):

    for i in u:

        if ord(i)==count:

            y.append(i)

    count+=1

print(y)