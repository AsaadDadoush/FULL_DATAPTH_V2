from myhdl import *
import DATA_PATH
import DATA_PATH_syn


print("="*60)
print("                             Team 1")
print("            --------------------------------------------")
print("             Turki Safar Alzahrani	| 1935944  | Leader")
print("             Osama Adel Alsahafi    | 1847902  | Member")
print("             Asaad Waleed Dadoush	| 1766585  | Member")
print("            --------------------------------------------")
while True:
    choice = input("\n To run Software simulation Mode press 1 \n To run The Synthesizable Mode press 2 \nChoice: ")
    if choice == "1" or choice == "2":
        break
    else:
        print("  # Wrong Choice")
print("="*60)

if choice == "1":
    print("\n==================== Software simulation ===================")
    test = DATA_PATH.test_bench()
    test.run_sim()
elif choice == "2":
    test = DATA_PATH_syn.convert()
    print(" \nFull Synthesis is done, you can see the Verilog code in the same directory")
    print("")



