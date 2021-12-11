// File: registers.v
// Generated by MyHDL 0.11
// Date: Sat Dec 11 21:55:51 2021


`timescale 1ns/10ps

module registers (
    rs1,
    rs2,
    rd,
    rs1_out,
    rs2_out,
    enable,
    DataWrite,
    clk
);


input [4:0] rs1;
input [4:0] rs2;
input [4:0] rd;
output [31:0] rs1_out;
wire [31:0] rs1_out;
output [31:0] rs2_out;
wire [31:0] rs2_out;
input enable;
input [31:0] DataWrite;
input clk;

reg signed [31:0] Reg [0:32-1];




assign rs1_out = Reg[rs1];
assign rs2_out = Reg[rs2];


always @(posedge clk) begin: REGISTERS_WRITE_LOGIC
    if ((enable == 1)) begin
        Reg[rd] <= DataWrite;
    end
end

endmodule
