from myhdl import *

import control
from memory import Memory
from mem import to_number
ProgramData = Memory()
ProgramData.load_binary_file(path="D:/text.txt", starting_address=0)
ProgramData.load_binary_file(path="D:/data.txt", starting_address=8192)


@block
def DataMemory(data_in, enable, size, address, data_out, clk):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(3072)]
    address_index = 0
    for i in range(3072):
        data = Signal(intbv(to_number(ProgramData.read(address_index, 4), 4, True))[32:])
        Mem1[i].next = data[8:]
        Mem1[i]._update()
        Mem2[i].next = data[16:8]
        Mem2[i]._update()
        Mem3[i].next = data[24:16]
        Mem3[i]._update()
        Mem4[i].next = data[32:24]
        Mem4[i]._update()
        address_index += 4
    print("******************** Data memory is done loading ********************")
    print("============================ Data Memory ============================")
    print("Checking Process...")
    print("data saved in 8192= ", bin(Mem4[2048].next, 8), bin(Mem3[2048].next, 8),
          bin(Mem2[2048].next, 8), bin(Mem1[2048].next, 8))

    @always_seq(clk.posedge, reset=None)
    def Write_logic():
        if address < 0:
            data.next = 0
        translated_address = (int(address/4))

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
        control.obj.Mem1 = Mem1
        control.obj.Mem2 = Mem2
        control.obj.Mem3 = Mem3
        control.obj.Mem4 = Mem4

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
