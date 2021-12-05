import opcode

from myhdl import *


from DataMemory import copy_Mem1,copy_Mem2,copy_Mem3,copy_Mem4





def sys_Call(copy_register, copy_Mem1, copy_Mem2, copy_Mem3, copy_Mem4):
    if copy_register[17] == 93:
        raise StopSimulation
    elif copy_register[17] == 64:
        if copy_register[10] == 1:
            translated_address = int(copy_register[12] / 4)
            for i in range(translated_address):
                translated_address = int(copy_register[12] / 4)
                print(bytearray.decode(concat(copy_Mem4[translated_address],copy_Mem3[translated_address],copy_Mem2[translated_address],copy_Mem1[translated_address])), end="")
                copy_register[11] += 1



@block
def control(opcode, func3, func7, branch_result, size_sel, operation_sel, enable_write, PC_genrator_sel, imm_sel,
            rs2_or_imm_or_4, PC_or_rs1, ALU_or_load_or_immShiftedBy12, Shift_amount, Enable_Reg, sign_selection):
    @always(opcode, func7, func3)
    def control_cir():
        print("============================== Control ==============================")
        # R-type
        if opcode == 0b0110011:
            PC_or_rs1.next = 1
            rs2_or_imm_or_4.next = 0
            ALU_or_load_or_immShiftedBy12.next = 0
            PC_genrator_sel.next = 3
            Enable_Reg.next = 1
            print("R-type")
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
            ALU_or_load_or_immShiftedBy12.next = 0
            imm_sel.next = 0
            Shift_amount.next = 2
            Enable_Reg.next = 1
            print("I-type")
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
            print("I-type (LOAD instructions)")
            operation_sel.next = 0
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
            print("S-type")
            operation_sel.next = 0
            PC_genrator_sel.next = 3
            enable_write.next = 1
            PC_or_rs1.next = 1
            rs2_or_imm_or_4.next = 1
            imm_sel.next = 1
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
            imm_sel.next = 2
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
            print("Jump And Link")
            operation_sel.next = 0
            PC_genrator_sel.next = 1
            PC_or_rs1.next = 0
            rs2_or_imm_or_4.next = 2
            ALU_or_load_or_immShiftedBy12.next = 0
            imm_sel.next = 4
            Shift_amount.next = 0
            Enable_Reg.next = 1

        # I-type (Jump And Link Reg)
        elif opcode == 0b1100111:
            print("Jump And Link Reg")
            operation_sel.next = 0
            PC_genrator_sel.next = 2
            PC_or_rs1.next
            rs2_or_imm_or_4.next = 2
            ALU_or_load_or_immShiftedBy12.next = 0
            imm_sel.next = 0
            Shift_amount.next = 2
            Enable_Reg.next = 1
        # U-type (Load Upper Imm)
        elif opcode == 0b0110111:
            print("Load Upper Imm")
            PC_genrator_sel.next = 3
            ALU_or_load_or_immShiftedBy12.next = 2
            imm_sel.next = 3
            Shift_amount.next = 1
            Enable_Reg.next = 1
        # U-type (Add Upper Imm to PC)
        elif opcode == 0b1110011:
            print("Ecall")
            sys_Call(obj.copy_register, copy_Mem1,copy_Mem2,copy_Mem3,copy_Mem4)
            raise StopSimulation
        # U-type (Add Upper Imm to PC)
        else:
            print("Add Upper Imm to PC")
            operation_sel.next = 0
            Shift_amount.next = 1
            imm_sel.next = 3
            Enable_Reg.next = 1
            ALU_or_load_or_immShiftedBy12.next = 0
            PC_or_rs1.next = 0
            rs2_or_imm_or_4.next = 1
            PC_genrator_sel.next = 3

        print("Opcode : %s" % bin(opcode, 7))
        print("func3 : %s" % bin(func3, 3))
        print("func7 : %s" % bin(func7, 7))
        print('-' * 30)
        print("size_sel: ", size_sel.next + 0)
        print("operation_sel: ", operation_sel.next + 0)
        print("enable_write: ", enable_write.next + 0)
        # print("PC_genrator_sel: ", PC_genrator_sel.next + 0)
        print("imm_sel: ", imm_sel.next + 0)
        print("rs2_or_imm_or_4: ", rs2_or_imm_or_4.next + 0)

        print("PC_or_rs1: ", PC_or_rs1.next + 0)
        # print("ALU_or_load_or_immShiftedBy12: ", ALU_or_load_or_immShiftedBy12.next + 0)
        print("Shift_amount: ", Shift_amount.next + 0)
        print("Enable_Reg: ", Enable_Reg.next + 0)
        print("sign_selection: ", sign_selection.next + 0)
        print("")

    # @always(branch_result)
    # def PC_gen_logic():
    #     if opcode == 0b1100011:
    #         if branch_result == 1:
    #             print("Branch has been taken")
    #             PC_genrator_sel.next = 1
    #         else:
    #             print("Branch has not been taken")
    #             PC_genrator_sel.next = 0
    #     elif opcode == 0b1101111:
    #         PC_genrator_sel.next = 1
    #         print("PC = PC + imm")
    #     elif opcode == 0b1100111:
    #         PC_genrator_sel.next = 2
    #         print("PC = rs1 + imm")
    return instances()

class copy:
    def __init__(self):
        self.copy_register = []

    def cop(self, Reg):
        self.copy_register = Reg
        return self.copy_register

obj = copy()