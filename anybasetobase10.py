base = int(input("Enter base no to convert to base 10 "))

if base == 2:
    no = int(input("Enter binary no to convert to decimal no "))
    decimal = 0
    l = len(str(no))
    for x in str(no):
        l = l-1                        
        decimal = decimal + pow(2,l) * int(x)   
    print(decimal)

if base == 8:
    no1 = int(input("Enter octal no to convert to decimal no "))
    decimal = 0
    l = len(str(no1))
    for x in str(no1):
        l = l-1                        
        decimal = decimal + pow(8,l) * int(x)   
    print(decimal)

if base == 16:
    no2 = input("Enter hexadecimal no to convert to decimal no ").upper()
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    l = len(no2) -1
    for digit in no2:
        decimal += conversion_table[digit]*16**l
        l -= 1
    print(decimal)
