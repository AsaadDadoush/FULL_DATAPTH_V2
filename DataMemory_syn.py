from myhdl import *
from Sys_call import obj
from memory import to_number, Memory

Program = Memory()
Program.load_binary_file(path="D:/binary_file/t1.txt", starting_address=0)
Program.load_binary_file(path="D:/binary_file/d1.txt", starting_address=8192)


@block
def DataMemory_syn(data_in, enable, size, address, data_out, clk, load_data, load_address):
    Mem1 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem2 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem3 = [Signal(intbv(0)[8:]) for i in range(3072)]
    Mem4 = [Signal(intbv(0)[8:]) for i in range(3072)]

    @always(clk.posedge)
    def load_logic():
        Mem1[load_address].next = load_data[8:]
        Mem2[load_address].next = load_data[16:8]
        Mem3[load_address].next = load_data[24:16]
        Mem4[load_address].next = load_data[32:24]
        # obj.Mem1 = Mem1
        # obj.Mem2 = Mem2
        # obj.Mem3 = Mem3
        # obj.Mem4 = Mem4

    @always_seq(clk.posedge, reset=None)
    def Write_logic():
        # if address < 0:
        #     data_in.next = 0
        # translated_address = (int(address / 4))

        if enable == 1:
            if size == 0:
                Mem1[address].next = data_in[8:0]

            elif size == 1:
                Mem1[address].next = data_in[8:0]
                Mem2[address].next = data_in[16:8]

            elif size == 2:
                Mem1[address].next = data_in[8:0]
                Mem2[address].next = data_in[16:8]
                Mem3[address].next = data_in[24:16]
                Mem4[address].next = data_in[32:24]
            else:
                Mem1[address].next = data_in[8:0]
                Mem2[address].next = data_in[16:8]
                Mem3[address].next = data_in[24:16]
                Mem4[address].next = data_in[32:24]
        # obj.Mem1 = Mem1
        # obj.Mem2 = Mem2
        # obj.Mem3 = Mem3
        # obj.Mem4 = Mem4

    @always_comb
    def Read_logic():
        # translated_address = (int(address / 4))
        # if translated_address > 3072:
        #     translated_address = 3071
        if size == 0:
            data_out.next = concat("00000000", "00000000", "00000000", Mem1[address])
        elif size == 1:
            data_out.next = concat("00000000", "00000000", Mem2[address], Mem1[address])
        else:
            data_out.next = concat(Mem4[address], Mem3[address], Mem2[address],
                                   Mem1[address])

    return instances()


@block
def test_bench():
    data_in = Signal(intbv(0, min=-2 ** 31, max=2 ** 31)[32:])
    data_out = Signal(intbv(0, min=-2 ** 31, max=2 ** 31)[32:])
    load_data = Signal(intbv(0, min=-2 ** 31, max=2 ** 31)[32:])
    load_address = Signal(intbv(0)[32:])
    enable = Signal(bool(0))
    size = Signal(intbv(0)[2:0])
    clk = Signal(bool(0))
    address = Signal(intbv(0)[32:])
    ins = DataMemory_syn(data_in, enable, size, address, data_out, clk, load_data, load_address)

    @always(delay(1))
    def clk_gen():
        clk.next = not clk

    @instance
    def stimulus():
        print("=" * 44)
        print("|address |    load data    |    data out   |")
        print("=" * 44)
        yield delay(2)
        address_counter = 0
        for i in range(3072):
            size.next = 2
            yield delay(1)
            load_address.next = i
            load_data.next = intbv(to_number(Program.read(address_counter, 4), 4, True))[32:]
            address_counter += 4
            yield delay(6)
            print("| %-5s | %-15s | %-15s|" % (i * 4, load_data + 0, data_out.next + 0))
            print("=" * 44)
        print("\n\n\n")
        print("=" * 44)
        print("|             loading is done              |")
        print("=" * 44)
        print("\n\n\n")
        yield clk.posedge
        print("=" * 58)
        print("|address |    load data    |     data out    |    Size   |")
        #################################
        size.next = 0
        yield clk.posedge
        if size.next == 0:
            temp = "Byte"
        elif size.next == 1:
            temp = "Half word"
        else:
            temp = "Word"
        ##################################
        print("=" * 58)
        for i in range(3072):
            address.next = i
            yield clk.posedge
            print("| %-6s | %-15s  | %-15s| %-9s |" % (address.next * 4, load_data + 0, data_out.next + 0, temp))
            print("=" * 58)

    return instances()


def convert():
    data_in = Signal(intbv(0, min=-2 ** 31, max=2 ** 31)[32:])
    data_out = Signal(intbv(0, min=-2 ** 31, max=2 ** 31)[32:])
    load_data = Signal(intbv(0, min=-2 ** 31, max=2 ** 31)[32:])
    load_address = Signal(intbv(0)[32:])
    enable = Signal(bool(0))
    size = Signal(intbv(0)[2:0])
    clk = Signal(bool(0))
    address = Signal(intbv(0)[32:])
    ins = DataMemory_syn(data_in, enable, size, address, data_out, clk, load_data, load_address)
    ins.convert(hdl='Verilog')


# test = test_bench()
# test.run_sim(100000)
# convert()
