from myhdl import *
from memory import Memory
from mem import to_number
Program_Instructions = Memory()
Program_Instructions.load_binary_file(path="D:/Osama Shits/Test1_text.txt", starting_address=0)
Program_Instructions.load_binary_file(path="D:/Osama Shits/Test1_data.txt", starting_address=8192)


@block
def InstructionMemory(address,data_out):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(3072)]
    address_index = 0
    for i in range(3072):
        data = Signal(intbv(to_number(Program_Instructions.read(address_index, 4), 4, True))[32:])
        Mem1[i].next = data[8:]
        Mem1[i]._update()
        Mem2[i].next = data[16:8]
        Mem2[i]._update()
        Mem3[i].next = data[24:16]
        Mem3[i]._update()
        Mem4[i].next = data[32:24]
        Mem4[i]._update()
        address_index += 4
    print("***************** Instruction memory is done loading ****************")
    @always(address)
    def Memory_logic():
        translated_address = int(address/4)
        data_out.next = concat(Mem4[translated_address], Mem3[translated_address], Mem2[translated_address], Mem1[translated_address])
        print("========================= Instruction Memory ========================")
        print("Address: ", address+0)
        print("Data out: ", bin(data_out.next, 32))
        print("")
    return instances()


