import random
from myhdl import *

random.seed()
randrange = random.randrange


@block
def mux2_1(sel, out, i0, i1):
    @always_comb
    def mux():
        if sel == 0:
            out.next = i0
        else:
            out.next = i1
        # print("================== PC or Rs1 mux (input a for ALU) ==================")
        # print("input i0: ", i0 + 0)
        # print("input i1: ", i1 + 0)
        # print("Selection: ", sel + 0)
        # print("Output: ", out.next + 0)
        # print("")
    return mux




