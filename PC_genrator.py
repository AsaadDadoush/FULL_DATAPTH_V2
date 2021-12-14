from myhdl import *

@block
def PC_gen(PC, rs1, imm, sel, out, alu_out):
    @always_comb
    def calc_gen():
        if sel == 0:
            if alu_out == 0:
                out.next = PC+4
            else:
                out.next = PC+imm

        elif sel == 1:
            out.next = PC+imm
        elif sel == 2:
            out.next = rs1 + imm
        else:
            out.next = PC+4

    return instances()

@block
def test():
    PC = Signal(intbv(0)[32:])
    imm = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    rs1 = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    alu_out = Signal(intbv(0)[32:])
    ins = PC_gen(PC, rs1, imm, sel, out, alu_out)

    @instance
    def stimulus():
        rs1.next, PC.next, imm.next, sel.next, alu_out.next = 60, 30, 10, 0, 0
        yield delay(2)
        print("\nWhen Branch is not taken and not jalr instruction : ")
        print("|ALU|sel | rs1 | PC | imm | Output|")
        print("|%s  |%s   | %s  | %s | %s  | %-6s|" % (alu_out+0, sel + 0, rs1+0, PC + 0, imm + 0, out + 0))
        print("\nWhen Branch is taken: ")
        rs1.next, PC.next, imm.next, sel.next, alu_out.next = 60, 30, 10, 0, 1
        yield delay(2)
        print("|ALU|sel | rs1 | PC | imm | Output|")
        print("|%s  |%s   | %s  | %s | %s  | %-6s|" % (alu_out + 0, sel + 0, rs1 + 0, PC + 0, imm + 0, out + 0))

        print("\nWhen instruction is Jump And Link Reg: ")
        rs1.next, PC.next, imm.next, sel.next, alu_out.next = 60, 30, 10, 2, 1
        yield delay(2)
        print("|ALU|sel | rs1 | PC | imm | Output|")
        print("|%s  |%s   | %s  | %s | %s  | %-6s|" % (alu_out + 0, sel + 0, rs1 + 0, PC + 0, imm + 0, out + 0))

    return instances()


def convert():
    PC = Signal(intbv(0)[32:])
    imm = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    rs1 = Signal(intbv(0)[32:])
    sel = Signal(intbv(0)[2:])
    alu_out = Signal(intbv(0)[32:])
    ins = PC_gen(PC, rs1, imm, sel, out, alu_out)
    ins.convert(hdl='Verilog')


# tb = test()
# tb.run_sim(500)
convert()

