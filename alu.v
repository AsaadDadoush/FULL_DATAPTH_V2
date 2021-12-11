// File: alu.v
// Generated by MyHDL 0.11
// Date: Sat Dec 11 22:14:51 2021


`timescale 1ns/10ps

module alu (
    a,
    b,
    sel,
    out
);


input signed [31:0] a;
input signed [31:0] b;
input [4:0] sel;
output signed [31:0] out;
reg signed [31:0] out;




always @(a, b, sel) begin: ALU_ALU
    integer v;
    case (sel)
        'h0: begin
            v = (a + b);
            if ((v < 0)) begin
                out = 0;
            end
            else begin
                out = v;
            end
        end
        'h1: begin
            out = (a * b);
        end
        'h2: begin
            out = (a / b);
        end
        'h3: begin
            out = (a & b);
        end
        'h4: begin
            out = (a | b);
        end
        'h5: begin
            out = (a ^ b);
        end
        'h6: begin
            out = (a << $signed({1'b0, b[5-1:0]}));
        end
        'h7: begin
            out = $signed(a >>> b[5-1:0]);
        end
        'h8: begin
            if ((a == b)) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'h9: begin
            if ((a != b)) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'ha: begin
            if ((a < b)) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'hb: begin
            if ((a < b[32-1:0])) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'hc: begin
            if ((a >= b)) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'hd: begin
            out = $signed(a >>> b[5-1:0]);
        end
        'he: begin
            if ((a > b[32-1:0])) begin
                out = 1;
            end
            else begin
                out = 0;
            end
        end
        'hf: begin
            out = (a / b[32-1:0]);
        end
        'h10: begin
            out = (a % b);
        end
        default: begin
            out = (a % b[32-1:0]);
        end
    endcase
end

endmodule