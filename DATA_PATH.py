from myhdl import *
from ALU import alu
from Sys_call import obj
from control import control
from extender import extender
from Instruction_decoder import ins_dec
from memory import to_number
from memory import Memory
from mux2_1 import mux2_1
from mux4_1 import mux_4to1
from mux8_1 import mux_8to1
from PC import pc
from PC_genrator import PC_gen
from registers import registers
from shifter import shifter
from sign_extend import sign_extender
from InstructionMemory import InstructionMemory
from DataMemory import DataMemory

Program = Memory()
Program.load_binary_file(path="C:/Users/asaad/Desktop/test2/Bsort_text.txt", starting_address=0)
Program.load_binary_file(path="C:/Users/asaad/Desktop/test2/Bsort_data.txt", starting_address=8192)


@block
def top_level(Constant_4, clk,  reset,load_ins, load_data, load_address, flag):
    # ======================= Lines ======================= #
    gen_to_PC, pc_out, imm_sel, signed_extnetion_output, Data_Memory_out, Instruction_Memory_out, \
    input_for_shifter = [Signal(intbv(0)[32:]) for i in range(7)]
    rs1, rs2, rd, operation_sel = [Signal(intbv(0)[5:0]) for i in range(4)]
    immU, immJ = [Signal(intbv(0)[20:0]) for i in range(2)]
    immI, immS, immB = [Signal(intbv(0)[12:0]) for i in range(3)]
    rs1_out, rs2_out, data_in_Reg, a, b,alu_out = [Signal(intbv(0, min=-2 ** 31, max=2 ** 31)) for i in range(6)]
    imm32I, imm32S, imm32B, imm32U, imm32J = [Signal(intbv(0)[32:0]) for i in range(5)]
    opcode, func7 = [Signal(intbv(0)[7:]) for i in range(2)]
    size_sel, sign_selection = [Signal(intbv(0)[2:]) for i in range(2)]
    enable_write, PC_or_rs1 = [Signal(bool(0)) for i in range(2)]
    PC_genrator_sel, rs2_or_imm_or_4, ALU_or_load_or_immShiftedBy12, Shift_amount \
        = [Signal(intbv(0)[2:]) for i in range(4)]
    Enable_Reg = Signal(bool(0))
    func3 = Signal(intbv(0)[3:])
    shifter_out = Signal(modbv(0, min=-2 ** 31, max=2 ** 31))

    # ====================== ins section ======================= #
    PC = pc(gen_to_PC, pc_out, clk, reset, flag)  # PC
    Instruction_Memory = InstructionMemory(load_ins, load_address, pc_out, Instruction_Memory_out, clk)
    Data_Memory = DataMemory(rs2_out, enable_write, size_sel, alu_out, Data_Memory_out, clk, load_data, load_address)
    Decode = ins_dec(Instruction_Memory_out, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU,
                     immJ)  # Decoder
    cont = control(opcode, func3, func7, size_sel, operation_sel, enable_write, PC_genrator_sel, imm_sel,
                   rs2_or_imm_or_4, PC_or_rs1, ALU_or_load_or_immShiftedBy12, Shift_amount, Enable_Reg,
                   sign_selection)  # Control
    Reg = registers(rs1, rs2, rd, rs1_out, rs2_out, Enable_Reg, data_in_Reg, clk)  # Reg
    ext = extender(immI, immS, immB, immU, immJ, imm32I, imm32S, imm32B, imm32U, imm32J)  # extend for imm
    mux_Reg = mux_4to1(alu_out, signed_extnetion_output, shifter_out, ALU_or_load_or_immShiftedBy12,
                       data_in_Reg)  # mux for Reg file
    mux_imm = mux_8to1(imm32I, imm32S, imm32B, imm32U, imm32J, input_for_shifter, imm_sel)  # mux imm to shift
    shift = shifter(input_for_shifter, Shift_amount, shifter_out)  # shifter for imm
    mux_b = mux_4to1(rs2_out, shifter_out, Constant_4, rs2_or_imm_or_4, b)  # mux imm rs2 4
    mux_a = mux2_1(PC_or_rs1, a, pc_out, rs1_out)  # mux PC rs1
    ALU = alu(a, b, operation_sel, alu_out)  # ALU
    gen = PC_gen(pc_out, rs1_out, shifter_out, PC_genrator_sel, gen_to_PC, alu_out)  # PC gen
    sign_ex = sign_extender(Data_Memory_out, sign_selection, signed_extnetion_output)
    return instances()


