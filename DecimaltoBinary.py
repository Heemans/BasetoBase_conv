n = 13
num = []
while n>1:
    collect = n%2
    num.append(collect)
    n = n/2
num.reverse()
for i in num:
    print(int(i))
