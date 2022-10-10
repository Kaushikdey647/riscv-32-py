# Circuit Manual

![Main Circuit Image](/docs/images/main.png)


In this document, we shall have an in depth look into the circuit of the processor and its components. Furthermore, we shall have a look 

## Components
<hr>

The **key** components of this processor are

- The **ALU**
- The **CU**
- The **Memory Interface**
- The **Instruction Address Generator**
- The **Instruction Decoder**
- The **Datapath**

## Arithmetic and Logic Unit (ALU)
<hr>

![ALU](/docs/images/alu.png)

The ALU, for now, has no flags, and supports only four operations:

- ADD
- SUB
- AND
- OR

It takes in two inputs `INPUT_A` and `INPUT_B` and gives out the result of the operation in `OUTPUT`. The parameter used for the operations is given by input `ALU_SELECT` and it also uses another control signal `ALU_ENABLE` to function

## Register File

<hr>

![RF](/docs/images/register-file.png)

The RF, or Register File, houses a family of registers that stores the temporary usage data for the datapath. It has interface to 8 General Purpose Registers and 3 muxes to select the register to use to store data from `RY` or to channel data to `RA` and `RB`.

Each register has a Enable Write Pin, Clock, Clear, Input and Output attached to it. Furthermore, it has 3 MUXes.

- `RA SELECT` selects the register to feed data to RA
- `RB SELECT` selects the register to feed data to RA
- `WRITE SELECT` selects the register to input data from RY

Pins that we use for the register are `ENABLE_RO_SELECT`, `ENABLE_RA_SELECT` and `ENABLE_RB_SELECT` to activate the registers, and `SELECT_RA`, `SELECT_RB` and `SELECT_RO` to refer their addresses. 

Data comes in via `DATA_IN` and goes out to RA and RB via `RA_OUT` and `RB_OUT` respectively

Furthermore, its worth mentioning that we use another pin `RO_RB_BYPASS` to bypass RO value directly into RB in case of `STORE` instruction. More of which we shall come into later.

## Memory Interface

<hr>

![MI](/docs/images/memory-interface.png)

The Memory Interface is the abstraction around memory which consists of various control and data signal tunnels. All of them are described below

- `MEM_ADDR` takes in the address where data needs to be written to/read from
- `RM_OUTPUT` takes in the output from RM register (from the datapath) and feeds into the Memory. It needs the `MEM_WRITE` signal to be active in order to write succesfully
- `MEM_OUTPUT` tunnels the output from the memory. It shares the data stored at [`MEM_ADDR`] and needs `MEM_READ` signal to be active to read succesfully.
- `MEM_CLEAR` is used to clear the memory
- `CLK` is clock (obviously)

## Instruction Address Generator

<hr>

![IAG](/docs/images/iag.png)

The IAG in this processor is responsible for generating the address to read the instructions from the memory. It starts at address 0000 and proceeds to next segment incrementing by 1. It needs the following signals to function:
- `CLOCK` as the system clock, `PC_ENABLE` to see if the PC needs to be incremented, `CLEAR` to reset the PC back to 0
- `PC` pin is used to output the current address (16-bit)
- Its only notable constituents are the PC Register, and an adder that increments the register and these pins.

## Instruction Decoder

<hr>

![IAG](/docs/images/decoder.png)

The instruction decoder is responsible for extracting the data from the 32bit instruction. All the codes in this processor architecture are non-overlapping and uses the entirety of 32-bits to represent the instruction. More about the same in the [encoding scheme](/docs/encoding-scheme.md).

The input pins are:

- `INPUT`: The 32bit Input being put into the IR(INSTRUCTION REGISTER)
- `IR_ENABLE`: Enables the usage of IR
- `IR_CLEAR`: Clears the IR

Output pins are:

- `OPCODE`: The 4-bit opcode
 - `RA_SELECT`: The 4-bit address of RA
- `RB_SELECT`: The 4-bit address of RB
- `RY_SELECT`: The 4-bit address of RY
- `IMMEDIATE`: The 16-bit immediate value

The interface around Instruction Decoder in the MAIN Circuit looks something like

![IAG-Interface](/docs/images/instruction-decoder.png)

- Note that `MEM_OUTPUT` is being channelled into `INPUT` and the outputs are being channelled into their respective pins for control signals or output

![IAG-Interface](/docs/images/opcode-decoder.png)

- The OPCODE is being fed into this MUX here for further decoding into the respective operation channel. These operations trigger respective control signals in the control unit.

## Instruction Datapath

<hr>

![DATAPATH](/docs/images/datapath/datapath.png)

The datapath is THE most significant and active component of the processor. All the other components are built around it and according to its convenience.

The datapath of our 32-bit RISC processor is a 5 stage pipeline, each stage executing a specific part in completing the instruction. More about that [here](/docs/datapath.md)

## Control Unit

<hr>

![CU](/docs/images/cu-interface.png)

The control unit takes in signals for all the instructions and stages and triggers respective signals in the dataline and several other components. It is being extensively discussed [here](/docs/control-signals.md)