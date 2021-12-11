from myhdl import *
from Sys_call import obj


@block
def DataMemory(data_in, enable, size, address, data_out, clk, load_data, load_address):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(3072)]

    @always(clk.posedge)
    def load_logic():
        Mem1[load_address].next = load_data[8:]
        Mem2[load_address].next = load_data[16:8]
        Mem3[load_address].next = load_data[24:16]
        Mem4[load_address].next = load_data[32:24]
        obj.Mem1 = Mem1
        obj.Mem2 = Mem2
        obj.Mem3 = Mem3
        obj.Mem4 = Mem4

    @always_seq(clk.posedge, reset=None)
    def Write_logic():
        if address < 0:
            data_in.next = 0
        translated_address = (int(address / 4))

        if enable == 1:
            if size == 0:
                Mem1[translated_address].next = data_in[8:0]

            elif size == 1:
                Mem1[translated_address].next = data_in[8:0]
                Mem2[translated_address].next = data_in[16:8]

            elif size == 2:
                Mem1[translated_address].next = data_in[8:0]
                Mem2[translated_address].next = data_in[16:8]
                Mem3[translated_address].next = data_in[24:16]
                Mem4[translated_address].next = data_in[32:24]
            else:
                Mem1[translated_address].next = data_in[8:0]
                Mem2[translated_address].next = data_in[16:8]
                Mem3[translated_address].next = data_in[24:16]
                Mem4[translated_address].next = data_in[32:24]
        obj.Mem1 = Mem1
        obj.Mem2 = Mem2
        obj.Mem3 = Mem3
        obj.Mem4 = Mem4

    @always_comb
    def Read_logic():
        translated_address = (int(address / 4))
        if translated_address > 3072:
            translated_address = 3071
        if size == 0:
            data_out.next = concat("00000000", "00000000", "00000000", Mem1[translated_address])
        elif size == 1:
            data_out.next = concat("00000000", "00000000", Mem2[translated_address], Mem1[translated_address])
        else:
            data_out.next = concat(Mem4[translated_address], Mem3[translated_address], Mem2[translated_address],
                                   Mem1[translated_address])

    return instances()
