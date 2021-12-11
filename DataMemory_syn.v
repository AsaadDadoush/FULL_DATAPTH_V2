// File: DataMemory_syn.v
// Generated by MyHDL 0.11
// Date: Sat Dec 11 20:01:50 2021


`timescale 1ns/10ps

module DataMemory_syn (
    data_in,
    enable,
    size,
    address,
    data_out,
    clk
);


input [31:0] data_in;
input enable;
input [1:0] size;
input [31:0] address;
output [31:0] data_out;
reg [31:0] data_out;
input clk;

reg [7:0] Mem1 [0:8-1];
reg [7:0] Mem2 [0:8-1];
reg [7:0] Mem3 [0:8-1];
reg [7:0] Mem4 [0:8-1];



always @(posedge clk) begin: DATAMEMORY_SYN_WRITE_LOGIC
    if ((enable == 1)) begin
        case (size)
            'h0: begin
                Mem1[address] <= data_in[8-1:0];
            end
            'h1: begin
                Mem1[address] <= data_in[8-1:0];
                Mem2[address] <= data_in[16-1:8];
            end
            'h2: begin
                Mem1[address] <= data_in[8-1:0];
                Mem2[address] <= data_in[16-1:8];
                Mem3[address] <= data_in[24-1:16];
                Mem4[address] <= data_in[32-1:24];
            end
            default: begin
                Mem1[address] <= data_in[8-1:0];
                Mem2[address] <= data_in[16-1:8];
                Mem3[address] <= data_in[24-1:16];
                Mem4[address] <= data_in[32-1:24];
            end
        endcase
    end
end


always @(address, Mem4[0], Mem4[1], Mem4[2], Mem4[3], Mem4[4], Mem4[5], Mem4[6], Mem4[7], size, Mem2[0], Mem2[1], Mem2[2], Mem2[3], Mem2[4], Mem2[5], Mem2[6], Mem2[7], Mem1[0], Mem1[1], Mem1[2], Mem1[3], Mem1[4], Mem1[5], Mem1[6], Mem1[7], Mem3[0], Mem3[1], Mem3[2], Mem3[3], Mem3[4], Mem3[5], Mem3[6], Mem3[7]) begin: DATAMEMORY_SYN_READ_LOGIC
    case (size)
        'h0: begin
            data_out = {8'b00000000, 8'b00000000, 8'b00000000, Mem1[address]};
        end
        'h1: begin
            data_out = {8'b00000000, 8'b00000000, Mem2[address], Mem1[address]};
        end
        default: begin
            data_out = {Mem4[address], Mem3[address], Mem2[address], Mem1[address]};
        end
    endcase
end

endmodule
