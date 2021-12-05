import random
from myhdl import *

random.seed()
randrange = random.randrange


@block
def mux2_1(sel, out, i0, i1):
    @always(i1, i0)
    def mux():
        if sel == 0:
            out.next = i0
        else:
            out.next = i1
        print("================== PC or Rs1 mux (input a for ALU) ==================")
        print("input i0: ", i0 + 0)
        print("input i1: ", i1 + 0)
        print("Selection: ", sel + 0)
        print("Output: ", out.next + 0)
        print("")
    return mux


@block
def mux2_1_pcANDalu(sel, out, i0, i1):
    @always(i0, i1, sel)
    def mux():
        if sel == 0:
            out.next = int(i0/4)
        else:
            out.next = int(i1/4)
        print("======================== PC and Address mux =========================")
        print("input i0: ", i0+0)
        print("input i1: ", i1 + 0)
        print("Selection: ",sel+0)
        print("Out from  PC and Address mux: ", out.next+0)
        print("")

    return mux