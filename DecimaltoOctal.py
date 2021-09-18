n = 0
num = []
while n>1:
    coll = n%8
    num.append(coll)
    n = n/8
num.reverse()
print(n)
for i in num:
    print(int(i),end="") 
