import IAS

#Important registers
MAR,MBR = " " , " "
IR ,IBR = " " , " "
AC ,MQ ,PC  = "0"*40,"0"*40,"0"*2+"1111101000"
Main_memory = ['0'*40]*1000 +[""]*3096

#Control signals
MAX = 0
Left  = 1
Jump  = 0

#Decoding Dictionary
decode_dict = {
               "00001010" :"LOAD MQ", "00001001" :"LOAD MQ,M(X)", "00100001" :"STOR M(X) ",
               "00000001" :"LOAD M(X) ","00000010" :"LOAD –M(X) ","00000011" :"LOAD |M(X)| ",
               "00000100" :"LOAD –|M(X)| ","00001101" :"JUMP M(X,0:19)","00001110" :"JUMP M(X,20:39)",
               "00001111" :"JUMP + M(X,0:19)","00010000" :"JUMP + M(X,20:39) ","00000101" :"ADD M(X) ",
               "00000111" :"ADD |M(X)|", "00000110" :"SUB M(X) ","00001000" :"SUB |M(X)|", 
               "00001011" :"MUL M(X) ","00001100" :"DIV M(X)","00010100" :"LSH ","00010101" :"RSH ",
               "00010010" :"STOR M(X,8:19)","00010011" :"STOR M(X,28:39)"
              }



#Making Program 
print("Enter the number :",end="")
n = int(input(""))
Main_memory[0] = IAS.decimal_binary(n,40) if n>=0 else '1'+IAS.decimal_binary((-1)*n,39)
Main_memory[1] = (Main_memory[1])[:39] + '1'
Main_memory[2] = (Main_memory[1])[:39] + '1'
Main_memory[3] = (Main_memory[1])[:39] + '1'
MAX = IAS.decimal_binary(int(PC,2)+6,2)
Main_memory[1000] = "0000001000000000000000001111001111101110"
Main_memory[1001] = "0000100100000000001100001011000000000010"
Main_memory[1002] = "0000101000000000000000100001000000000011"
Main_memory[1003] = "0000000100000000001000000101000000000001"
Main_memory[1004] = "0010000100000000001000000001000000000000"
Main_memory[1005] = "0000011000000000001000001111001111101001"

print()
#Program Executing
while int(PC,2)<int(MAX,2):
    print("*"*120)
    
    Jump = 0
    #Fetching Instruction
    MAR,MBR = IAS.Fetch_Instruction(PC,Main_memory,MAR,MBR)

    #Dealing with the Left Half
    if(Left):
        IR,MAR,IBR = IAS.Left_Instruction(IR,MAR,MBR,IBR,Left)
        IAS.Decode_Instruction(IR,decode_dict)
        Main_memory,IR,MAR,MBR,AC,MQ,PC,Left,Jump = IAS.Execute_Instruction(Main_memory,IR,MAR,MBR,AC,MQ,PC)

    #Dealing with Jump
    if Jump:continue
    
    #Dealing with the Right Half
    IR,MAR = IAS.Right_Instruction(IR,MAR,MBR,IBR,Left)
    IAS.Decode_Instruction(IR,decode_dict)
    Main_memory,IR,MAR,MBR,AC,MQ,PC,Left,Jump = IAS.Execute_Instruction(Main_memory,IR,MAR,MBR,AC,MQ,PC)

    #Dealing with Jump
    if Jump:continue

    #Incrementing Program Counter
    PC = IAS.decimal_binary(int(PC,2) + 1,12)
    Left = 1


print()
print("Final Answer :",int(Main_memory[3],2))

    






