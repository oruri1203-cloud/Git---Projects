import math

num = int(input("Enter a positive number: "))
bits = int(input("Enter number of bits: "))

def ToBinary(num, bits):
    numlist = ['0'] * bits
    for i in range(bits):
        power = bits - 1 - i
        if num >= 2 ** power:
            numlist[i] = '1'
            num -= 2 ** power
        else:
            numlist[i] = '0'
    return numlist

def OnesComplement(numlist):
    complemented = []
    for bit in numlist:
        if bit == '1':
            complemented.append('0')
        else:
            complemented.append('1')
    return complemented

def TwosComplement(numlist):
    ones = OnesComplement(numlist)
    bits = len(ones)
    result = ['0'] * bits
    carry = 1
    for i in range(bits - 1, -1, -1):
        if ones[i] == '1' and carry == 1:
            result[i] = '0'
            carry = 1
        elif ones[i] == '0' and carry == 1:
            result[i] = '1'
            carry = 0
        else:
            result[i] = ones[i]
    return result

# הפעלת הפונקציות
binary = ToBinary(num, bits)
ones = OnesComplement(binary)
twos = TwosComplement(binary)

# הצגת התוצאות
print("Binary:", ''.join(binary))
print("One's Complement:", ''.join(ones))
print("Two's Complement:", ''.join(twos))
