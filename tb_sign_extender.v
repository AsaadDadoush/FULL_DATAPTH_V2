module tb_sign_extender;

reg [31:0] data_in;
reg [1:0] sel;
wire [31:0] data_out;

initial begin
    $from_myhdl(
        data_in,
        sel
    );
    $to_myhdl(
        data_out
    );
end

sign_extender dut(
    data_in,
    sel,
    data_out
);

endmodule
