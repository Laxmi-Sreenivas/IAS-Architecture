import ALU

#Finding the sum of accumalator and given memory location
def Add_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Add M(X) to AC; put the result in AC")
    print(" "*5+"Present Value of Accumalator = "+AC)

    MBR = Main_Memory[int(MAR,2)]
    AC = ALU.Sum(AC,MBR,40)

    print(" "*5+"MBR = ",MBR," M(X) = "+Main_Memory[int(MAR,2)]+" AC = "+AC)    
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Finding the sum of accumalator and modulus of given memory location
def Add_mod_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Add M(X) to AC; put the result in AC")
    print(" "*5+"Present Value of Accumalator = "+AC)

    MBR = Main_Memory[int(MAR,2)]
    AC = ALU.Sum(AC,ALU.modulo(MBR),40)

    print(" "*5+"MBR = ",MBR," M(X) = "+Main_Memory[int(MAR,2)]+" AC = "+AC)  
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Subtract M(X) From AC
def Sub_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Subtract M(X) from AC; put the result in AC")
    print(" "*5+"Present Value of Accumalator = "+AC)

    MBR = Main_Memory[int(MAR,2)]
    AC = ALU.Sub(AC,MBR,40)

    print(" "*5+"MBR = ",MBR," M(X) = "+Main_Memory[int(MAR,2)]+" AC = "+AC)   
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Subtract |M(X)| From AC
def Sub_mod_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Subtract M(X) from AC; put the result in AC")
    print(" "*5+"Present Value of Accumalator = "+AC)

    MBR = Main_Memory[int(MAR,2)]
    AC = ALU.Sub(AC,ALU.modulo(MBR),40)

    print(" "*5+"MBR = ",MBR," M(X) = "+Main_Memory[int(MAR,2)]+" AC = "+AC)   
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Product of MQ and M(X)
def Mul_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Multiply M(X) by MQ, AC = MSB and MQ = LSB")
    print(" "*5+"Present Values of Accumalator and MQ,AC = ",AC," MQ = ",MQ)

    MBR   = Main_Memory[int(MAR,2)]
    AC,MQ = ALU.Mul(MQ,MBR,80)

    print(" "*5+"MBR = ",MBR," M(X) = "+Main_Memory[int(MAR,2)]+" AC = "+AC," MQ = "+MQ)   
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Division of AC and M(X)
def Div_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Divide AC by M(X), AC = MSB and MQ = LSB")
    print(" "*5+"Present Values of Accumalator and MQ,AC = ",AC," MQ = ",MQ)

    MBR   = Main_Memory[int(MAR,2)]
    AC,MQ = ALU.Div(AC,MBR,40)

    print(" "*5+"MBR = ",MBR," M(X) = "+Main_Memory[int(MAR,2)]+" AC = "+AC," MQ = "+MQ)   
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Left Shifting The value in accumalator by 1 bit
def LSH(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Shift Left 1 bit position of AC")
    print(" "*5+"Present Value of Accumalotor AC = "+AC)

    AC = ALU.LeftShift(AC)

    print(" "*5+"AC = "+AC)
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Right Shifting The Value in accumalator by 1 bit
def RSH(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Shift Left 1 bit position of AC")
    print(" "*5+"Present Value of Accumalotor AC = "+AC)

    AC = ALU.LeftShift(AC)

    print(" "*5+"AC = "+AC)
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

