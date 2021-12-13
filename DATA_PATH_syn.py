from myhdl import *

from ALU import alu
from control_syn import control_syn
from extender import extender
from Instruction_decoder import ins_dec
from memory import to_number
from memory import Memory
from mux2_1 import mux2_1
from mux4_1 import mux_4to1
from mux8_1 import mux_8to1
from PC import pc
from PC_genrator import PC_gen
from registers_syn import registers_syn
from shifter import shifter
from sign_extend import sign_extender
from InstructionMemory_syn import InstructionMemory_syn
from DataMemory_syn import DataMemory_syn

# Program = Memory()
# Program.load_binary_file(path="D:/binary_file/t1.txt", starting_address=0)
# Program.load_binary_file(path="D:/binary_file/d1.txt", starting_address=8192)


@block
def top_level(Constant_4, clk,  reset,load_ins, load_data, load_address, flag):
    # ======================= Lines ======================= #
    gen_to_PC, pc_out, imm_sel, signed_extnetion_output, Data_Memory_out, alu_out, Instruction_Memory_out, \
    input_for_shifter = [Signal(intbv(0)[32:]) for i in range(8)]
    rs1, rs2, rd, operation_sel = [Signal(intbv(0)[5:0]) for i in range(4)]
    immU, immJ = [Signal(intbv(0)[20:0]) for i in range(2)]
    immI, immS, immB = [Signal(intbv(0)[12:0]) for i in range(3)]
    rs1_out, rs2_out, data_in_Reg, a, b = [Signal(intbv(0, min=-2 ** 31, max=2 ** 31)) for i in range(5)]
    imm32I, imm32S, imm32B, imm32U, imm32J = [Signal(intbv(0)[32:0]) for i in range(5)]
    opcode, func7 = [Signal(intbv(0)[7:]) for i in range(2)]
    size_sel, sign_selection = [Signal(intbv(0)[2:]) for i in range(2)]
    enable_write, PC_or_rs1 = [Signal(bool(0)) for i in range(2)]
    PC_genrator_sel, rs2_or_imm_or_4, ALU_or_load_or_immShiftedBy12, Shift_amount \
        = [Signal(intbv(0)[2:]) for i in range(4)]
    Enable_Reg = Signal(bool(0))
    func3 = Signal(intbv(0)[3:])
    shifter_out = Signal(modbv(0, min=-2 ** 31, max=2 ** 31))

    # ======================= ins section ======================= #
    PC = pc(gen_to_PC, pc_out, clk, reset, flag)  # PC
    # Main_memory = memory(rs2_out, enable_write, size_sel, pc_out, alu_out, Instruction_Memory_out)
    Instruction_Memory = InstructionMemory_syn(load_ins, load_address, pc_out, Instruction_Memory_out, clk)
    Data_Memory = DataMemory_syn(rs2_out, enable_write, size_sel, alu_out, Data_Memory_out, clk, load_data, load_address)
    Decode = ins_dec(Instruction_Memory_out, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU,
                     immJ)  # Decoder
    cont = control_syn(opcode, func3, func7, size_sel, operation_sel, enable_write, PC_genrator_sel, imm_sel,
                   rs2_or_imm_or_4, PC_or_rs1, ALU_or_load_or_immShiftedBy12, Shift_amount, Enable_Reg,
                   sign_selection)  # Control
    Reg = registers_syn(rs1, rs2, rd, rs1_out, rs2_out, Enable_Reg, data_in_Reg, clk)  # Reg

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


def convert():
    clk = Signal(bool(0))
    Constant_4 = Signal(intbv(4)[32:])
    load_ins = Signal(intbv(0)[32:])
    load_data = Signal(intbv(0)[32:])
    reset = ResetSignal(0, active=1, isasync=False)
    load_address = Signal(intbv(0)[32:])
    flag = Signal(bool(0))
    ins = top_level(Constant_4, clk, reset, load_ins, load_data, load_address, flag)
    ins.convert(hdl='Verilog')

convert()

