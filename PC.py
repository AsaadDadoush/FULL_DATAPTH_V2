from myhdl import *


@block
def pc(data_in, out, clk, reset, flag):
    @always_seq(clk.posedge, reset=reset)
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
    reset = ResetSignal(0, active=1, isasync=False)
    ins = pc(data_in, out, clk, reset, flag)

    @always(delay(1))
    def clkgen():
        clk.next = not clk

    @instance
    def stimulus():
        flag.next = 1
        data_in.next = 0b111
        yield clk.posedge
        print("="*71)
        print("|             Data in              |             Data out             |")
        print("=" * 71)
        print("| %-32s | %-32s |" % (bin(data_in.next, 32) ,bin(out.next, 32)))
        print("=" * 71)
        yield clk.posedge
        data_in.next = 0b10111101
        yield clk.posedge
        print("| %-32s | %-32s |" % (bin(data_in.next, 32), bin(out.next, 32)))
        print("=" * 71)
    return instances()


def convert():
    data_in = Signal(intbv(0)[32:])
    out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    flag = Signal(bool(0))
    reset = ResetSignal(0, active=1, isasync=False)
    ins = pc(data_in, out, clk, reset, flag)
    ins.convert(hdl='Verilog')


# convert()
# tb=test()
# tb.run_sim(500)