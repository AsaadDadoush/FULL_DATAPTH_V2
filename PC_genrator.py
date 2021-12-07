from myhdl import *



@block
def PC_gen(PC, rs1, imm, sel, out, alu_out):
    @always_comb
    def calc_gen():
        if sel == 0:
            if alu_out == 0:
                out.next = PC+4
            elif alu_out == 1:
                out.next = PC+imm

        elif sel == 1:
            out.next = PC+imm
        elif sel == 2:
            out.next = rs1 + imm
        elif sel == 3:
            out.next = PC+4


        # print("=============================== PC_gen ==============================")
        # print("PC  (input 1): ", PC + 0)
        # print("imm (input 2): ", imm + 0)
        # print("Rs1 (input 3): ", rs1+0)
        # print("Selection: ", sel + 0)
        # print("Output: ", out.next + 0)
        # print("")

    return instances()