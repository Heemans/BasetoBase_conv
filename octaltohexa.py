# octal to hexadecimal
# octal to decimal than decimal to hexa

octal = 26
print("Octal no is "+str(octal))
decimal = 0
l = len(str(octal))
for x in str(octal):
    l = l-1                        
    decimal = decimal + pow(8,l) * int(x)   
    
print("Octal to decimal is "+str(decimal))

hexaDeciNum = ['0'] * 100
i = 0
while(decimal != 0):
    temp = 0
    temp = decimal % 16
    if(temp < 10):
        hexaDeciNum[i] = chr(temp + 48)
        i = i + 1
    else:
        hexaDeciNum[i] = chr(temp + 55)
        i = i + 1
    decimal = int(decimal / 16)
j = i - 1
print("Octal to hexadecimal is ")
while(j >= 0):
    print((hexaDeciNum[j]), end="")
    j = j - 1
