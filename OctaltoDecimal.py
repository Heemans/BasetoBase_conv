octal = 24
decimal = 0
l = len(str(octal))
for x in str(octal):
    l = l-1                        
    decimal = decimal + pow(8,l) * int(x)   
    
print(decimal)
