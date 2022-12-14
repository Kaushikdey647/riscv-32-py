# riscv-32-c
A RISC Processor with a 5 stage pipeline and 32-bit instruction set.

## CONTENTS

- [Circuit Manual](/docs/circuit.md)
- [Encoding Scheme](/docs/encoding-scheme.md)
- [Assembler Manual](/docs/assembler.md)
- [Five Stage Architecture Explained](/docs/datapath.md)
- [Control Signals and Control Unit](/docs/control-signals.md)

## DESCRIPTION

This repository is created by **Kaushik Dey (20CS01043, IIT Bhubaneswar)** as a submission for the **Assignment 4** (Mini Project) of **Computer Organization and Architecture Lab** Course in Autumn of 2022

## PREREQUISITES

- python (version 3.6 or above)
- logisim (original, avoid logisim evolution)

## HOW TO USE

- Open up the circuit in [`/circuits/riscv.circ`](/circuits/riscv.circ) in logisim
- Refer to Assembler Manual and write your assembly code.
- Assemble your code using the script at [`/assembler/main.py`](/assembler/main.py)
- Go to `MAIN` section in circuit and right click on the memory and load the code into the circuit.
- Run the code by executing the clock (`Ctrl+T` repeatedly)

### **NOTE**: USE ASSEMBLER TO CHECK AND ENCODE THE INSTRUCTIONS

The assembler can be found at assembler/main.py



## INSTRUCTION SET

The instuction set needed to define for the processor are

- **`MOV RA RB`**: Content of RB is transferred to RA
- **`MVI RA Im`**: The Immediate value Im is stored in RA
- **`LOAD RA RB X`**: The content of the memory location [[RB]+X] is loaded into RA, where X is a 16bit unsigned immediate value
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


## DELIVERABLES (for the Assignment)

- A readme file (this).
- The Logisim circuit files. *(go to the [circuits folder](/circuits) )*
- Block level diagram of the implementation. *(go to the [circuit manual](/docs/circuit.md) )*
- 5 stage architecture overview *(go to the [Pipeline Overview](/docs/datapath.md))*
- Assembler Manual *(go to the [Assembler Manual](/docs/assembler.md))*
- Encoding Scheme *(go to the [Encoding Scheme](/docs/encoding-scheme.md))*

## INSTRUCTIONS PROVIDED

- Programs start from memory address 0
- Atleast 4 GPRs should be included
- All registers are 32bit
- Control Unit should be designed using hardwired control mechanism.
- Memory should have enough space to store 32 instructions and 32 data.
- Provide a reset signal that sets the value of PC to 0