@block
def test_bench():
    clk = Signal(bool(0))
    Constant_4 = Signal(intbv(4)[32:])
    load_ins = Signal(intbv(0)[32:])
    load_data = Signal(intbv(0)[32:])
    reset = ResetSignal(0, active=1, isasync=False)
    load_address = Signal(intbv(0)[32:])
    flag = Signal(bool(0))
    ins = top_level(Constant_4, clk,reset, load_ins, load_data, load_address, flag)

    @always(delay(14000))
    def gen_clk():
        clk.next = not clk

    @instance
    def loading():
        translated_address = 0
        print("\n # Wait Loading ....", end="\n\n")
        for i in range(3072):
            load_address.next = i
            load_ins.next = intbv(to_number(Program.read(translated_address, 4), 4, True))[32:]
            load_data.next = intbv(to_number(Program.read(translated_address, 4), 4, True))[32:]
            yield clk.posedge
            translated_address += 4

        load_address.next = 2000
        print(" # loading is done ", end="\n\n")

        print("===================================================== Memory =================="
              "==================================")
        print("|Address|     +0     |     +4     |     +8     |     +12    |     +16    |     +20    |    "
              " +24    |     +28    |")
        print("|=======+============+============+============+============+============+============+====="
              "=======+============|")
        address_p = 0
        i1 = 0
        for i in range(384):
            cell_0 = concat(obj.Mem4[i1], obj.Mem3[i1], obj.Mem2[i1], obj.Mem1[i1]) + 0
            cell_4 = concat(obj.Mem4[i1 + 1], obj.Mem3[i1 + 1], obj.Mem2[i1 + 1], obj.Mem1[i1 + 1]) + 0
            cell_8 = concat(obj.Mem4[i1 + 2], obj.Mem3[i1 + 2], obj.Mem2[i1 + 2], obj.Mem1[i1 + 2]) + 0
            cell_12 = concat(obj.Mem4[i1 + 3], obj.Mem3[i1 + 3], obj.Mem2[i1 + 3], obj.Mem1[i1 + 3]) + 0
            cell_16 = concat(obj.Mem4[i1 + 4], obj.Mem3[i1 + 4], obj.Mem2[i1 + 4], obj.Mem1[i1 + 4]) + 0
            cell_20 = concat(obj.Mem4[i1 + 5], obj.Mem3[i1 + 5], obj.Mem2[i1 + 5], obj.Mem1[i1 + 5]) + 0
            cell_24 = concat(obj.Mem4[i1 + 6], obj.Mem3[i1 + 6], obj.Mem2[i1 + 6], obj.Mem1[i1 + 6]) + 0
            cell_28 = concat(obj.Mem4[i1 + 7], obj.Mem3[i1 + 7], obj.Mem2[i1 + 7], obj.Mem1[i1 + 7]) + 0
            print("| %5s | %10s | %10s | %10s | %10s | %10s | %10s | %10s | %10s |" % (address_p, cell_0, cell_4, cell_8
                                                                                       , cell_12, cell_16, cell_20,
                                                                                       cell_24, cell_28))
            print("|-------+------------+------------+------------+------------+------------+------------+------------+"
                  "------------|")
            address_p += 32
            i1 += 8

        print("\n===== Register File =====")
        name_list = ["Zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0", "s1", "a0", "a1", "a2", "a3", "a4", "a5",
                     "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4", "t5", "t6"]
        print("| Name | Number | Value |")
        print("|======|========|=======|")
        for i in range(32):
            print("| %-5s| %5s  | %5s |" % (name_list[i], i, obj.copy_register[i] + 0))
            print("|------+--------+-------|")
        flag.next = 1
        yield clk.posedge
        reset.next = 1
        yield clk.posedge
        reset.next = 0
        yield clk.posedge
        print("\n # Processing...")

    return instances()

