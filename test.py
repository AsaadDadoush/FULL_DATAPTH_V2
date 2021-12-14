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

    @always_seq(clk.posedge, reset=None)
    def Write_logic():
        if enable == 1:
            if size == 0:
                Mem1[address].next = data_in[8:0]

            elif size == 1:
                Mem1[address].next = data_in[8:0]
                Mem2[address].next = data_in[16:8]

            elif size == 2:
                Mem1[address].next = data_in[8:0]
                Mem2[address].next = data_in[16:8]
                Mem3[address].next = data_in[24:16]
                Mem4[address].next = data_in[32:24]
            else:
                Mem1[address].next = data_in[8:0]
                Mem2[address].next = data_in[16:8]
                Mem3[address].next = data_in[24:16]
                Mem4[address].next = data_in[32:24]
    @always_comb
    def Read_logic():
        if size == 0:
            data_out.next = concat("00000000", "00000000", "00000000", Mem1[address])
        elif size == 1:
            data_out.next = concat("00000000", "00000000", Mem2[address], Mem1[address])
        else:
            data_out.next = concat(Mem4[address], Mem3[address], Mem2[address],
                                   Mem1[address])

    return instances()