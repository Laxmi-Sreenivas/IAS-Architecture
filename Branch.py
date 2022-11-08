#Left UnConditional Jump
def LUC_JUMP(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Performing Left Jump to "+"M("+MAR+")")
    
    PC = MAR
    
    print(" "*5+"New Program Counter = "+PC)
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,1

#Right UnConditional Jump
def RUC_JUMP(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Performing Right Jump to "+"M("+MAR+")")

    PC = MAR

    print(" "*5+"New Program Counter = "+PC)
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,0,1

#Left Conditional Jump
def LC_JUMP(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Checking Conditions For Left Jump to "+"M("+MAR+")")

    if AC[0] == '0':
        print(" "*5+"Condition Satisfied")
        
        PC = MAR
    
        print(" "*5+"New Program Counter = "+PC)
        print()

        return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,1
    else:
        print(" "*5+"Condition Not Satisfied")
        print()

        return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Right Conditional Jump
def RC_JUMP(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Checking Conditions For Right Jump to "+"M("+MAR+")")

    if AC[0] == '0':
        print(" "*5+"Condition Satisfied")

        PC = MAR

        print("New Program Counter = "+PC)
        print()

        return Main_Memory,IR,MAR,MBR,AC,MQ,PC,0,1
    else:
        print(" "*5+"Condition Not Satisfied")
        print()
        
        return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0



