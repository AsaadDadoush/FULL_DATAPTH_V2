from myhdl import *
from memory import to_number, number_to_Buff, Memory

program = Memory()
program.load_binary_file(path="C:/Users/asaad/Desktop/test2/V2Code", starting_address=0)
program.load_binary_file(path="C:/Users/asaad/Desktop/test2/V2Data", starting_address=8192)


@block
def InstructionMemory_syn(load_data, load_address, address, data_out, clk):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(3072)]

    @always_seq(clk.posedge, reset=None)
    def load_logic():
        Mem1[load_address].next = load_data[8:]
        Mem2[load_address].next = load_data[16:8]
        Mem3[load_address].next = load_data[24:16]
        Mem4[load_address].next = load_data[32:24]

    @always(address)
    def read_logic():
        data_out.next = concat(Mem4[address], Mem3[address], Mem2[address],
                               Mem1[address])

    return instances()


@block
def testbench():
    load_data = Signal(intbv(0)[32:])
    load_address = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    address = Signal(intbv(0)[32:])
    ins = InstructionMemory_syn(load_data, load_address, address, data_out, clk)

    @always(delay(1))
    def clkgen():
        clk.next = not clk

    @instance
    def monitor():
        print("=" * 44)
        print("|address |    load data    |    data out   |")
        print("=" * 44)
        yield delay(2)
        address_counter = 0
        for i in range(3072):
            yield delay(1)
            load_address.next = i
            load_data.next = intbv(to_number(program.read(address_counter, 4), 4, True))[32:]
            address_counter += 4
            yield delay(6)
            print("| %-6s | %-15s | %-14s|" % (i * 4, load_data + 0, data_out.next + 0))
            print("=" * 44)
        print("\n\n\n")
        print("=" * 44)
        print("|             loading is done              |")
        print("=" * 44)
        print("\n\n\n")
        print("=" * 44)
        yield clk.posedge
        for i in range(3072):
            address.next = i
            yield clk.posedge
            print("| %-5s | %-15s | %-15s|" % (address.next * 4, load_data + 0, data_out.next + 0))
            print("=" * 44)

    return instances()


def convert():
    load_data = Signal(intbv(0)[32:])
    load_address = Signal(intbv(0)[32:])
    data_out = Signal(intbv(0)[32:])
    clk = Signal(bool(0))
    address = Signal(intbv(0)[32:])
    ins = InstructionMemory_syn(load_data, load_address, address, data_out, clk)
    ins.convert(hdl='Verilog')


test = testbench()
test.run_sim(100000)
# convert()
