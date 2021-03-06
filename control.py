from Sys_call import obj, sys_Call
from myhdl import *


@block
def control(opcode, func3, func7, size_sel, operation_sel, enable_write, PC_genrator_sel, imm_sel,
            rs2_or_imm_or_4, PC_or_rs1, ALU_or_load_or_immShiftedBy12, Shift_amount, Enable_Reg, sign_selection):
    @always_comb
    def control_cir():
        # R-type
        if opcode == 0b0110011:
            PC_or_rs1.next = 1
            rs2_or_imm_or_4.next = 0
            enable_write.next = 0
            ALU_or_load_or_immShiftedBy12.next = 0
            PC_genrator_sel.next = 3
            Enable_Reg.next = 1

            # ADD
            if func3 == 0x0 and func7 == 0x00:
                operation_sel.next = 0
            # SUB
            elif func3 == 0x0 and func7 == 0x20:
                operation_sel.next = 0

            # XOR
            elif func3 == 0x4 and func7 == 0x00:
                operation_sel.next = 5
            # OR
            elif func3 == 0x6 and func7 == 0x00:
                operation_sel.next = 4

            # AND
            elif func3 == 0x7 and func7 == 0x00:
                operation_sel.next = 3

            # Shift Left logical
            elif func3 == 0x1 and func7 == 0x00:
                operation_sel.next = 6


            # Shift Right logical
            elif func3 == 0x5 and func7 == 0x00:
                operation_sel.next = 7

            # Shift Right Arith*
            elif func3 == 0x5 and func7 == 0x20:
                operation_sel.next = 13

            # set less than
            elif func3 == 0x2 and func7 == 0x00:
                operation_sel.next = 10

            # set less than(U)
            elif func3 == 0x3 and func7 == 0x00:
                operation_sel.next = 11

            # MUL
            elif func3 == 0x0 and func7 == 0x01:
                operation_sel.next = 1


            # DIV
            elif func3 == 0x4 and func7 == 0x01:
                operation_sel.next = 2


            # DIV(U)
            elif func3 == 0x5 and func7 == 0x01:
                operation_sel.next = 15


            # Remainder
            elif func3 == 0x6 and func7 == 0x01:
                operation_sel.next = 16

            # Remainder (U)
            else:
                operation_sel.next = 17

        # I-type
        elif opcode == 0b0010011:
            PC_or_rs1.next = 1
            rs2_or_imm_or_4.next = 1
            enable_write.next = 0
            ALU_or_load_or_immShiftedBy12.next = 0
            imm_sel.next = 0
            Shift_amount.next = 2
            Enable_Reg.next = 1

            # Add imm
            if func3 == 0x0:
                operation_sel.next = 0
                PC_genrator_sel.next = 3
            # XOR imm
            elif func3 == 0x4:
                operation_sel.next = 5
                PC_genrator_sel.next = 3
            # OR imm
            elif func3 == 0x6:
                operation_sel.next = 4
                PC_genrator_sel.next = 3
            # AND imm
            elif func3 == 0x7:
                operation_sel.next = 3
                PC_genrator_sel.next = 3
            # Shift left logical imm
            elif func3 == 0x1 and func7 == 0x00:
                operation_sel.next = 6
                PC_genrator_sel.next = 3
            # Shift right logical imm
            elif func3 == 0x5 and func7 == 0x00:
                operation_sel.next = 7
                PC_genrator_sel.next = 3
            # Shift right Arith imm
            elif func3 == 0x5 and func7 == 0x20:
                operation_sel.next = 13
                PC_genrator_sel.next = 3

            # Set less than imm
            elif func3 == 0x2:
                operation_sel.next = 10
                PC_genrator_sel.next = 3

            # Set less than imm (U)
            else:
                operation_sel.next = 11
                PC_genrator_sel.next = 3
        # I-type (LOAD instructions)
        elif opcode == 0b0000011:

            operation_sel.next = 0
            enable_write.next = 0
            PC_genrator_sel.next = 3
            PC_or_rs1.next = 1
            rs2_or_imm_or_4.next = 1
            ALU_or_load_or_immShiftedBy12.next = 1
            imm_sel.next = 0
            Shift_amount.next = 2
            Enable_Reg.next = 1
            # load Byte
            if func3 == 0x0:
                size_sel.next = 0
                sign_selection.next = 0

            # load Half
            elif func3 == 0x1:
                size_sel.next = 1
                sign_selection.next = 1

            # load Word
            elif func3 == 0b010:
                size_sel.next = 2
                sign_selection.next = 2

            # load Byte(U)
            elif func3 == 0x4:
                size_sel.next = 0
                sign_selection.next = 2

            # load Half(U)
            else:
                size_sel.next = 1
                sign_selection.next = 2

        # S-Type
        elif opcode == 0b0100011:

            operation_sel.next = 0
            PC_genrator_sel.next = 3
            enable_write.next = 1
            PC_or_rs1.next = 1
            rs2_or_imm_or_4.next = 1
            imm_sel.next = 1
            Enable_Reg.next = 0
            Shift_amount.next = 2
            # Store Byte
            if func3 == 0x0:
                size_sel.next = 0

            # Store Half
            elif func3 == 0x1:
                size_sel.next = 1

            # Store word
            else:
                size_sel.next = 2

        # B-type
        elif opcode == 0b1100011:
            PC_or_rs1.next = 1
            rs2_or_imm_or_4.next = 0
            enable_write.next = 0
            imm_sel.next = 2
            Enable_Reg.next = 0
            Shift_amount.next = 0
            # Branch ==
            if func3 == 0x0:
                operation_sel.next = 8
                PC_genrator_sel.next = 0
            # Branch !=
            elif func3 == 0x1:
                operation_sel.next = 9
                PC_genrator_sel.next = 0
            # Branch <
            elif func3 == 0x4:
                operation_sel.next = 10
                PC_genrator_sel.next = 0
            # Branch <=
            elif func3 == 0x5:
                operation_sel.next = 12
                PC_genrator_sel.next = 0
            # Branch <(U)
            elif func3 == 0x6:
                operation_sel.next = 11
                PC_genrator_sel.next = 0

            # Branch >=(U)
            else:
                PC_genrator_sel.next = 0
                operation_sel.next = 14

        # J-type (Jump And Link)
        elif opcode == 0b1101111:

            operation_sel.next = 0
            PC_genrator_sel.next = 1
            enable_write.next = 0
            PC_or_rs1.next = 0
            rs2_or_imm_or_4.next = 2
            ALU_or_load_or_immShiftedBy12.next = 0
            imm_sel.next = 4
            Shift_amount.next = 0
            Enable_Reg.next = 1

        # I-type (Jump And Link Reg)
        elif opcode == 0b1100111:

            operation_sel.next = 0
            PC_genrator_sel.next = 2
            enable_write.next = 0
            rs2_or_imm_or_4.next = 2
            ALU_or_load_or_immShiftedBy12.next = 0
            imm_sel.next = 0
            Shift_amount.next = 2
            Enable_Reg.next = 1
        # U-type (Load Upper Imm)
        elif opcode == 0b0110111:

            PC_genrator_sel.next = 3
            enable_write.next = 0
            ALU_or_load_or_immShiftedBy12.next = 2
            imm_sel.next = 3
            Shift_amount.next = 1
            Enable_Reg.next = 1
        # Ecall
        elif opcode == 0b1110011:
            Enable_Reg.next = 0
            sys_Call(obj.copy_register, obj.Mem1, obj.Mem2, obj.Mem3, obj.Mem4)
        # U-type (Add Upper Imm to PC)
        else:
            operation_sel.next = 0
            enable_write.next = 0
            Shift_amount.next = 1
            imm_sel.next = 3
            Enable_Reg.next = 1
            ALU_or_load_or_immShiftedBy12.next = 0
            PC_or_rs1.next = 0
            rs2_or_imm_or_4.next = 1
            PC_genrator_sel.next = 3

    return instances()

