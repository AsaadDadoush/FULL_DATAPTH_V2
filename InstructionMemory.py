from myhdl import *
from memory import Memory
from mem import to_number

Program_Instructions = Memory()
Program_Instructions.load_binary_file(path="D:/binary_file/t1.txt", starting_address=0)
Program_Instructions.load_binary_file(path="D:/binary_file/d1.txt", starting_address=8192)


@block
def InstructionMemory(load_data, load_address, address, data_out, clk):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(3072)]


    @always_seq(clk.posedge, reset=None)
    def load_logic():
        Mem1[load_address].next = load_data[8:]
        Mem2[load_address].next = load_data[16:8]
        Mem3[load_address].next = load_data[24:16]
        Mem4[load_address].next = load_data[32:24]

    @always(address)
    def Memory_logic():
        translated_address = int(address / 4)
        data_out.next = concat(Mem4[translated_address], Mem3[translated_address], Mem2[translated_address],
                               Mem1[translated_address])
        # print("========================= Instruction Memory ========================")
        # print("Address: ", address + 0)
        # print("Data out: ", bin(data_out.next, 32))
        # print("")

    return instances()
