import ALU

#MQ->AC
def LoadMQ(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Transfering Contents of MQ to AC")

    AC = MQ

    print(" "*5+"AC = "+AC)
    print()
    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Mem(MAR)->MBR && MBR->MQ
def LoadMQ_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Transfer Contents of Memory Location X to MQ")

    MBR = Main_Memory[int(MAR,2)]
    MQ  = MBR

    print(" "*5+"MBR = "+MBR+" MQ = "+MQ)
    print()    
    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#AC->MBR && MBR->M(MAR)
def Store_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Transfering Contents of Accumalator to Mem(X)")

    MBR = AC
    Main_Memory[int(MAR,2)] = MBR

    print(" "*5+"MBR = "+MBR+" M(X) = "+Main_Memory[int(MAR,2)])
    print()
    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#Mem(MAR)->MBR && MBR->AC
def Load_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Transfering Contents of Memory Location X to Accumalator")

    MBR = Main_Memory[int(MAR,2)]
    AC  = MBR
    
    print(" "*5+"M(X) = "+Main_Memory[int(MAR,2)]+" AC = "+AC)
    print()
    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#M(X)->MBR && MBR->ALU && bitflip && ALU->AC
def Load_Neg_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Transfering Negative of Memory Location X to Accumalator")

    MBR = Main_Memory[int(MAR,2)]
    AC = ALU.sign_change(MBR)

    print(" "*5+"M(X) = "+Main_Memory[int(MAR,2)]+" MBR = "+MBR+" AC = "+AC)
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#M(X)->MBR && MBR->ALU && make MSB '0' && ALU->AC
def Load_Mod_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Transfering Modulus of Memory Location X to Accumalator")

    MBR = Main_Memory[int(MAR,2)]
    AC = ALU.modulo(MBR)

    print(" "*5+"M(X) = "+Main_Memory[int(MAR,2)]+" MBR = "+MBR+" AC = "+AC)
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

#M(X)->MBR && MBR->ALU && make MSB '1' && ALU->AC
def Load_NegMod_MemX(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    print(" "*5+"Transfering Modulus of Memory Location X to Accumalator")

    MBR = Main_Memory[int(MAR,2)]
    AC = ALU.sign_change((ALU.modulo(MBR)))

    print(" "*5+"M(X) = "+Main_Memory[int(MAR,2)]+" MBR = "+MBR+" AC = "+AC)
    print()

    return Main_Memory,IR,MAR,MBR,AC,MQ,PC,1,0

