from myhdl import *


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

    return instances()
