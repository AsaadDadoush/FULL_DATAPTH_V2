from myhdl import *


@block
def ins_dec(data_in, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU, immJ):

    @always_comb
    def decoder():
        opcode.next = data_in[7:0]  # opcode
        func3.next = data_in[15:12]  # func3
        func7.next = data_in[32:25] # func7
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
        # print("======================== Instruction decoder ========================")
        # print("--------------- input ---------------")
        # print("Data in: ", bin(data_in,32), " = ", data_in+0)
        # print("-------------- Outputs --------------")
        # print("Opcode: ", bin(opcode.next, 7))
        # print("func3: ", bin(func3.next, 3), " = ", func3.next+0)
        # print("func7: ", bin(func7.next, 7), " = ", func7.next+0)
        # print("immI: ", bin(immI.next, 12), " = ", immI.next + 0)
        # print("immS: ", bin(immS.next, 12), " = ", immS.next + 0)
        # print("immB: ", bin(immB.next, 12), " = ", immB.next + 0)
        # print("immU: ", bin(immU.next, 20), " = ", immU.next + 0)
        # print("immJ: ", bin(immJ.next, 20), " = ", immJ.next + 0)
        # print("")
    return decoder

