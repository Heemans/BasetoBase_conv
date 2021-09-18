binary = 1101
decimal = 0
l = len(str(binary))
for x in str(binary):
    l = l-1                        
    decimal = decimal + pow(2,l) * int(x)   
    
print(decimal)
