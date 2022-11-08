#Converting decimal number into binary string
def decimal_binary(num,bits):
    binary_num = ""
    pad = 0

    while num:
        binary_num = str(num%2) +binary_num
        num = int(num/2)
        pad = pad + 1

    return "0"*(bits-pad) +binary_num

#Flipping The Sign of The Number
def sign_change(num1):
    num1  = '1'+num1[1:] if num1[0] == '0' else '0'+num1[1:]
    return(num1)

#Finding The Absolute Value of a Number
def modulo(num):
    num = '0'+num[1:]
    return num

#Finding The Sum of Given Numbers
def Sum(num1,num2,bits):
    NUM1 = int(num1[1:],2) if num1[0] =='0' else (-1)*int(num1[1:],2)
    NUM2 = int(num2[1:],2) if num2[0] =='0' else (-1)*int(num2[1:],2)

    SUM = NUM1 + NUM2
    if SUM < 0:
        return '1' + decimal_binary((-1)*SUM,bits-1)
    else :
        return '0' + decimal_binary(SUM,bits-1)

#Finding the difference of Given Numbers
def Sub(num1,num2,bits):
    NUM1 = int(num1[1:],2) if num1[0] =='0' else (-1)*int(num1[1:],2)
    NUM2 = int(num2[1:],2) if num2[0] =='0' else (-1)*int(num2[1:],2)

    DIFF = NUM1 - NUM2
    if DIFF < 0:
        return '1' + decimal_binary((-1)*DIFF,bits-1)
    else :
        return '0' + decimal_binary(DIFF,bits-1)

#Finding the product of Given Numbers
def Mul(num1,num2,bits):
    NUM1 = int(num1[1:],2) if num1[0] =='0' else (-1)*int(num1[1:],2)
    NUM2 = int(num2[1:],2) if num2[0] =='0' else (-1)*int(num2[1:],2)

    PROD = NUM1*NUM2

    if PROD < 0:
        PROD =  '1' + decimal_binary((-1)*PROD,bits-1)
    else :
        PROD =  '0' + decimal_binary(PROD,bits-1)

    return PROD[:40],PROD[40:]

#Finding the quotient and remainder of Given Numbers
def Div(num1,num2,bits):
    NUM1 = int(num1[1:],2) if num1[0] =='0' else (-1)*int(num1[1:],2)
    NUM2 = int(num2[1:],2) if num2[0] =='0' else (-1)*int(num2[1:],2)

    QUOT = int(NUM1/NUM2)

    if QUOT < 0:
        QUOT =  '1' + decimal_binary((-1)*QUOT,bits-1)
    else :
        QUOT =  '0' + decimal_binary(QUOT,bits-1)

    REMA = NUM1%NUM2
    
    if REMA < 0:
        REMA =  '1' + decimal_binary((-1)*REMA,bits-1)
    else :
        REMA =  '0' + decimal_binary(REMA,bits-1)

    return REMA,QUOT

#Left Shifts the given number 
def LeftShift(num):
    bits = len(num)

    NUM = int(num[1:],2) if num[0] == '0' else (-1)*int(num[1:],2)
    ANS = NUM << 1

    if ANS<0:
        return '1'+decimal_binary((-1)*ANS,bits-1)
    else :
        return '0'+decimal_binary(ANS,bits-1)

#Right Shifts the given number
def RightSHift(num):
    bits = len(num)

    NUM = int(num[1:],2) if num[0] == '0' else (-1)*int(num[1:],2)
    ANS = NUM >> 1

    if ANS<0:
        return '1'+decimal_binary(int((-1)*ANS,2),bits-1)
    else :
        return '0'+decimal_binary(int(ANS,2),bits-1)
