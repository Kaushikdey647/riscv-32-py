# Circuit and Function Description

![Main Circuit Image](/docs/images/main.png)


In this document, we shall have an in depth look into the circuit of the processor and its components. Furthermore, we shall have a look 

## Components

The **key** components of this processor are

- The **ALU**
- The **CU**
- The **Memory Interface**
- The **Datapath**
- The **MInstruction Address Generator**
- The **Instruction Decoder**

### Arithmetic and Logic Unit (ALU)

![ALU](/docs/images/alu.png)

The ALU, for now, has no flags, and supports only four operations:

- ADD
- SUB
- AND
- OR

It takes in two inputs `INPUT_A` and `INPUT_B`