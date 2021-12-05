from myhdl import *
from memory import Memory
from mem import to_number

ProgramData = Memory()
ProgramData.load_binary_file(path="D:/Osama Shits/OsamaPure1.txt", starting_address=0)
ProgramData.load_binary_file(path="D:/Osama Shits/OsamaPure.txt", starting_address=8191)


# print(ProgramData.Max_Address)


@block
def DataMemory(data_in, enable, size, address, data_out):
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
    # print("_" * 35)
    # print('Address: ', address_index, "Has been loaded in address %s" % (int(address_index/4)))
    # print("%s|%s|%s|%s" % (bin(Mem4[i], 8), bin(Mem3[i], 8), bin(Mem2[i], 8), bin(Mem1[i], 8)))
    # address_index += 4
    #     global global_copy
    #     global_copy = Memory_copy(Mem1, Mem2, Mem3, Mem4)
    #                                   5        13
    #                    000000000001|00101|000|01101|0010011 done
    #                    0000001|01011|00100|000|00101|0110011 done
    #                                    5       7
    #                    000000000000|00101|010|00111|0000011  # I(load)
    #
    # data = Signal(intbv("00000000000000101000011010010011")[32:])
    # Mem1[0].next = data[8:]
    # Mem2[0].next = data[16:8]
    # Mem3[0].next = data[24:16]
    # Mem4[0].next = data[32:24]
    # Mem1[0]._update()
    # Mem2[0]._update()
    # Mem3[0]._update()
    # Mem4[0]._update()
    # data = Signal(intbv("00000000000000101010001110000011")[32:])
    # Mem1[1].next = data[8:]
    # Mem2[1].next = data[16:8]
    # Mem3[1].next = data[24:16]
    # Mem4[1].next = data[32:24]
    # Mem1[1]._update()
    # Mem2[1]._update()
    # Mem3[1]._update()
    # Mem4[1]._update()
    # data = Signal(intbv("00000000000000000000000001000101")[32:])
    # Mem1[2].next = data[8:]
    # Mem2[2].next = data[16:8]
    # Mem3[2].next = data[24:16]
    # Mem4[2].next = data[32:24]
    # Mem1[2]._update()
    # Mem2[2]._update()
    # Mem3[2]._update()
    # Mem4[2]._update()
    #
    print("============================ Data Memory ============================")
    print("Address: ", address + 0)
    print("Enable: ", enable + 0)
    print("Data in: ", bin(data_in, 32), " = ", data_in + 0)
    print("Data out: ", bin(data_out.next, 32))

    @always(data_in, address, enable, size)
    def Write_logic():
        translated_address = int(address/4)
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
                Mem3[address].next = data_in[24:16]
                Mem4[translated_address].next = data_in[32:24]

    @always(address, size)
    def Read_logic():
        translated_address = int(address / 4)
        print("Translated Address: ",translated_address)
        if size == 0:
            data_out.next = concat("00000000", "00000000", "00000000", Mem1[translated_address])
        elif size == 1:
            data_out.next = concat("00000000", "00000000", Mem2[translated_address], Mem1[translated_address])
        else:
            data_out.next = concat(Mem4[translated_address], Mem3[translated_address], Mem2[translated_address],
                                   Mem1[translated_address])
    print("")

    return instances()
