import random
from myhdl import *

random.seed()
randrange = random.randrange


@block
def mux_3to1(i0, i1, i2, sel, out):
    @always_comb
    def mux3to1():
        if sel == 0:
            out.next = i0
        elif sel == 1:
            out.next = i1
        elif sel == 2:
            out.next = i2
        else:
            out.next = i2


    return mux3to1

@block
def mux_3to1_for_Register(i0, i1, i2, sel, out):
    @always_comb
    def mux3to1():
        if sel == 0:
            out.next = i0.signed()
        elif sel == 1:
            out.next = i1.signed()
        elif sel == 2:
            out.next = i2.signed()
        else:
            out.next = i2.signed()


    return mux3to1
