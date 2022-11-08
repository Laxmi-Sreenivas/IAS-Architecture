import Data_Transfer
import Branch
import Arithmetic
import Address_Modify

#Converting decimal number into binary string
def decimal_binary(num,bits):
    binary_num = ""
    pad = 0

    while num:
        binary_num = str(num%2) +binary_num
        num = int(num/2)
        pad = pad + 1

    return "0"*(bits-pad) +binary_num

#Taking input from I/O device
def IO_device(PC,Main_Memory):
    print("->Taking Instructions Form I/O...")

    while True:
        n = input("")
        if n:
            Main_Memory[int(PC,2)] =  n
            PC = decimal_binary(int(PC,2)+1,12)
        else:
            break

    return PC,Main_Memory

#Fetching an instruction
def Fetch_Instruction(PC,Main_Memory,MAR,MBR):
    MAR = PC
    print("->Fetching The Instruction.....")
    MBR = Main_Memory[int(MAR,2)]

    print(" "*2+"PC = "+PC+" MAR = "+MAR+" MBR = "+MBR)
    print()

    return MAR,MBR

#Fetching the left half of instruction
def Left_Instruction(IR,MAR,MBR,IBR,flag_left):

    if flag_left:
        print(" "*3+"->Fetching The Left-Half.....")
        print()

        IBR = MBR[20:]
        IR  = MBR[0:8]
        MAR = MBR[8:20]

        print(" "*5+"IR = "+IR+" MAR = "+MAR+" IBR = "+IBR)
    return IR,MAR,IBR

#Fetching the right half of instruction
def Right_Instruction(IR,MAR,MBR,IBR,flag_left):

    print(" "*3+"->Fetching The Right-Half.....")
    print()

    if flag_left:
        IR  = IBR[0:8]
        MAR = IBR[8:]

    else :
        IR  = MBR[20:28]
        MAR = MBR[28:]

    
    print(" "*5+"IR = "+IR+" MAR = "+MAR)
    return IR,MAR

#Decoding An Instruction
def Decode_Instruction(IR,decode_dict):
    #Decoding process
    print(" "*5+"Decoding The Instruction.....")
    print(" "*5+"The instruction type is "+decode_dict[IR])
    print()

#Executing The Decoded Instruction
def Execute_Instruction(Main_Memory,IR,MAR,MBR,AC,MQ,PC):
    Execute_Instruction = {
                           "00001010":Data_Transfer.LoadMQ,"00001001" :Data_Transfer.LoadMQ_MemX,
                           "00100001":Data_Transfer.Store_MemX,"00000001":Data_Transfer.Load_MemX,
                           "00000010":Data_Transfer.Load_Neg_MemX,"00000011":Data_Transfer.Load_Mod_MemX,
                           "00000100":Data_Transfer.Load_NegMod_MemX,"00001101":Branch.LUC_JUMP,
                           "00001110":Branch.RUC_JUMP,"00001111":Branch.LC_JUMP,"00010000":Branch.RC_JUMP,
                           "00000101":Arithmetic.Add_MemX,"00000111":Arithmetic.Add_mod_MemX,
                           "00000110":Arithmetic.Sub_MemX,"00001000":Arithmetic.Sub_mod_MemX,
                           "00001011":Arithmetic.Mul_MemX,"00001100":Arithmetic.Div_MemX,
                           "00010100":Arithmetic.LSH,"00010101":Arithmetic.RSH,
                           "00010010":Address_Modify.LeftSTOR,"00010011":Address_Modify.RightSTOR
                          }
    
    return Execute_Instruction[IR](Main_Memory,IR,MAR,MBR,AC,MQ,PC)
        