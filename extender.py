from myhdl import *


@block
def extender(immI, immS, immB, immU, immJ, imm32I, imm32S, imm32B, imm32U, imm32J):
    @always(immI, immS, immB, immU, immJ)
    def extend():
        imm32I.next = immI.signed()[32:]
        imm32S.next = immS.signed()[32:]
        imm32B.next = immB.signed()[32:]
        imm32U.next = immU.signed()[32:]
        imm32J.next = immJ.signed()[32:]
        print("============================ imm Extender ===========================")
        print("-------------- inputs ---------------")
        print("immI: ", bin(immI, 12), " = ", immI+0)
        print("immS: ", bin(immS, 12), " = ",immS+0)
        print("immB: ", bin(immB, 12), " = ",immB+0)
        print("immU: ", bin(immU, 20), " = ",immU+0)
        print("immJ: ", bin(immJ, 20), " = ",immJ+0)
        print("-------------- Outputs --------------")
        print("immI: ", bin(imm32I.next, 32))
        print("immS: ", bin(imm32S.next, 32))
        print("immB: ", bin(imm32B.next, 32))
        print("immU: ", bin(imm32U.next, 32))
        print("immJ: ", bin(imm32J.next, 32))
        print("")
    return extend

