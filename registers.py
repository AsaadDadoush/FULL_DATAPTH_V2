from myhdl import *
from Sys_call import obj


@block
def registers(rs1, rs2, rd, rs1_out, rs2_out, enable, DataWrite, clk):
    Reg = [Signal(intbv(0, min=-2 ** 31, max=2 ** 31)) for i in range(32)]
    Reg[0] = Signal(intbv(0)[32:])
    Reg[0]._update()
    Reg[2] = Signal(intbv(10016)[32:])
    Reg[2]._update()
    Reg[3] = Signal(intbv(6144)[32:])
    Reg[3]._update()
    obj.copy_register = Reg

    @always_comb
    def Read_logic():
        rs1_out.next = Reg[rs1].signed()
        rs2_out.next = Reg[rs2].signed()

    @always_seq(clk.posedge, reset=None)
    def write_logic():
        if enable == 1:
            Reg[rd].next = DataWrite
            Reg[rd]._update()
            Reg[0].next = 0
            Reg[0]._update()
            obj.copy_register = Reg

    return instances()

