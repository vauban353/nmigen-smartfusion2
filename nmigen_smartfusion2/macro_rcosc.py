
def get_rcosc_macro():
  silicon_macro = 'module RCOSC_1MHZ ( \n\
  CLKOUT );\n\
\n\
/* synthesis syn_black_box */\n\
/* synthesis syn_noprune=1 */\n\
\n\
output CLKOUT;\n\
\n\
endmodule\n\
\n\
module RCOSC_25_50MHZ ( \n\
  CLKOUT );\n\
\n\
/* synthesis syn_black_box */\n\
/* synthesis syn_noprune=1 */\n\
\n\
output CLKOUT;\n\
\n\
parameter FREQUENCY = 50.0;\n\
\n\
endmodule\n\
\n\
module XTLOSC ( \n\
  CLKOUT,\n\
  XTL );\n\
\n\
/* synthesis syn_black_box */\n\
/* synthesis syn_noprune=1 */\n\
/* synthesis black_box_pad_pin =\"XTL\" */\n\
\n\
output CLKOUT;\n\
input XTL;\n\
\n\
parameter MODE = \'h3;\n\
parameter FREQUENCY = 20.0;\n\
\n\
endmodule\n\
\n\
module RCOSC_1MHZ_FAB ( \n\
  CLKOUT,\n\
  A );\n\
\n\
/* synthesis syn_black_box */\n\
/* synthesis syn_noprune=1 */\n\
\n\
output CLKOUT;\n\
input A;\n\
\n\
endmodule\n\
\n\
module RCOSC_25_50MHZ_FAB ( \n\
  CLKOUT,\n\
  A );\n\
\n\
/* synthesis syn_black_box */\n\
/* synthesis syn_noprune=1 */\n\
\n\
output CLKOUT;\n\
input A;\n\
\n\
endmodule\n\
\n\
module XTLOSC_FAB ( \n\
  CLKOUT,\n\
  A );\n\
\n\
/* synthesis syn_black_box */\n\
/* synthesis syn_noprune=1 */\n\
\n\
output CLKOUT;\n\
input A;\n\
\n\
endmodule\n'

  return silicon_macro
