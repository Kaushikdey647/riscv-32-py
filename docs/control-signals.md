# Control Unit and the Control Signals

![CU](/docs/images/control-unit/control-unit.png)

- The control system is responsible for the orchestration of the entire processor. It has mostly non-sequential components, and doesn't use up any cpu time. There is only one sequential components and it is the counter for the 5-stage architecture.

- The CU used in this project is based on hardwired control mechanism.

- A signal exists for each operation and each stage. And each signal has a role in triggering some respective control signals.

We shall go into in-depth analysis of signals associated with every stage, and question the logic behind the same.

## TEMPLATES

Here we defined some templates to group some signals together for ease of circuit representation.

![TEMP](/docs/images/control-unit/cu-temp.png)

## COUNTER

![CTR](/docs/images/control-unit/cu-counter.png)

- We also have a 3-bit counter in the CU, that counts the stages of the pipeline.

## STAGE 1

![S1](/docs/images/control-unit/cu-1.png)

![MC](/docs/images/control-unit/cu-instr.png)

- In stage 1, every instruction, except HLT, triggers `IR_ENABLE` and `PC_ENABLE` enabling us to read the memory address of the instruction from PC and subsequently read the instruction into IR.

- For all the 13 instructions (`TYPE_4`), we trigger `MEM_READ` so that the instruction can be fetched from memory.

## STAGE 2

![S2](/docs/images/control-unit/cu-stage-2.png)

- In stage 2, if the instruction is `STORE` the CU triggers `MUX_STORE_SELCT`, which bypasses RY to RB so that the value meant for RY in STORE instruction can be passed to RB, and subsequently into the memory.

- If the instruction is `HLT`, it simply triggers `PC_STOP` so that the PC doesnt go for next addresses.

- If the instruction is `TYPE_3` (ADD,SUB,AND,OR,STORE) RB is used to store, either the second operand, or the value to store, as in case of `STORE` instruction. Hence the CU, enables the register RB, by signalling `RB_ENABLE` and `RB_ENABLE_SELECT`, so that the value can be written to it.

- For any other instruction (including `TYPE_3` and `TYPE_2` and `MOV`) it also activates `RA_ENABLE` and `RA_ENABLE_SELECT` enabling RA for use.

## STAGE 3

![S3](/docs/images/control-unit/cu-stage-3.png)

- In stage 3, it will enable RZ, MUXB and ALU for every instruction except `HLT`, signified by `TYPE_1`

- for `STORE` or any other `TYPE_2` instruction, it takes in input from the immediate into ALU, hence, `MUXB_SELECT` is set to high.

- for `STORE` specficially, the `RM` register is enabled to recieve the value from `RB`.

## STAGE 4

![S4](/docs/images/control-unit/cu-stage-4.png)

- for every `TYPE_1` instruction enable `RY` and `MUXY`

- For `STORE` and `LOAD`, `MUXMEM_SELECT` is set to high so that the `MEMORY` address is being fed from `RZ`.

- For `LOAD` `MUXY_SELECT` and `MEM_READ` is set to high so that RY gets data from the memory.

- For `STORE` `MEM_WRITE` is set to high so that data can be written to the memory.

## STAGE 5

![S5](/docs/images/control-unit/cu-stage-5.png)

- In stage 5, for every `TYPE_1` instruction, `RY_ENABLE_SELECT` is set to high so that output register designated in the instruction can be written into.