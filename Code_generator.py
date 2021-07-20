import numpy as np
import argparse

parser = argparse.ArgumentParser(description='LOG_LUT_code_generator')
parser.add_argument('-iw', '--Input_width', metavar='N', type=int, default='32',
                    help='Input data width, max 64')
parser.add_argument('-fw', '--Frac_width', metavar='N', type=int, default='8',
                    help='Output fractional width, fixed point; max 16')

args = parser.parse_args()

if (args.Input_width>64):
	print("ERROR: Input width too large, max is 64 bits")
	exit()
if (args.Frac_width>16):
	print("ERROR: Output fractional width too large, max is 16 bits")
	exit()
	
in_width      = args.Input_width
# Out width
frac_width    = args.Frac_width
integer_width = int(np.floor(np.log2(in_width-1))+1)
out_width     = integer_width + frac_width
LUT_input     = np.linspace(0,2**frac_width,2**frac_width,endpoint=False, dtype=np.uint32)

LUT_output = np.log2(1+LUT_input/(1<<frac_width))*((1<<frac_width))
LUT_output = LUT_output.round()
LUT_output = LUT_output.astype(np.uint32)

f = open('LOG_LUT.v', 'w')
f.write('`timescale 1ns / 1ps\n')
f.write('\n')
f.write('\n')
f.write('// Code generated by python script made by Gabriele Bortolato\n')
f.write('\n')
f.write('\n')
f.write('// Computation of base-2 logarithm with axi4 lite comunication protocol\n')
f.write('// Input  --> %d bits integer\n' % in_width)
f.write('// Output --> %d bits fixed point format (%d_fix_%d)\n' % (out_width, out_width, frac_width))
f.write('\n')
f.write('module LOG_LUT\n')
f.write('#(\n')
f.write('    // Parameters.\n')
f.write('    parameter DATA_IN_WIDTH  = %d,     // Input axis data width\n' % (in_width)                )
f.write('    parameter DATA_OUT_WIDTH = %d      // Output data width\n'     % (out_width))
f.write(')\n')
f.write('(\n')
f.write('    input aresetn,\n')
f.write('    input aclk,\n')
f.write('    \n')
f.write('    //input\n')
f.write('    input [DATA_IN_WIDTH-1:0] s_axis_din_tdata,\n')
f.write('    input s_axis_din_tlast,\n')
f.write('    input [15:0] s_axis_din_tuser,\n')
f.write('    input s_axis_din_tvalid,\n')
f.write('    output s_axis_din_tready,\n')
f.write('    \n')
f.write('    //output\n')
f.write('    output  [DATA_OUT_WIDTH-1:0] m_axis_dout_tdata,\n')
f.write('    output  m_axis_dout_tlast,\n')
f.write('    input m_axis_dout_tready,\n')
f.write('    output  [15:0] m_axis_dout_tuser,\n')
f.write('    output  m_axis_dout_tvalid\n')
f.write(');\n')
f.write("    reg [%d:0] LUT_input_1    = %d'b0;\n"  % (frac_width-1,frac_width))
f.write("    \n")
f.write("    reg [%d:0] LUT_output_2    = %d'b0;\n" % (frac_width-1,frac_width))
f.write("    \n")
f.write("    reg [DATA_IN_WIDTH-1:0] data_in_0 = 64'b0;\n")
f.write("    \n")
f.write("    reg [DATA_OUT_WIDTH-1:0] data_out_0 = %d'b0;\n" % (out_width))
f.write("    reg [DATA_OUT_WIDTH-1:0] data_out_1 = %d'b0;\n" % (out_width))
f.write("    reg [DATA_OUT_WIDTH-1:0] data_out_2 = %d'b0;\n" % (out_width))
f.write("    reg [DATA_OUT_WIDTH-1:0] data_out_3 = %d'b0;\n" % (out_width))
f.write("    \n")    
f.write("    reg tvalid_0    = 1'b0;\n")
f.write("    reg tvalid_1    = 1'b0;\n")
f.write("    reg tvalid_2    = 1'b0;\n")
f.write("    reg tvalid_3    = 1'b0;\n")
f.write("    \n")    
f.write("    reg tlast_0    = 1'b0;\n")
f.write("    reg tlast_1    = 1'b0;\n")
f.write("    reg tlast_2    = 1'b0;\n")
f.write("    reg tlast_3    = 1'b0;\n")
f.write("    \n")   
f.write("    reg [15:0] tuser_0    = 16'b0;\n")
f.write("    reg [15:0] tuser_1    = 16'b0;\n")
f.write("    reg [15:0] tuser_2    = 16'b0;\n")
f.write("    reg [15:0] tuser_3    = 16'b0;\n")
f.write("    \n")
f.write("    reg [5:0] prienc;\n")
f.write("    \n")
f.write("    \n")
f.write("    always @(posedge aclk)  //priority encoder\n")
f.write("    begin\n")
f.write("    \n")
f.write("        if      (s_axis_din_tdata [%d]==1'b1)   prienc <=	%d'd%d;    // Highest Priority\n" 
        % (in_width-1, integer_width, in_width-1))
