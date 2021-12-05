import random
from myhdl import *


@block
def alu(a, b, sel, out):
    @always(a, b)
    def alu():
        # ADD
        if sel == 0:
            out.next = a.signed() + b.signed()
        # MULTIPLY
        elif sel == 1:
            out.next = a.signed() * b.signed()
        # DIVISION
        elif sel == 2:
            out.next = a.signed() // b.signed()
        # AND
        elif sel == 3:
            out.next = a.signed() & b.signed()
        # OR
        elif sel == 4:
            out.next = a.signed() | b.signed()
        # XOR
        elif sel == 5:
            out.next = a.signed() ^ b.signed()
        # Shift left
        elif sel == 6:
            out.next = a.signed() << b[5:].signed()
        # Shift right
        elif sel == 7:
            out.next = a.signed() >> b[5:].signed()
        # Branch ==
        elif sel == 8:
            if a.signed() == b.signed():
                out.next = 1
            else:
                out.next = 0
        # Branch !=
        elif sel == 9:
            if a.signed() != b.signed():
                out.next = 1
            else:
                out.next = 0
        # Branch < & Set less than
        elif sel == 10:
            if a.signed() < b.signed():
                out.next = 1
            else:
                out.next = 0
        # Branch < (U) & Set less than (U)
        elif sel == 11:
            if a.signed() < b[32:]:
                out.next = 1
            else:
                out.next = 0
        # Branch <=
        elif sel == 12:
            if a.signed() <= b.signed():
                out.next = 1
            else:
                out.next = 0
        # Shift right Arith
        elif sel == 13:
            out.next = a.signed() >> b[5:].signed()

        # Branch >= (U)
        elif sel == 14:
            if a.signed() > b[32:]:
                out.next = 1
            else:
                out.next = 0
        # DIV (U)
        elif sel == 15:
            out.next = a.signed() // b[32:]
        # Remainder
        elif sel == 16:
            out.next = a.signed() % b.signed()
        # Remainder (U)
        else:
            out.next = a.signed() % b[32:]

        print("================================ ALU ================================")
        print("a: ", a+0, " b: ", b+0)
        print("Operation: ", sel + 0)
        print("ALU out: ", out.next+0)
        print("")

    return alu