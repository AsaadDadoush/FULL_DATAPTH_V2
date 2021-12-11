module tb_control;

reg [6:0] opcode;
reg [2:0] func3;
reg [6:0] func7;
wire [1:0] size_sel;
wire [4:0] operation_sel;
wire enable_write;
wire [1:0] PC_genrator_sel;
wire [2:0] imm_sel;
wire [1:0] rs2_or_imm_or_4;
wire PC_or_rs1;
wire [1:0] ALU_or_load_or_immShiftedBy12;
wire [1:0] Shift_amount;
wire Enable_Reg;
wire [1:0] sign_selection;

initial begin
    $from_myhdl(
        opcode,
        func3,
        func7
    );
    $to_myhdl(
        size_sel,
        operation_sel,
        enable_write,
        PC_genrator_sel,
        imm_sel,
        rs2_or_imm_or_4,
        PC_or_rs1,
        ALU_or_load_or_immShiftedBy12,
        Shift_amount,
        Enable_Reg,
        sign_selection
    );
end

control dut(
    opcode,
    func3,
    func7,
    size_sel,
    operation_sel,
    enable_write,
    PC_genrator_sel,
    imm_sel,
    rs2_or_imm_or_4,
    PC_or_rs1,
    ALU_or_load_or_immShiftedBy12,
    Shift_amount,
    Enable_Reg,
    sign_selection
);

endmodule
