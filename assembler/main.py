import sys




instruction_encoding = {
    "HLT": [0, "0000"],
    "ORI": [3, "0001"],
    "OR": [3, "0010"],
    "ANI": [3, "0010"],
    "AND": [3, "0010"],
    "ADI": [3, "0010"],
    "ADD": [3, "0010"],
    "SUI": [3, "0010"],
    "SUB": [3, "0010"],
    "LOAD": [3, "0010"],
    "MOV": [3, "0010"],
    "MVI": [2, "0010"],
    "STORE": [3, "0010"]
}

register_encoding = {
    "R1": 0,
    "R2": 1,
    "R3": 2,
    "R4": 3,
    "R5": 4,
    "R6": 5,
    "R7": 6,
    "R8": 7
}


def bin_to_hex(bin_str):
    if( len(bin_str) != 32 ):
        return None
    return hex(int( bin_str, 2))


def process_line(instr_str,line_num):
    tokens = [ tok.strip() for tok in instr_str.split(" ") ]
    if len(tokens) > 4:
        print("INVALID STATEMENT AT LINE ", line_num," : ", instr_str)
        print("Extra tokens detected")
    instruction = tokens[0]


if __name__ == '__main__':
    try:
        filepath = sys.argv[1]
    except:
        print("No File Provided")
        exit()

    with open(filepath) as file:
        lines = file.readlines()
    
    for i,line in enumerate(lines):
        print(line)
        # print(process_line(line, i))