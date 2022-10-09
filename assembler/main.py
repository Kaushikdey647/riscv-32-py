import sys


instruction_encoding = {
    "add": 0,
    "adi": 1,
    "sub": 2,
    "sui": 3,
    "and": 4,
    "ani": 5,
    "or": 6,
    "ori": 7,
    "mov": 8,
    "mvi": 9,
    "load": 10,
    "store": 11,
    "hlt": 15
}

register_encoding = {
    "r1": 0,
    "r2": 1,
    "r3": 2,
    "r4": 3,
    "r5": 4,
    "r6": 5,
    "r7": 6,
    "r8": 7
}

def convert_line(line,index):
    if(line.find('#') >= 0): line = line[:line.index('#')] #ignore commands
    line = line.replace('\n','').strip().lower()
    if len(line) == 0: return None #Empty Line
    tokens = line.split()
    if len(tokens) > 4 : raise Exception("POSSIBLE ILLEGAL HARDWARE INSTRUCTION AT LINE: ", index)
    
    #PREDEFINING THE LABELS
    try:
        opcode = instruction_encoding[ tokens[0] ]
    except:
        raise Exception("INVALID OPCODE AT LINE: ",index)
    ra = 0
    rb = 0
    ry = 0
    im = 0

    # 3 REGISTER FORMAT
    if opcode in [0,2,4,6]:
        if len(tokens) != 4: raise Exception("INVALID INSTRUCTION FORMAT AT: ", index)
        try:
            ry = register_encoding[ tokens[1] ]
            ra = register_encoding[ tokens[2] ]
            rb = register_encoding[ tokens[3] ]
        except:
            raise Exception("INVALID REGISTER AT LINE: ", index)

    # 2 REGISTER 1 CONSTANT FORMAT
    elif opcode in [1,3,5,7,10,11]:
        if len(tokens) != 4: raise Exception("INVALID INSTRUCTION FORMAT AT: ", index)
        try:
            ry = register_encoding[ tokens[1] ]
            ra = register_encoding[ tokens[2] ]
            im = int(tokens[3])
        except:
            raise Exception("INVALID REGISTER AT LINE: ", index)

    # 2 REGISTER 1 CONSTANT FORMAT
    elif opcode in [1,3,5,7,10,11]:
        if len(tokens) != 4: raise Exception("INVALID INSTRUCTION FORMAT AT: ", index)
        try:
            ry = register_encoding[ tokens[1] ]
            ra = register_encoding[ tokens[2] ]
            im = int(tokens[3])
        except:
            raise Exception("INVALID REGISTER AT LINE: ", index)

    # 2 REGISTER FORMAT (MOV)
    elif opcode == 8:
        if len(tokens) != 3: raise Exception("INVALID INSTRUCTION FORMAT AT: ", index)
        try:
            ry = register_encoding[ tokens[1] ]
            ra = register_encoding[ tokens[2] ]
        except:
            raise Exception("INVALID REGISTER AT LINE: ", index)

    # 1 REGISTER 1 CONSTANT FORMAT (MVI)
    elif opcode == 9:
        if len(tokens) != 3: raise Exception("INVALID INSTRUCTION FORMAT AT: ", index)
        try:
            ry = register_encoding[ tokens[1] ]
            im = int(tokens[2])
        except:
            raise Exception("INVALID REGISTER AT LINE: ", index)
   
    # HALT OP
    elif opcode == 15:
        pass
    
    else:
        raise Exception("Unknown Hardware Instruction at line: ", index)

    return merge_hex(opcode,ry,ra,rb,im)

def merge_hex(opcode,ry,ra,rb,im):
    return hex(opcode%0x10)[2:] + hex(ry%0x10)[2:] + hex(ra%0x10)[2:] + hex(rb%0x10)[2:] + '{0:0{1}X}'.format(im%0x10000,4)

if __name__ == '__main__':
    try:
        input_filename = sys.argv[1]
    except IndexError:
        print('Usage: command inputfile outputfile \n\r')
        sys.exit()
    try:
        output_filename = sys.argv[2]
    except IndexError:
        output_filename = 'memimg'
    
    input = open(input_filename)
    output = open(output_filename, mode = 'w')

    output.write('v2.0 raw')

    for i,line in enumerate(input):
        if i%8 == 0: output.write('\n')
        if len(line.strip()) > 0:
            if line.strip()[0] == '#': continue
            hexcode = convert_line(line, i)
            output.write(hexcode+' ')
    
    input.close()
    output.close()
