module tb_mux8_1;

reg [31:0] i0;
reg [31:0] i1;
reg [31:0] i2;
reg [31:0] i3;
reg [31:0] i4;
wire [31:0] out;
reg [2:0] sel;

initial begin
    $from_myhdl(
        i0,
        i1,
        i2,
        i3,
        i4,
        sel
    );
    $to_myhdl(
        out
    );
end

mux8_1 dut(
    i0,
    i1,
    i2,
    i3,
    i4,
    out,
    sel
);

endmodule
