from myhdl import *


@block
def extender(immI, immS, immB, immU, immJ, imm32I, imm32S, imm32B, imm32U, imm32J):
    @always_comb
    def extend():
        imm32I.next = immI.signed()[32:]
        imm32S.next = immS.signed()[32:]
        imm32B.next = immB.signed()[32:]
        imm32U.next = immU.signed()[32:]
        imm32J.next = immJ.signed()[32:]

    return extend

