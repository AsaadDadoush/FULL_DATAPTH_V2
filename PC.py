from myhdl import *


@block
def pc(pass_input, out, clk, reset,flag):
    @always_seq(clk.posedge, reset=reset)
    def pcblock():
        if flag == 1:
            out.next = pass_input

    return instances()
