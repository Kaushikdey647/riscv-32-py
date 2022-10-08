# Encoding Scheme

## ENCODING SCHEME

The proposed encoding scheme for the circuit would be:

- **31-28**: `OPCODE`
- **27-25**: `RY`
- **24-22**: `RA`
- **21-19**: `RB`
- **21-06**: `Immediate`

## INSTRUCTION SET

The instuction set needed to define for the processor are

- **`MOV RA RB`**: Content of RB is transferred to RA
- **`MVI RA Im`**: The Immediate value Im is stored in RA
- **`LOAD RA RB X `**: The content of the memory location [[RB]+X] is loaded into RA, where X is a 16bit unsigned immediate value
- **`STORE RA RB X`**: The content of register RA is stored in memory location [[RB]+X] where X is again, a 16bit unsigned immediate value
- **`ADD RA RB RC`**: RA = RB + RC
- **`ADI RA RB Im`**: RA = RB + Im, where Im is a 32-bit unsigned extended immediate value
- **`SUB RA RB RC`**: RA = RB - RC
- **`SUI RA RB Im`**: RA = RB - Im, where Im is a 32-bit unsigned extended immediate value
- **`AND RA RB RC`**: RA = RB AND RC
- **`ANI RA RB IM`**: RA = RB AND Im, where Im is a 32-bit unsigned extended immediate value
- **`OR RA RB RC`**: RA = RB OR RC
- **`ORI RA RB IM`**: RA = RB OR Im, where Im is a 32-bit unsigned extended immediate value
- **`HLT`**

## INSTRUCTION ENCODING

The OPCODES FOR THE OPERATIONS ARE WITH ALU MAPPING :
- **`ADD`**: 0000 (0) (SUM)
- **`ADI`**: 0001 (1) (SUM)
- **`SUB`**: 0010 (2) (DIFF)
- **`SUI`**: 0011 (3) (DIFF)
- **`AND`**: 0100 (4) (AND)
- **`ANI`**: 0101 (5) (AND)
- **`OR`**: 0110 (6) (OR)
- **`ORI`**: 0111 (7) (ORI)
- **`MOV`**: 1000 (8) (RA)
- **`MVI`**: 1001 (9) (RB)
- **`LOAD`**: 1010 (10) (SUM)
- **`STORE`**: 1011 (11) (SUM)
- **`HLT`**: 1111 (15) (NOP)

## REGISTER ENCODING

There are 8 registers available, those are:
- **`R1`**: 000
- **`R2`**: 001
- **`R3`**: 010
- **`R4`**: 011
- **`R5`**: 100
- **`R6`**: 101
- **`R7`**: 110
- **`R8`**: 111

**NOTE**: The immediate values are 16-bit

**NOTE**: 0-1 of OPCODE is ALU_SELECT

## LITERAL ENCODING

- All literals are expected to be in hexadecimal, if not found, they are converted into hex.
- All immediate values would be capped at 16 bit


## INSTRUCTION EXAMPLE

For example the instruction

`ADI R2 R1 56`

would translate to:

 ` 0010 001 000 0000000000111000 000000 `
 
 Note that the last 6 bits are not used, nevenrtheless, grouping into 4, we have:
 
 ` 0010 0010 0000 0000 0000 1110 0000 0000 `
 
 And converting into hex, we have
 
 ### `22000E00`
