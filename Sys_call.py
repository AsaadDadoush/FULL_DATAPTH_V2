import math
from myhdl import *


class copy:
    def __init__(self):
        self.copy_register = []
        self.Mem1 = []
        self.Mem2 = []
        self.Mem3 = []
        self.Mem4 = []


obj = copy()


def sys_Call(copy_register, Mem1, Mem2, Mem3, Mem4):
    if copy_register[17] == 93:
        print("# Software simulation is done\n")
        print_method(copy_register, Mem1, Mem2, Mem3, Mem4)
        raise StopSimulation
    elif copy_register[17] == 64:
        if copy_register[10] == 1:
            print("-"*32)
            print("Console: ")
            base_address = int(copy_register[11] / 4)
            for i in range(math.ceil(copy_register[12] / 4)):
                m1 = Mem1[base_address]
                m2 = Mem2[base_address]
                m3 = Mem3[base_address]
                m4 = Mem4[base_address]
                print("%s%s%s%s" % (chr(m1), chr(m2), chr(m3), chr(m4)), end="")
                base_address = base_address + 1
            print("")
            print("-" * 32)
            print("\n")


def print_method(copy_register, Mem1, Mem2, Mem3, Mem4):
    while True:
        a = input(
            "# Availabe Choices\n To print Memory press 1 \n To print Register File press 2 \n To print both press"
            " 3 \n To Exit press 4 \nChoice: ")
        if a == "1":
            print(
                "===================================================== Memory ====================================="
                "===============")
            print(
                "|Address|     +0     |     +4     |     +8     |     +12    |     +16    |     +20    |     +24   "
                " |     +28    |")
            print(
                "|=======+============+============+============+============+============+============+==========="
                "=+============|")
            address_p = 0
            i1 = 0
            for i in range(384):
                cell_0 = concat(Mem4[i1], Mem3[i1], Mem2[i1], Mem1[i1]) + 0
                cell_4 = concat(Mem4[i1 + 1], Mem3[i1 + 1], Mem2[i1 + 1], Mem1[i1 + 1]) + 0
                cell_8 = concat(Mem4[i1 + 2], Mem3[i1 + 2], Mem2[i1 + 2], Mem1[i1 + 2]) + 0
                cell_12 = concat(Mem4[i1 + 3], Mem3[i1 + 3], Mem2[i1 + 3], Mem1[i1 + 3]) + 0
                cell_16 = concat(Mem4[i1 + 4], Mem3[i1 + 4], Mem2[i1 + 4], Mem1[i1 + 4]) + 0
                cell_20 = concat(Mem4[i1 + 5], Mem3[i1 + 5], Mem2[i1 + 5], Mem1[i1 + 5]) + 0
                cell_24 = concat(Mem4[i1 + 6], Mem3[i1 + 6], Mem2[i1 + 6], Mem1[i1 + 6]) + 0
                cell_28 = concat(Mem4[i1 + 7], Mem3[i1 + 7], Mem2[i1 + 7], Mem1[i1 + 7]) + 0
                print("| %5s | %10s | %10s | %10s | %10s | %10s | %10s | %10s | %10s |" % (
                    address_p, cell_0, cell_4, cell_8, cell_12, cell_16, cell_20, cell_24, cell_28))
                print(
                    "|-------+------------+------------+------------+------------+------------+------------+------------+------------|")
                address_p += 32
                i1 += 8
        elif a == "2":
            print("\n===== Register File =====")
            name_list = ["Zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0", "s1", "a0", "a1", "a2", "a3", "a4",
                         "a5", "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4",
                         "t5", "t6"]
            print("| Name | Number | Value |")
            print("|======|========|=======|")
            for i in range(32):
                print("| %-5s| %5s  | %5s |" % (name_list[i], i, copy_register[i] + 0))
                print("|------+--------+-------|")
        elif a == "3":
            print(
                "===================================================== Memory ====================================================")
            print(
                "|Address|     +0     |     +4     |     +8     |     +12    |     +16    |     +20    |     +24    |     +28    |")
            print(
                "|=======+============+============+============+============+============+============+============+============|")
            address_p = 0
            i1 = 0
            for i in range(384):
                cell_0 = concat(Mem4[i1], Mem3[i1], Mem2[i1], Mem1[i1]) + 0
                cell_4 = concat(Mem4[i1 + 1], Mem3[i1 + 1], Mem2[i1 + 1], Mem1[i1 + 1]) + 0
                cell_8 = concat(Mem4[i1 + 2], Mem3[i1 + 2], Mem2[i1 + 2], Mem1[i1 + 2]) + 0
                cell_12 = concat(Mem4[i1 + 3], Mem3[i1 + 3], Mem2[i1 + 3], Mem1[i1 + 3]) + 0
                cell_16 = concat(Mem4[i1 + 4], Mem3[i1 + 4], Mem2[i1 + 4], Mem1[i1 + 4]) + 0
                cell_20 = concat(Mem4[i1 + 5], Mem3[i1 + 5], Mem2[i1 + 5], Mem1[i1 + 5]) + 0
                cell_24 = concat(Mem4[i1 + 6], Mem3[i1 + 6], Mem2[i1 + 6], Mem1[i1 + 6]) + 0
                cell_28 = concat(Mem4[i1 + 7], Mem3[i1 + 7], Mem2[i1 + 7], Mem1[i1 + 7]) + 0
                print("| %5s | %10s | %10s | %10s | %10s | %10s | %10s | %10s | %10s |" % (
                    address_p, cell_0, cell_4, cell_8, cell_12, cell_16, cell_20, cell_24, cell_28))
                print(
                    "|-------+------------+------------+------------+------------+------------+------------+------------+------------|")
                address_p += 32
                i1 += 8
            print("\n===== Register File =====")
            name_list = ["Zero", "ra", "sp", "gp", "tp", "t0", "t1", "t2", "s0", "s1", "a0", "a1", "a2", "a3", "a4",
                         "a5", "a6", "a7", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "t3", "t4",
                         "t5", "t6"]
            print("| Name | Number | Value |")
            print("|======|========|=======|")
            for i in range(32):
                print("| %-5s| %5s  | %5s |" % (name_list[i], i, copy_register[i] + 0))
                print("|------+--------+-------|")
        elif a == "4":
            print("# Thank you ")
            break
        else:
            print(" * Wrong Choise, Try again *")


