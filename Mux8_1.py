from myhdl import *
from random import randrange


@block
def mux8_1(i0, i1, i2, i3, i4, out, sel):
    @always(i0, i1, i2, i3, i4,sel)
    def mux():
        if sel == 0:
            out.next = i0
        elif sel == 1:
            out.next = i1
        elif sel == 2:
            out.next = i2
        elif sel == 3:
            out.next = i3
        elif sel == 4:
            out.next = i4
        elif sel == 5:
            out.next = i4
        elif sel == 6:
            out.next = i4
        else:
            out.next = i4
        print("============================== imm mux ==============================")
        print("input i0: ", i0 + 0)
        print("input i1: ", i1 + 0)
        print("input i2: ", i2 + 0)
        print("input i3: ", i3 + 0)
        print("input i4: ", i4 + 0)
        print("Selection: ", sel + 0)
        print("Output: ", out.next + 0)
        print("")
    return mux
