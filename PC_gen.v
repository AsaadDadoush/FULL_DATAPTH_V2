// File: PC_gen.v
// Generated by MyHDL 0.11
// Date: Sat Dec 11 21:32:05 2021


`timescale 1ns/10ps

module PC_gen (
    PC,
    rs1,
    imm,
    sel,
    out,
    alu_out
);


input [31:0] PC;
input [31:0] rs1;
input [31:0] imm;
input [1:0] sel;
output [31:0] out;
reg [31:0] out;
input [31:0] alu_out;




always @(imm, alu_out, rs1, PC, sel) begin: PC_GEN_CALC_GEN
    case (sel)
        'h0: begin
            if ((alu_out == 0)) begin
                out = (PC + 4);
            end
            else begin
                out = (PC + imm);
            end
        end
        'h1: begin
            out = (PC + imm);
        end
        'h2: begin
            out = (rs1 + imm);
        end
        default: begin
            out = (PC + 4);
        end
    endcase
end

endmodule