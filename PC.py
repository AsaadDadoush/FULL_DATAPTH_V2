from myhdl import*

@block
def pc(pass_input, out, clk, reset):
    @always(clk.posedge, pass_input)
    def pcblock():
        print("reset: ", reset + 0)
        if reset:
            out.next = 0
            reset.next = 0
        else:
            out.next = pass_input
        print("****************************** Fetching *****************************")
        print("================================= PC ================================")
        print("Data  in: ", pass_input + 0)
        print("Data out: ", out.next+0)
        print("")
    return instances()
