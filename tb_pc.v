module tb_pc;

reg [31:0] data_in;
wire [31:0] out;
reg clk;
reg flag;

initial begin
    $from_myhdl(
        data_in,
        clk,
        flag
    );
    $to_myhdl(
        out
    );
end

pc dut(
    data_in,
    out,
    clk,
    flag
);

endmodule
