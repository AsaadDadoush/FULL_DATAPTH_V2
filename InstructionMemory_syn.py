from myhdl import *


@block
def InstructionMemory_syn(load_data, load_address, address, data_out, clk):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(10)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(10)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(10)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(10)]

    @always_seq(clk.posedge, reset=None)
    def load_logic():
        Mem1[load_address].next = load_data[8:]
        Mem2[load_address].next = load_data[16:8]
        Mem3[load_address].next = load_data[24:16]
        Mem4[load_address].next = load_data[32:24]

    @always(address)
    def Memory_logic():
        # translated_address = int(address / 4)
        data_out.next = concat(Mem4[address], Mem3[address], Mem2[address],
                               Mem1[address])

    return instances()


def convert():
    load_data = Signal(intbv(0)[32:])
    load_address = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    address = Signal(intbv(0)[32:])
    ins = InstructionMemory_syn(load_data,load_address, address, data_out, clk)
    ins.convert(hdl='Verilog')


# convert()


