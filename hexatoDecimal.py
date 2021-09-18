conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hexadecimal = input("Enter the hexadecimal number: ").upper()
decimal = 0
power = len(hexadecimal) -1
for digit in hexadecimal:
    decimal += conversion_table[digit]*16**power
    power -= 1
    
print(decimal)
