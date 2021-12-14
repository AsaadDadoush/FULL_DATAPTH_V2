-------------------------------------------------------------------------------------------------------------------------------
				                    Team 1
            -----------------------------------------------------------------------
             Turki Safar Alzahrani	| 1935944  | Leader
             Osama Adel Alsahafi    | 1847902  | Member
             Asaad Waleed Dadoush	| 1766585  | Member
            -----------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------

# RISC-V CPU - Full data path

This CPU will work on two versions
1- Software simulation version
2- Synthesizable version

Run the main.py to choose which version do you want to run
The access of loading the binary file could be changed from DATA_PATH.py
	* Program.load_binary_file(path="   *Path for text file*  ", starting_address=0)
	* Program.load_binary_file(path="  *Path for text file*   ", starting_address=8192)

* Make sure: 
   1- The program that you want to exctue is writin based on RISC-V ISA 
   2- The address of the instruction section start at address 0 
   3- The address of the data section start at address 8192 
-------------------------------------------------------------------------------------------------------------------------------
		* For the software simulation *  
You will run the top-level that able to print the memory and register file
before and after running the implemented program which is Bubble sort.


		* For Synthesizable version *
You will run the top-level that will generate a Verilog code that could be used in
the synthesis tool (Quartus)

-------------------------------------------------------------------------------------------------------------------------------
The differences between the two versions:
You could see the differences on the code if the command commented that means the same command is exist
at the software version but not exist on the synthesizable version
-------------------------------------------------------------------------------------------------------------------------------
			* Software simulation *
1-Instruction Memory:
 	# Addresse signal is divided by 4 to manage the addressing method

2-Data Memory
	# Addresse signal is divided by 4 to manage the addressing method
	# let obj instances(Mem1, Mem2, Mem3 and Mem4) take copies of memory chunks in each write logic

3-Register File 
	# let obj instance (copy_register) take a copy of Register's in each write logic
	# Storing 10016 at register 2 "sp" to make it similar to the rars
	# Storing  6144 at register 3 "gp" to make it similar to the rars

4-Control 
	# Calling sys_call method to make the Ecall works 

5-DATA_PATH 
	# instiniate the blocks that will work with software simulation without exceptions
-------------------------------------------------------------------------------------------------------------------------------
			* Synthesizable *
1-Instruction Memory_syn:
 	# NO address will be divided by 4 

2-Data Memory_syn:
	# NO address will be divided by 4 
	# NO obj instances(Mem1, Mem2, Mem3 and Mem4)

3-Register File_syn:
	# NO obj instance (copy_register)
	# NO intilizing at register 2 "sp" 
	# NO intilizing at register 3 "gp" 

4-Control_syn: 
	# NO Calling for sys_call

5-DATA_PATH_syn:
	# instiniate the blocks that will not make any exceptions while converting the module 
	  to Verilog code
-------------------------------------------------------------------------------------------------------------------------------





