module tb_InstructionMemory_syn;

reg [31:0] load_data;
reg [31:0] address;
wire [31:0] data_out;
reg clk;

initial begin
    $from_myhdl(
        load_data,
        address,
        clk
    );
    $to_myhdl(
        data_out
    );
end

InstructionMemory_syn dut(
    load_data,
    address,
    data_out,
    clk
);

endmodule
