# THE Five Stage Architecture

![DATAPATH](/docs/images/datapath/datapath.png)

- The datapath is THE most significant and active component of the processor. All the other components are built around it and according to its convenience.

- The datapath of our 32-bit RISC processor is a 5 stage pipeline, each stage executing a specific part in completing the instruction. More about that below.

- Below given 

<br>

## STAGE 1

![NA](/docs/images/datapath/datapath-stage1.png)

- In stage 1, the PC is being fed into the memory interface and the data is being relayed to the IR.
- The instruction from IR is being decoded and put into the respective channels of OPCODE and register addresses by the end of stage 1.
- Notable signals here are `RA_ENABLE_SELECT` and `RB_ENABLE_SELECT` which enables data read from the register addresses.`MEM_READ` in memory interface and `IR_ENABLE` in decoder that enables reading of the instruction 

## STAGE 2

![NA](/docs/images/datapath/datapath-stage2.png)

- In stage 2, the data from the respective registers are being put into the RA and RB registers, the immediate value is also channeled at this point.
- Notable signals here are `RA_ENABLE` and `RB_ENABLE` in the datapath.
## STAGE 3

![NA](/docs/images/datapath/datapath-stage3.png)

- Here the data relays on to the ALU for respective operation, and the result is ready for RZ to take in. Also the data that needs to be stored, if in RB, is being taken in by RM.

- Notable signals here are `MUXB_ENABLE`, `RM_ENABLE` and `ALU_ENABLE` that facilitates necessary channeling

## STAGE 4 and 5

![NA](/docs/images/datapath/datapath-stage4.png)

- In stage 4 the data is being taken into RZ and according to appropriate signals, the data is relayed into RY, or `MEM_ADDR`. The signals at play here are primarily `RZ_ENABLE` and `MUMXMEM_SELECT` which selects between the `PC_OUTPUT` and `RZ` to feed into the `MEM_ADDR`.

- In stage 5 the data from `RZ` (or the memory value) is being fed into `RY`. The signals used for the same is `RY_ENABLE`, `MUXY_ENABLE`. In case of `LOAD` the `MUXY_SELECT` is also set high.