for i in range(in_width-2, 0 ,-1):
    f.write("        else if (s_axis_din_tdata [%d]==1'b1)   prienc <=	%d'd%d;\n" 
            % (i, integer_width, i))
f.write("        else                                    prienc <=	6'd00;\n")
f.write("        \n")
f.write("    \n")    
f.write("    end\n")
f.write("    \n") 
f.write("    \n") 
f.write("    always @(posedge aclk)\n")
f.write("    begin\n")
f.write("        if (!aresetn) begin\n")
f.write("            data_in_0 <= 1'b0;\n")
f.write("        end\n")
f.write("        \n")
f.write("        else begin\n")
f.write("            \n")
f.write("            tvalid_0 <= s_axis_din_tvalid;\n")
f.write("            tvalid_1 <= tvalid_0;\n")
f.write("            tvalid_2 <= tvalid_1;\n")
f.write("            tvalid_3 <= tvalid_2;\n")
f.write("            \n")
f.write("            tlast_0 <= s_axis_din_tlast;\n")
f.write("            tlast_1 <= tlast_0;\n")
f.write("            tlast_2 <= tlast_1;\n")
f.write("            tlast_3 <= tlast_2;\n")
f.write("            \n")
f.write("            tuser_0 <= s_axis_din_tuser;\n")
f.write("            tuser_1 <= tuser_0;\n")
f.write("            tuser_2 <= tuser_1;\n")
f.write("            tuser_3 <= tuser_2;\n")
f.write("            \n")
f.write("            data_in_0 <= s_axis_din_tdata;\n")
f.write("            \n")
f.write("            LUT_input_1      <= ((data_in_0-(64'b1<<prienc))<<(DATA_IN_WIDTH-prienc)>>(DATA_IN_WIDTH-%d));\n" % (frac_width))
f.write("            //pipeline computing\n")
f.write("            case(LUT_input_1)\n")
for i in range(2**frac_width):
    f.write("            %d'd%d: LUT_output_2 <= %d'd%d;\n" % ((out_width),LUT_input[i],(out_width),LUT_output[i]))
f.write("        endcase\n")

f.write("        if (prienc == 6'b000000) begin\n")
f.write("            data_out_1  <= %d'd0;\n" % (out_width))
f.write("        end\n")
f.write("        else begin\n")
f.write("            data_out_1  <= prienc<<%d;\n" % frac_width)
f.write("        end\n")
f.write("        data_out_2  <= data_out_1;\n")
f.write("        data_out_3  <= data_out_2 + (LUT_output_2);\n")
f.write("    end\n")
f.write("    \n")    
f.write("    assign m_axis_dout_tdata    = data_out_3;\n")
f.write("    assign m_axis_dout_tlast    = tlast_3;\n")
f.write("    assign m_axis_dout_tuser    = tuser_3;\n")
f.write("    assign m_axis_dout_tvalid   = tvalid_3;\n")
f.write("    \n") 
f.write("    assign s_axis_din_tready    = m_axis_dout_tready;\n")
f.write("    \n")
f.write("endmodule\n")

f.close()

N = 5000000

Test_input    = np.random.randint(1,2**in_width-1,N, dtype=np.uint64)
Exact_output  = np.log2(Test_input)
prienc_out    = np.array(np.log2(Test_input), dtype=np.uint64)
frac_out      = np.array(((Test_input - 2**prienc_out)*2**(in_width-prienc_out))/(2**(in_width-frac_width)), dtype=np.uint32)
Comp_output   = ((prienc_out<<frac_width) + LUT_output[frac_out])/2**frac_width
Error         = Exact_output - Comp_output

print("Expected deviation from 'ideality'")
print("Mean error               = %e" % np.mean(Error))
print("Standard deviation error = %e" % np.std( Error))

