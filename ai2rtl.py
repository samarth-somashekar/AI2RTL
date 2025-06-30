import os

def generate_verilog(description):
    description = description.lower()
    if "4-bit counter" in description:
        return """module counter(input clk, reset, output reg [3:0] count);
    always @(posedge clk or posedge reset)
        if (reset) count <= 0;
        else count <= count + 1;
endmodule"""
    return "// Unsupported description"

def save_io(description, verilog_code, folder="verilog_output"):
    os.makedirs(folder, exist_ok=True)
    idx = len(os.listdir(folder)) + 1
    with open(f"{folder}/gen_{idx}.txt", "w") as f:
        f.write("Input Description:\n")
        f.write(description + "\n\n")
        f.write("Generated Verilog:\n")
        f.write(verilog_code + "\n")
