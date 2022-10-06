# riscv-32-c
A RISC Processor with a 5 stage pipeline and 32-bit instruction set.

## DESCRIPTION

This repository is created by **Kaushik Dey (20CS01043, IIT Bhubaneswar)** as a submission for the **Assignment 4** (Mini Project) of **Computer Organization and Architecture Lab** Course in Autumn of 2022

## INSTRUCTION SET

The instuction set needed to define for the processor are

- **`MOVE RA, RB`**: Content of RB is transferred to RA
- **`MOVE RA, Im`**: The Immediate value Im is stored in RA
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

## HOW TO USE

## DELIVERABLES (for the Assignment)

- A readme file (this).
- The Logisim circuit files.
- Block level diagram of the implementation.
- 5 stage architecture overview
- Assembler Table
- Encoding Scheme

## INSTRUCTIONS PROVIDED

- Programs start from memory address 0
- Atleast 4 GPRs should be included
- All registers are 32bit
- Control Unit should be designed using hardwired control mechanism.
- Memory should have enough space to store 32 instructions and 32 data.
- Provide a reset signal that sets the value of PC to 0