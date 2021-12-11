// File: pc.v
// Generated by MyHDL 0.11
// Date: Sat Dec 11 21:17:48 2021


`timescale 1ns/10ps

module pc (
    data_in,
    out,
    clk,
    flag
);


input [31:0] data_in;
output [31:0] out;
reg [31:0] out;
input clk;
input flag;




always @(posedge clk) begin: PC_PCBLOCK
    if ((flag == 1)) begin
        out <= data_in;
    end
end

endmodule