import random
from myhdl import *

random.seed()
randrange = random.randrange


@block
def mux_3to1(i0, i1, i2, sel, out):
    @always(i0, i1, i2)
    def mux3to1():
        if sel == 0:
            out.next = i0
        elif sel == 1:
            out.next = i1
        elif sel == 2:
            out.next = i2
        else:
            out.next = i2
        print("=========== Rs2 or imm or Costant 4 mux (input b for ALU) ===========")
        print("input i0: ", i0 + 0)
        print("input i1: ", i1 + 0)
        print("input i2: ", i2 + 0)
        print("Selection: ", sel + 0)
        print("Output: ", out.next + 0)
        print("")

    return mux3to1

@block
def mux_3to1_for_Register(i0, i1, i2, sel, out):
    @always(i0, i1, i2)
    def mux3to1():
        if sel == 0:
            out.next = i0.signed()
        elif sel == 1:
            out.next = i1.signed()
        elif sel == 2:
            out.next = i2.signed()
        else:
            out.next = i2.signed()
        print("============== ALU result or Load Value or imm<<12 mux ==============")
        print("input i0: ", i0 + 0)
        print("input i1: ", i1 + 0)
        print("input i2: ", i2 + 0)
        print("Selection: ", sel + 0)
        print("Output: ", out.next + 0)
        print("")

    return mux3to1
