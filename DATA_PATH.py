from myhdl import *
from ALU import alu
from control import control
from extender import extender
from Instruction_decoder import ins_dec
from mux2_1 import mux2_1
from mux3_1 import mux_3to1, mux_3to1_for_Register
from Mux8_1 import mux8_1
from PC import pc
from PC_genrator import PC_gen
from registers import registers
from shifter import shifter
from sign_extend import sign_extender
from InstructionMemory import InstructionMemory
from DataMemory import DataMemory

main_memory = None


@block
def top_level(Constant_4, clk, reset):
    # ======================= Lines ======================= #
    gen_to_PC = Signal(modbv(1, min=0, max=83*4)[32:])
    pc_out = Signal(modbv(1, min=0, max=83*4)[32:])
    Instruction_Memory_out = Signal(intbv(0)[32:])
    rs1 = Signal(intbv(0)[5:0])
    rs2 = Signal(intbv(0)[5:0])
    immU = Signal(intbv(0)[20:0])
    immJ = Signal(intbv(0)[20:0])
    immI = Signal(intbv(0)[12:0])
    immS = Signal(intbv(0)[12:0])
    immB = Signal(intbv(0)[12:0])
    rd = Signal(intbv(0)[5:])
    rs1_out = Signal(intbv(0, min=-2**31, max=2**31))
    rs2_out = Signal(intbv(0, min=-2**31, max=2**31))
    data_in_Reg = Signal(intbv(0, min=-2**31, max=2**31))
    imm32I = Signal(intbv(0)[32:0])
    imm32S = Signal(intbv(0)[32:0])
    imm32B = Signal(intbv(0)[32:0])
    imm32U = Signal(intbv(0)[32:0])
    imm32J = Signal(intbv(0)[32:0])
    opcode = Signal(intbv(0)[7:])
    func3 = Signal(intbv(0)[5:])
    func7 = Signal(intbv(0))
    size_sel = Signal(intbv(2)[2:])
    operation_sel = Signal(intbv(0)[5:])
    enable_write = Signal(bool(0))
    PC_genrator_sel = Signal(intbv(0)[2:])
    imm_sel = Signal(intbv(0)[32:])
    rs2_or_imm_or_4 = Signal(intbv(0)[2:])
    PC_or_rs1 = Signal(bool(0))
    ALU_or_load_or_immShiftedBy12 = Signal(intbv(0)[2:])
    Shift_amount = Signal(intbv(0)[2:])
    Enable_Reg = Signal(bool(1))
    # todo modbv
    input_for_shifter = Signal(intbv(0)[32:])
    # todo modbv
    shifter_out = Signal(modbv(0, min=-2**31, max=2**31))
    a = Signal(intbv(0, min=-2**31, max=2**31))
    b = Signal(intbv(0, min=-2**31, max=2**31))
    alu_out = Signal(intbv(0)[32:0])
    sign_selection = Signal(intbv(2)[2:])
    signed_extnetion_output = Signal(intbv(0)[32:])
    Data_Memory_out = Signal(intbv(0)[32:])

    # ======================= ins section ======================= #

    # ========= input == out ============
    PC = pc(gen_to_PC, pc_out, clk, reset)  # PC

    # =================================== sel ======= out === i0 ==== i1
    # mux_PC_or_ALU_to_memory = mux2_1_pcANDalu(PC_or_Address, addres, pc_out, alu_out)  # mux PC or ALU to memory

    # =================== input == Data in == enable ========== output ===========

    # Main_memory = memory(rs2_out, enable_write, size_sel, pc_out, alu_out, Instruction_Memory_out)
    Instruction_Memory = InstructionMemory(pc_out, Instruction_Memory_out)
    Data_Memory = DataMemory(rs2_out, enable_write, size_sel, alu_out, Data_Memory_out, clk)
    # Main_memory = memory(Instruction_Memory_out, pc_out)
    # ================== input =============
    Decode = ins_dec(Instruction_Memory_out, opcode, rd, func3, rs1, rs2, func7, immI, immS, immB, immU,
                     immJ)  # Decoder
    cont = control(opcode, func3, func7, alu_out, size_sel, operation_sel, enable_write, PC_genrator_sel, imm_sel,
                   rs2_or_imm_or_4, PC_or_rs1, ALU_or_load_or_immShiftedBy12, Shift_amount, Enable_Reg,
                   sign_selection)  # Control
    # ================== inputs ========== outputs================== input
    Reg = registers(rs1, rs2, rd, rs1_out, rs2_out, Enable_Reg, data_in_Reg,clk)  # Reg

    ext = extender(immI, immS, immB, immU, immJ, imm32I, imm32S, imm32B, imm32U, imm32J)  # extend for imm
    mux_Reg = mux_3to1_for_Register(alu_out, signed_extnetion_output, shifter_out, ALU_or_load_or_immShiftedBy12,
                                    data_in_Reg)  # mux for Reg file
    mux_imm = mux8_1(imm32I, imm32S, imm32B, imm32U, imm32J, input_for_shifter, imm_sel)  # mux imm to shift
    # ===============input============== sel========== output
    shift = shifter(input_for_shifter, Shift_amount, shifter_out)  # shifter for imm
    # ====================== inputs ================ sel ===== out
    mux_b = mux_3to1(rs2_out, shifter_out, Constant_4, rs2_or_imm_or_4, b)  # mux imm rs2 4
    # ============= sel == out===== inputs
    mux_a = mux2_1(PC_or_rs1, a, pc_out, rs1_out)  # mux PC rs1
    ALU = alu(a, b, operation_sel, alu_out)  # ALU
    # ======================== inputs ============= sel ========= out
    gen = PC_gen(pc_out, rs1_out, shifter_out, PC_genrator_sel, gen_to_PC, alu_out)  # PC gen

    sign_ex = sign_extender(Data_Memory_out, sign_selection, signed_extnetion_output)
    return instances()



@block
def test_bench():
    clk = Signal(bool(0))
    reset = Signal(bool(1))
    Constant_4 = Signal(intbv(4)[32:])
    ins = top_level(Constant_4, clk, reset)

    @always(delay(14000))
    def gen_clk():
        clk.next = not clk
    return instances()


test = test_bench()
test.run_sim()
