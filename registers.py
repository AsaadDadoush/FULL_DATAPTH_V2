from myhdl import *
from copy import deepcopy
from control import obj







@block
def registers(rs1, rs2, rd, rs1_out, rs2_out, enable, DataWrite):
    Reg = [Signal(intbv(0, min=-2 ** 31, max=2 ** 31)) for i in range(32)]
    Reg[0] = Signal(intbv(0)[32:])
    Reg[0]._update()
    Reg[2] = Signal(intbv(10016)[32:])
    Reg[2]._update()
    Reg[3] = Signal(intbv(6144)[32:])
    Reg[3]._update()

    @always(rd, rs1, rs2)
    def Read_logic():
        rs1_out.next = Reg[rs1].signed()
        rs2_out.next = Reg[rs2].signed()
        print("=========================== Register File ===========================")
        print("Enable: ", enable + 0)
        print("rd: ", rd.next + 0)
        print("rs1: ", rs1 + 0)
        print("rs2: ", rs2 + 0)
        print("Data in: ", DataWrite + 0)
        print("rs1_out: ", rs1_out.next + 0)
        print("rs2_out: ", rs2_out.next + 0)

        print("------------ Registers -------------")
        for i in range(32):
            print("Reg[%s]: %s" % (i, Reg[i].next + 0))
        print("")
        obj.cop(Reg)



    @always(DataWrite)
    def write_logic():
        if enable == 1:
            Reg[rd].next = DataWrite
            Reg[rd]._update()
            print("")
            print("# %s has been writen on Reg[%s]" % (DataWrite + 0, rd + 0))
            print("")
            print("=========================== Register File ===========================")
            print("Enable: ", enable + 0)
            print("rd: ", rd.next + 0)
            print("rs1: ", rs1 + 0)
            print("rs2: ", rs2 + 0)
            print("Data in: ", DataWrite + 0)
            print("rs1_out: ", rs1_out.next + 0)
            print("rs2_out: ", rs2_out.next + 0)
            print("------------ Registers -------------")
            for i in range(32):
                print("Reg[%s]: %s" % (i, Reg[i].next + 0))
            print("")
            obj.cop(Reg)


    print("=========================== Register File ===========================")
    print("Enable: ", enable + 0)
    print("rd: ", rd.next + 0)
    print("rs1: ", rs1 + 0)
    print("rs2: ", rs2 + 0)
    print("Data in: ", DataWrite + 0)
    print("rs1_out: ", rs1_out.next + 0)
    print("rs2_out: ", rs2_out.next + 0)

    print("------------ Registers -------------")
    for i in range(32):
        print("Reg[%s]: %s" % (i, Reg[i].next + 0))
    print("")

    return instances()
