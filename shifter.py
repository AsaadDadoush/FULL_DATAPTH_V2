from myhdl import *


@block
def shifter(data_in, sel, data_out):
    @always(data_in,sel)
    def shift():
        if sel == 0:
            data_out.next = data_in.signed() << 1
        elif sel == 1:
            data_out.next = data_in.signed() << 12
        else:
            data_out.next = data_in.signed()
        # print("============================ imm Shifter ============================")
        # print("Data in: ", data_in+0)
        # print("Selection: ",sel + 0)
        # print("Data Out: ", data_out.next + 0)
        # print("")

    return shift