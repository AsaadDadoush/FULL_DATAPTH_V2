from myhdl import *


@block
def ins_dec(data_in, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU, immJ):

    @always_comb
    def decoder():
        opcode.next = data_in[7:0]  # opcode
        func3.next = data_in[15:12]  # func3
        func7.next = data_in[32:25]  # func7
        rd.next = data_in[12:7]  # rd
        rs1.next = data_in[20:15]  # rs1
        rs2.next = data_in[25:20]  # rs2

        # I-type
        immI.next = intbv(data_in[32:20])
        # S-type
        immS.next = intbv(concat(data_in[32:25], data_in[12:7]))

        # B-type
        immB.next = intbv(concat(data_in[32:31], data_in[8:7], data_in[31:25], data_in[12:8]))

        # U-type
        immU.next = intbv(data_in[32:12])

        # # J-Type
        immJ.next = intbv(concat(data_in[31], data_in[20:12], data_in[20], data_in[31:21]))

    return decoder

@block
def Test():
    data_in = Signal(intbv(0)[32:0])
    opcode = Signal(intbv(0)[7:0])
    rd = Signal(intbv(0)[5:0])
    func3 = Signal(intbv(0)[3:0])
    rs1 = Signal(intbv(0)[5:0])
    rs2 = Signal(intbv(0)[5:0])
    func7 = Signal(intbv(0)[7:0])
    immU = Signal(intbv(0)[20:0])
    immJ = Signal(intbv(0)[20:0])
    immI = Signal(intbv(0)[12:0])
    immS = Signal(intbv(0)[12:0])
    immB = Signal(intbv(0)[12:0])
    ins = ins_dec(data_in, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU, immJ)

    @instance
    def sim():
        data_in.next = 0b00000000000000000010010100010111  # U-AUIPC
        yield delay(2)
        print("="*19, "U-Type", "="*19)
        print("| Data in: ", bin(data_in.next, 32), "|")
        print("| Opcode:  ", bin(opcode.next, 7), " " * 24, "|")
        print("| func3:   ", bin(func3.next, 3), " " * 28, "|")
        print("| func7:   ", bin(func7.next, 7), " " * 24, "|")
        print("| rd:      ", bin(rd.next, 5), " " * 26, "|")
        print("| rs1:     ", bin(rs1.next, 5), " " * 26, "|")
        print("| rs2:     ", bin(rs2.next, 5), " " * 26, "|")
        print("| immU:    ", bin(immU.next, 20), " " * 11, "|")
        print("=" * 46, end="\n\n")
        data_in.next = 0b00000000101100000000001010110011  # R-type
        yield delay(2)
        print("="*19, "R-Type", "="*19)
        print("| Data in: ", bin(data_in.next, 32), "|")
        print("| Opcode:  ", bin(opcode.next, 7), " " * 24, "|")
        print("| func3:   ", bin(func3.next, 3), " " * 28, "|")
        print("| func7:   ", bin(func7.next, 7), " " * 24, "|")
        print("| rd:      ", bin(rd.next, 5), " " * 26, "|")
        print("| rs1:     ", bin(rs1.next, 5), " " * 26, "|")
        print("| rs2:     ", bin(rs2.next, 5), " " * 26, "|")
        print("="*46,end="\n\n")
        data_in.next = 0b11111111111100101000001010010011  # I-Type
        yield delay(2)
        print("="*19, "I-Type", "="*19)
        print("| Data in: ", bin(data_in.next, 32), "|")
        print("| Opcode:  ", bin(opcode.next, 7), " " * 24, "|")
        print("| func3:   ", bin(func3.next, 3), " " * 28, "|")
        print("| func7:   ", bin(func7.next, 7), " " * 24, "|")
        print("| rd:      ", bin(rd.next, 5), " " * 26, "|")
        print("| rs1:     ", bin(rs1.next, 5), " " * 26, "|")
        print("| rs2:     ", bin(rs2.next, 5), " " * 26, "|")
        print("| immI:    ", bin(immI.next, 12), " " * 19, "|")
        print("=" * 46, end="\n\n")
        data_in.next = 0b00000000000000101010001110000011  # I(load)
        yield delay(2)
        print("=" * 19, "I-Type", "=" * 19)
        print("| Data in: ", bin(data_in.next, 32), "|")
        print("| Opcode:  ", bin(opcode.next, 7), " " * 24, "|")
        print("| func3:   ", bin(func3.next, 3), " " * 28, "|")
        print("| func7:   ", bin(func7.next, 7), " " * 24, "|")
        print("| rd:      ", bin(rd.next, 5), " " * 26, "|")
        print("| rs1:     ", bin(rs1.next, 5), " " * 26, "|")
        print("| rs2:     ", bin(rs2.next, 5), " " * 26, "|")
        print("| immI:    ", bin(immI.next, 12), " " * 19, "|")
        print("=" * 46, end="\n\n")
        data_in.next = 0b00000000000000001000000001100111  # I(JALR)
        yield delay(2)
        print("=" * 19, "I-Type", "=" * 19)
        print("| Data in: ", bin(data_in.next, 32), "|")
        print("| Opcode:  ", bin(opcode.next, 7), " " * 24, "|")
        print("| func3:   ", bin(func3.next, 3), " " * 28, "|")
        print("| func7:   ", bin(func7.next, 7), " " * 24, "|")
        print("| rd:      ", bin(rd.next, 5), " " * 26, "|")
        print("| rs1:     ", bin(rs1.next, 5), " " * 26, "|")
        print("| rs2:     ", bin(rs2.next, 5), " " * 26, "|")
        print("| immI:    ", bin(immI.next, 12), " " * 19, "|")
        print("=" * 46, end="\n\n")
        data_in.next = 0b00000000000000000000000001110011  # I(sys)
        yield delay(2)
        print("=" * 19, "I-Type", "=" * 19)
        print("| Data in: ", bin(data_in.next, 32), "|")
        print("| Opcode:  ", bin(opcode.next, 7), " " * 24, "|")
        print("| func3:   ", bin(func3.next, 3), " " * 28, "|")
        print("| func7:   ", bin(func7.next, 7), " " * 24, "|")
        print("| rd:      ", bin(rd.next, 5), " " * 26, "|")
        print("| rs1:     ", bin(rs1.next, 5), " " * 26, "|")
        print("| rs2:     ", bin(rs2.next, 5), " " * 26, "|")
        print("| immI:    ", bin(immI.next, 12), " " * 19, "|")
        print("=" * 46, end="\n\n")
        data_in.next = 0b00000000000001010010000000100011  # S-type
        yield delay(2)
        print("=" * 19, "S-Type", "=" * 19)
        print("| Data in: ", bin(data_in.next, 32), "|")
        print("| Opcode:  ", bin(opcode.next, 7), " " * 24, "|")
        print("| func3:   ", bin(func3.next, 3), " " * 28, "|")
        print("| func7:   ", bin(func7.next, 7), " " * 24, "|")
        print("| rd:      ", bin(rd.next, 5), " " * 26, "|")
        print("| rs1:     ", bin(rs1.next, 5), " " * 26, "|")
        print("| rs2:     ", bin(rs2.next, 5), " " * 26, "|")
        print("| immS:    ", bin(immS.next, 12), " " * 19, "|")
        print("=" * 46, end="\n\n")
        data_in.next = 0b11111110000000101001101011100011  # B-Type
        yield delay(2)
        print("=" * 19, "B-Type", "=" * 19)
        print("| Data in: ", bin(data_in.next, 32), "|")
        print("| Opcode:  ", bin(opcode.next, 7), " " * 24, "|")
        print("| func3:   ", bin(func3.next, 3), " " * 28, "|")
        print("| func7:   ", bin(func7.next, 7), " " * 24, "|")
        print("| rd:      ", bin(rd.next, 5), " " * 26, "|")
        print("| rs1:     ", bin(rs1.next, 5), " " * 26, "|")
        print("| rs2:     ", bin(rs2.next, 5), " " * 26, "|")
        print("| immB:    ", bin(immB.next, 12), " " * 19, "|")
        print("=" * 46, end="\n\n")
        data_in.next = 0b11111110110111111111000011101111  # J-type
        yield delay(2)
        print("=" * 19, "J-Type", "=" * 19)
        print("| Data in: ", bin(data_in.next, 32), "|")
        print("| Opcode:  ", bin(opcode.next, 7), " " * 24, "|")
        print("| func3:   ", bin(func3.next, 3), " " * 28, "|")
        print("| func7:   ", bin(func7.next, 7), " " * 24, "|")
        print("| rd:      ", bin(rd.next, 5), " " * 26, "|")
        print("| rs1:     ", bin(rs1.next, 5), " " * 26, "|")
        print("| rs2:     ", bin(rs2.next, 5), " " * 26, "|")
        print("| immJ:    ", bin(immJ.next, 20), " " * 11, "|")
        print("=" * 46)

    return instances()


def convert():
    data_in = Signal(intbv(0)[32:0])
    opcode = Signal(intbv(0)[7:0])
    rd = Signal(intbv(0)[5:0])
    func3 = Signal(intbv(0)[3:0])
    rs1 = Signal(intbv(0)[5:0])
    rs2 = Signal(intbv(0)[5:0])
    func7 = Signal(intbv(0)[7:0])
    immU = Signal(intbv(0)[20:0])
    immJ = Signal(intbv(0)[20:0])
    immI = Signal(intbv(0)[12:0])
    immS = Signal(intbv(0)[12:0])
    immB = Signal(intbv(0)[12:0])
    ins = ins_dec(data_in, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU, immJ)
    ins.convert(hdl='Verilog')


# convert()
# tb = Test()
# tb.run_sim(100)
#
