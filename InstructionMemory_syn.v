// File: InstructionMemory_syn.v
// Generated by MyHDL 0.11
// Date: Sat Dec 11 20:16:27 2021


`timescale 1ns/10ps

module InstructionMemory_syn (
    load_data,
    address,
    data_out,
    clk
);


input [31:0] load_data;
input [31:0] address;
output [31:0] data_out;
reg [31:0] data_out;
input clk;

reg [7:0] Mem1 [0:3072-1];
reg [7:0] Mem2 [0:3072-1];
reg [7:0] Mem3 [0:3072-1];
reg [7:0] Mem4 [0:3072-1];



always @(posedge clk) begin: INSTRUCTIONMEMORY_SYN_LOAD_LOGIC
    Mem1[address] <= load_data[8-1:0];
    Mem2[address] <= load_data[16-1:8];
    Mem3[address] <= load_data[24-1:16];
    Mem4[address] <= load_data[32-1:24];
end


always @(address) begin: INSTRUCTIONMEMORY_SYN_READ_LOGIC
    data_out <= {Mem4[address], Mem3[address], Mem2[address], Mem1[address]};
end

endmodule