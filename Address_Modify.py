def LeftSTOR(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Changing the left Address of the given M(X)")
    print(" "*5+"Current Left Adress",(Main_Memory[(int(MAR,2))])[8:20])

    MBR = Main_Memory[int(MAR,2)]
    MBR = MBR[:8]+AC[28:]+MBR[20:]
    Main_Memory[int(MAR,2)] = MBR

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

def RightSTOR(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Changing the Right Address of the given M(X)")
    print(" "*5+"Current Right Adress",(Main_Memory[(int(MAR,2))])[8:20])

    MBR = Main_Memory[int(MAR,2)]
    MBR = MBR[:28]+AC[28:]
    Main_Memory[int(MAR,2)] = MBR

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0
