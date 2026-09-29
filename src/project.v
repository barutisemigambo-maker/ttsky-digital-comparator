`default_nettype none

module tt_um_baruti_digital_comparator (
    input  wire [7:0] ui_in,     // A input
    output wire [7:0] uo_out,    // Comparator outputs
    input  wire [7:0] uio_in,    // B input
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire ena,
    input  wire clk,
    input  wire rst_n
);

    // Digital Comparator
    // ui_in = A
    // uio_in = B

    assign uo_out[0] = (ui_in > uio_in);   // A > B
    assign uo_out[1] = (ui_in == uio_in);  // A = B
    assign uo_out[2] = (ui_in < uio_in);   // A < B

    // Unused outputs
    assign uo_out[7:3] = 5'b00000;

    // Bidirectional pins are not used
    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    // Unused control signals
    wire _unused = &{ena, clk, rst_n, 1'b0};

endmodule