from myhdl import *
from memory import Memory
from mem import to_number

# Program_Instructions = Memory()
# Program_Instructions.load_binary_file(path="D:/binary_file/t1.txt", starting_address=0)
# Program_Instructions.load_binary_file(path="D:/binary_file/d1.txt", starting_address=8192)


@block
def InstructionMemory_syn(load_data, address, data_out, clk):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(3072)]

    @always(clk.posedge)
    def load_logic():
        Mem1[address].next = load_data[8:]
        Mem2[address].next = load_data[16:8]
        Mem3[address].next = load_data[24:16]
        Mem4[address].next = load_data[32:24]

    @always(address)
    def Read_logic():
        data_out.next = concat(Mem4[address], Mem3[address], Mem2[address],
                               Mem1[address])

    return instances()

def convert():
    load_data = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    address = Signal(intbv(0)[32:])
    ins = InstructionMemory_syn(load_data, address, data_out, clk)
    ins.convert(hdl='Verilog')


convert()


