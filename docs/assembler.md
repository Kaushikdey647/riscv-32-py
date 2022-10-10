# Assembler

Found in `assembler/main.py`, the assembler for this circuit is a rather basic one, written in python.

Following are the instructions available in the assembler, with description on how to use them and examples

## **HOW TO USE**

- Check the examples given in `/examples` directory
- Make sure you are in the `riscv-32-py` directory
- Run `python assembler/main.py <path_to_assembly_code> <desired_path_to_memory_image>`
- Open `circuit/riscv.circ` in logisim
- Right click on the Memory in Memory Interface in `MAIN` circuit
- Import this memory image you just created
- Press the reset settings button (***NOT the reset memory button***)
- To execute the commands, run the clock and see the commands executing sequentially

### **NOTE**: USE ASSEMBLER TO CHECK AND ENCODE THE INSTRUCTIONS

## **ADD**

- **DESCRIPTION**: Adds numbers from two registers and stores in another register. The format includes output register and two input registers
- **OPCODE**: `0000`
- **FORMAT**: `ADD R1 R2 R3` adds [R2] and [R3] and stores it in R1

## **ADI**

- **DESCRIPTION**: Adds a 16-bit immediate number to a register and stores in another register. The format includes output register, an input register and an immediate value
- **OPCODE**: `0001`
- **FORMAT**: `ADI R1 R3 100` adds [R3] and 100 and stores it in R1

## **SUB**

- **DESCRIPTION**: Subtracts numbers from two registers and stores in another register. The format includes output register and two input registers
- **OPCODE**: `0010`
- **FORMAT**: `SUB R2 R4 R5` subtracts [R5] from [R4] and stores it in R2

## **SUI**

- **DESCRIPTION**: Subtracts a 16-bit immediate number from a register and stores in another register. The format includes output register, an input register and an immediate value
- **OPCODE**: `0011`
- **FORMAT**: `SUI R1 R7 5` subtracts 5 from [R7] and stores it in R1

## **AND**

- **DESCRIPTION**: Takes bitwise and of numbers from two registers and stores in another register. The format includes output register and two input registers
- **OPCODE**: `0100`
- **FORMAT**: `AND R1 R2 R3` stores [R2] and [R3] in R1

## **ANI**

- **DESCRIPTION**: Takes bitwise and of a register and an immediate value and stores in another register. The format includes output register, an input register and an immediate value
- **OPCODE**: `0101`
- **FORMAT**: `ANI R1 R3 100` stores [R2] and 100 in R1

## **OR**

- **DESCRIPTION**: Takes bitwise or of numbers from two registers and stores in another register. The format includes output register and two input registers
- **OPCODE**: `0110`
- **FORMAT**: `OR R2 R1 R4` stores [R1] or [R4] in R2

## **MOV**

- **DESCRIPTION**: Takes bitwise or of a register and an immediate value and stores in another register. The format includes output register, an input register and an immediate value
- **OPCODE**: `1000`
- **FORMAT**: `MOV R1 R6` stores [R6] in R1

## **MVI**

- **DESCRIPTION**: Takes bitwise or of a register and an immediate value and stores in another register. The format includes output register, an input register and an immediate value
- **OPCODE**: `1001`
- **FORMAT**: `MVI R2 100` stores 100 in R2

## **LOAD**

- **DESCRIPTION**: The content of the memory location [[RB]+X] is loaded into RA, where X is a 16bit unsigned immediate value.
- **OPCODE**: `1010`
- **FORMAT**: `LOAD R1 R2 2` loads [ [R2] + 2 ] into R1

## **STORE**

- **DESCRIPTION**: The content of register RA is stored in memory location [[RB]+X] where X is again, a 16bit unsigned immediate value
- **OPCODE**: `1011`
- **FORMAT**: `STORE R1 R2 2` stores R1 into [ [R2] + 2 ]

## **COMMENTS**

- `#` is used to denote a comment.
- Every comment is ignored during transpilation
- Every empty line is ignored during a transpilation

## **EXAMPLE**

### The following is a code written in assembly

```asm
# CODE 1
# SIMPLE PROGRAM TO ADD TWO NUMBERS at 16 and 17 and storing it at 18

MVI R1 16 #BASE ADDRESS
LOAD R2 R1 0 #LOAD DATA AT 16
LOAD R3 R1 1 #LOAD DATA AT 17
ADD R4 R2 R3 #ADD IN R4
STORE R4 R1 2 #STORE AT 18
HLT
```

### The Assembler translates it to

```asm
v2.0 raw
90000010 a1000000 a2000001 03120000 b3000002 f0000000
```
**NOTE**: Each group is a 32-bit instruction