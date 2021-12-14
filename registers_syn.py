from myhdl import *
import control


@block
def registers_syn(rs1, rs2, rd, rs1_out, rs2_out, enable, DataWrite, clk):
    Reg = [Signal(intbv(0, min=-2 ** 31, max=2 ** 31)) for i in range(32)]

    @always_comb
    def Read_logic():
        rs1_out.next = Reg[rs1].signed()
        rs2_out.next = Reg[rs2].signed()
    @always_seq(clk.posedge, reset=None)
    def write_logic():
        if enable == 1:
            Reg[rd].next = DataWrite

    return instances()

@block
def testbench():
    rs1 = Signal(intbv(0)[5:])
    rs2 = Signal(intbv(0)[5:])
    rd = Signal(intbv(0)[5:])
    rs1_out = Signal(intbv(0)[32:])
    rs2_out = Signal(intbv(0)[32:])
    enable = Signal(bool(0))
    clk = Signal(bool(0))
    DataWrite = Signal(intbv(0)[32:])
    reg = registers_syn(rs1, rs2, rd, rs1_out, rs2_out, enable, DataWrite, clk)

    @always(delay(2))
    def gen_clk():
        clk.next = not clk

    @instance
    def stimulus():
        enable.next = 1
        rd.next = 0b00011
        DataWrite.next = 0b01001
        yield delay(5)
        print('========================================================================================================'
              '=========================================')
        rs1.next = 0b00111
        rs2.next = 0b00011
        yield delay(10)
        print("| Data in: ", bin(DataWrite, 32), " "*98, "|")
        print("| rd: ", bin(rd, 5), " "*130, "|")
        print('========================================================================================================'
              '=========================================')
        print("| rs1      | rs2   |        rs1_out                      |           rs2_out      "
              "                 |                data              |  enable |")
        print("| %s    | %s |   %s  |    %s     | %s |       %s | " % \
              (bin(rs1, 5), bin(rs2, 5), bin(rs1_out, 32), bin(rs2_out, 32), bin(DataWrite, 32), bin(enable, 1)))
        enable.next = 1
        rd.next = 0b00111
        DataWrite.next = 0b01111
        enable.next = 1
        yield delay(5)
        print('========================================================================================================'
              '=========================================')
        print("| Data in: ", bin(DataWrite, 32), " " * 98, "|")
        print("| rd: ", bin(rd, 5), " " * 130, "|")
        print('========================================================================================================'
              '=========================================')

        print("| rs1      | rs2   |        rs1_out                      |           rs2_out      "
              "                 |                data              |  enable |")
        print("| %s    | %s |   %s  |    %s     | %s |       %s | " % \
              (bin(rs1, 5), bin(rs2, 5), bin(rs1_out, 32), bin(rs2_out, 32), bin(DataWrite, 32), bin(enable, 1)))
        print('========================================================================================================'
              '=========================================')
        enable.next = 0
        yield delay(5)

    return instances()

def convert():
    rs1 = Signal(intbv(0)[5:])
    rs2 = Signal(intbv(0)[5:])
    rd = Signal(intbv(0)[5:])
    rs1_out = Signal(intbv(0)[32:])
    rs2_out = Signal(intbv(0)[32:])
    enable = Signal(bool(0))
    clk = Signal(bool(0))
    DataWrite = Signal(intbv(0)[32:])
    reg = registers_syn(rs1, rs2, rd, rs1_out, rs2_out, enable, DataWrite, clk)
    reg.convert(hdl='Verilog')


# convert()
# tst = testbench()
# tst.run_sim(50)
