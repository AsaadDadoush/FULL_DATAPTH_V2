import math
import struct

from myhdl import *
from memory import Memory

ACTIVE_LOW, INACTIVE_HIGH = 0, 1


def number_to_Buff(number: int, size, little_endian=True):
    endianness = '<' if little_endian else '>'
    if size == 1:
        fmt = f'b'
    elif size == 2:
        fmt = f'{endianness}h'
    elif size == 4:
        fmt = f'{endianness}i'
    elif size == 8:
        fmt = f'{endianness}q'
    else:
        raise Exception('unsupported Size')

    retV = struct.pack(fmt, number)
    return retV


def to_number(buff: bytearray, size, signed, little_endian=True):
    endianness = '<' if little_endian else '>'
    if size == 1:
        fmt = f'b' if signed else f'B'
    elif size == 2:
        fmt = f'{endianness}h' if signed else f'{endianness}H'
    elif size == 4:
        fmt = f'{endianness}i' if signed else f'{endianness}I'
    elif size == 8:
        fmt = f'{endianness}q' if signed else f'{endianness}Q'
    else:
        raise Exception('unsupported Size')

    retV = struct.unpack(fmt, buff[0:size])
    return retV[0]


# class Memory_copy:
#     def __init__(self, Memory_1=[], Memory_2=[], Memory_3=[], Memory_4=[]):
#         self.Memory_1 = Memory_1
#         self.Memory_2 = Memory_2
#         self.Memory_3 = Memory_3
#         self.Memory_4 = Memory_4


# global_copy = Memory_copy()

program = Memory()
program.load_binary_file(path="C:/Users/asaad/Desktop/test2/V2Code", starting_address=0)
program.load_binary_file(path="C:/Users/asaad/Desktop/test2/V2Data", starting_address=8191)

@block
def memory(data_in, enable, size, address,addressWrite, data_out):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(3072)]
    address_index = 0
    for i in range(3072):
        data = Signal(intbv(to_number(program.read(address_index, 4), 4, True))[32:])
        Mem1[i].next = data[8:]
        Mem1[i]._update()
        Mem2[i].next = data[16:8]
        Mem2[i]._update()
        Mem3[i].next = data[24:16]
        Mem3[i]._update()
        Mem4[i].next = data[32:24]
        Mem4[i]._update()
        address_index += 4
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
    @always(enable)
    def WriteLogic():
        if enable == 1:
            if size == 0:
                Mem1[addressWrite].next = data_in[8:0]

            elif size == 1:
                Mem1[addressWrite].next = data_in[8:0]
                Mem2[addressWrite].next = data_in[16:8]

            elif size == 2:
                Mem1[addressWrite].next = data_in[8:0]
                Mem2[addressWrite].next = data_in[16:8]
                Mem3[addressWrite].next = data_in[24:16]
                Mem4[addressWrite].next = data_in[32:24]
            else:
                Mem1[addressWrite].next = data_in[8:0]
                Mem2[addressWrite].next = data_in[16:8]
                Mem3[addressWrite].next = data_in[24:16]
                Mem4[addressWrite].next = data_in[32:24]
        else :
            if size == 0:
                data_out.next = concat("00000000", "00000000", "00000000", Mem1[address])
            elif size == 1:
                data_out.next = concat("00000000", "00000000", Mem2[address], Mem1[address])
            else:
                data_out.next = concat(Mem4[address], Mem3[address], Mem2[address], Mem1[address])
    print("memory is done loading")
    print("***********************************************************")

    @always(address)
    def inst():
        data_out.next = concat(Mem4[address], Mem3[address], Mem2[address], Mem1[address])
        print("********************************************************* Instruction "
              "*********************************************************")
        print("=============================== Memory ==============================")
        print("Address: ", address.next+0)
        print("DATA out of memory: ", bin(data_out.next, 32))
        # index = 0
        # print(("Memory[%s]: %s%s%s%s")%(index,bin(Mem4[index],8),bin(Mem3[index],8),bin(Mem2[index],8),bin(Mem1[index],8)))
        # print(("Memory[%s]: %s (in Decimal)")%(index,concat(bin(Mem4[index],8),bin(Mem3[index],8),bin(Mem2[index],8),bin(Mem1[index],8))+0))
        # print("")


    return instances()
