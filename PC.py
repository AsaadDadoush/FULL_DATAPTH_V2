from myhdl import *


@block
def pc(data_in, out, clk,flag):
    @always(clk.posedge)
    def pcblock():
        if flag == 1:
            out.next = data_in

    return instances()

@block
def test():
    data_in = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    flag = Signal(bool(0))
    ins = pc(data_in, out, clk, flag)

    @always(delay(1))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        flag.next = 1
        data_in.next = 0b111
        yield clk.posedge
        print("Data in : ", bin(data_in.next, 32))
        print("Data out: ", bin(out.next, 32))

    return instances()


def convert():
    data_in = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    flag = Signal(bool(0))
    ins = pc(data_in, out, clk, flag)
    ins.convert(hdl='Verilog')


convert()
tb=test()
tb.run_sim(500)