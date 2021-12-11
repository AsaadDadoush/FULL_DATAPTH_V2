module tb_DataMemory_syn;

reg [31:0] data_in;
reg enable;
reg [1:0] size;
reg [31:0] address;
wire [31:0] data_out;
reg clk;

initial begin
    $from_myhdl(
        data_in,
        enable,
        size,
        address,
        clk
    );
    $to_myhdl(
        data_out
    );
end

DataMemory_syn dut(
    data_in,
    enable,
    size,
    address,
    data_out,
    clk
);

endmodule
