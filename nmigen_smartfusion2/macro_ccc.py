
def get_ccc_macro():
    silicon_macro = '`timescale 1 ns/100 ps\n\
// Version: v2021.1 2021.1.0.17\n\
\n\
\n\
module CCC_50MHZ_RCOSC_IN_100MHZ_OUT(\n\
       RCOSC_25_50MHZ,\n\
       LOCK,\n\
       GL0\n\
    );\n\
input  RCOSC_25_50MHZ;\n\
output LOCK;\n\
output GL0;\n\
\n\
    wire gnd_net, vcc_net, GL0_net;\n\
    \n\
    VCC vcc_inst (.Y(vcc_net));\n\
    GND gnd_inst (.Y(gnd_net));\n\
    CLKINT GL0_INST (.A(GL0_net), .Y(GL0));\n\
    CCC #( .INIT(210\'h0000007FB8000044D74000318C6318C1F18C61EC0404040400301)\n\
        , .VCOFREQUENCY(800.000) )  CCC_INST (.Y0(), .Y1(), .Y2(), .Y3(\n\
        ), .PRDATA({nc0, nc1, nc2, nc3, nc4, nc5, nc6, nc7}), .LOCK(\n\
        LOCK), .BUSY(), .CLK0(vcc_net), .CLK1(vcc_net), .CLK2(vcc_net), \n\
        .CLK3(vcc_net), .NGMUX0_SEL(gnd_net), .NGMUX1_SEL(gnd_net), \n\
        .NGMUX2_SEL(gnd_net), .NGMUX3_SEL(gnd_net), .NGMUX0_HOLD_N(\n\
        vcc_net), .NGMUX1_HOLD_N(vcc_net), .NGMUX2_HOLD_N(vcc_net), \n\
        .NGMUX3_HOLD_N(vcc_net), .NGMUX0_ARST_N(vcc_net), \n\
        .NGMUX1_ARST_N(vcc_net), .NGMUX2_ARST_N(vcc_net), \n\
        .NGMUX3_ARST_N(vcc_net), .PLL_BYPASS_N(vcc_net), .PLL_ARST_N(\n\
        vcc_net), .PLL_POWERDOWN_N(vcc_net), .GPD0_ARST_N(vcc_net), \n\
        .GPD1_ARST_N(vcc_net), .GPD2_ARST_N(vcc_net), .GPD3_ARST_N(\n\
        vcc_net), .PRESET_N(gnd_net), .PCLK(vcc_net), .PSEL(vcc_net), \n\
        .PENABLE(vcc_net), .PWRITE(vcc_net), .PADDR({vcc_net, vcc_net, \n\
        vcc_net, vcc_net, vcc_net, vcc_net}), .PWDATA({vcc_net, \n\
        vcc_net, vcc_net, vcc_net, vcc_net, vcc_net, vcc_net, vcc_net})\n\
        , .CLK0_PAD(gnd_net), .CLK1_PAD(gnd_net), .CLK2_PAD(gnd_net), \n\
        .CLK3_PAD(gnd_net), .GL0(GL0_net), .GL1(), .GL2(), .GL3(), \n\
        .RCOSC_25_50MHZ(RCOSC_25_50MHZ), .RCOSC_1MHZ(gnd_net), .XTLOSC(\n\
        gnd_net));\n\
    \n\
endmodule\n'

    return silicon_macro

