module tb_mux2_1;

reg sel;
wire [31:0] out;
reg [31:0] i0;
reg [31:0] i1;

initial begin
    $from_myhdl(
        sel,
        i0,
        i1
    );
    $to_myhdl(
        out
    );
end

mux2_1 dut(
    sel,
    out,
    i0,
    i1
);

endmodule
