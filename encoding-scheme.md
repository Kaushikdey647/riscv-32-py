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

- **`MOV RA, RB`**: Content of RB is transferred to RA
- **`MVI RA, Im`**: The Immediate value Im is stored in RA
- **`LOAD RA, X(RB)`**: The content of the memory location [[RB]+X] is loaded into RA, where X is a 16bit unsigned immediate value
- **`STORE RA, X(RB)`**: The content of register RA is stored in memory location [[RB]+X] where X is again, a 16bit unsigned immediate value
- **`ADD RA, RB, RC`**: RA = RB + RC
- **`ADI RA, RB, Im`**: RA = RB + Im, where Im is a 32-bit unsigned extended immediate value
- **`SUB RA, RB, RC`**: RA = RB - RC
- **`SUI RA, RB, Im`**: RA = RB - Im, where Im is a 32-bit unsigned extended immediate value
- **`AND RA, RB, RC`**: RA = RB AND RC
- **`ANI RA, RB, IM`**: RA = RB AND Im, where Im is a 32-bit unsigned extended immediate value
- **`OR RA, RB, RC`**: RA = RB OR RC
- **`ORI RA, RB, IM`**: RA = RB OR Im, where Im is a 32-bit unsigned extended immediate value
- **`HLT`**

## INSTRUCTION ENCODING

The OPCODES FOR THE OPERATIONS ARE:
- **`MOV`**: 0010
- **`MVI`**: 0011
- **`LOAD`**: 0010
- **`STORE`**: 0010
- **`ADD`**: 0010
- **`ADI`**: 0010
- **`SUB`**: 0010
- **`SUI`**: 0010
- **`AND`**: 0010
- **`ANI`**: 0010
- **`OR`**: 0010
- **`ORI`**: 0010

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

## INSTRUCTION EXAMPLE

For example the instruction

`ADI R2 R1 #56`

would translate to:

 ` 0010 001 000 0000000000111000 000000 `
 
 Note that the last 6 bits are not used, nevenrtheless, grouping into 4, we have:
 
 ` 0010 0010 0000 0000 0000 1110 0000 0000 `
 
 And converting into hex, we have
 
 ### `22000E00`
