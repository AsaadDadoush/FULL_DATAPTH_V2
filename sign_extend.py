from myhdl import *


@block
def sign_extender(data_in, sel, data_out):
    # sel >> 0 for 8-bit msb extend
    # sel >> 1 for 16-bit msb extend
    # sel >> 2 for zero-extends

    @always_comb
    def logic():
        if sel == 0:
            data_out.next = intbv(data_in[8:])[32:]
        elif sel == 1:
            data_out.next = intbv(data_in[16:]).signed()[32:]
        elif sel == 2:
            data_out.next = data_in
        else:
            data_out.next = data_in

    return logic
