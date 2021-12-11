module tb_registers;

reg [4:0] rs1;
reg [4:0] rs2;
reg [4:0] rd;
wire [31:0] rs1_out;
wire [31:0] rs2_out;
reg enable;
reg [31:0] DataWrite;
reg clk;

initial begin
    $from_myhdl(
        rs1,
        rs2,
        rd,
        enable,
        DataWrite,
        clk
    );
    $to_myhdl(
        rs1_out,
        rs2_out
    );
end

registers dut(
    rs1,
    rs2,
    rd,
    rs1_out,
    rs2_out,
    enable,
    DataWrite,
    clk
);

endmodule
