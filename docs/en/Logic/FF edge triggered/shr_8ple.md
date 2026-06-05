<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function module

| | |
|:---|:---|
| **Input	DIN** | BOOL (Shift Data  Input  ) |
| **Dload** | Byte (data word for parallel  Load  ) |
| **CLK** | BOOL (clock input) |
| **UP** | BOOL (control input  Up  /  Down,  TRUE =  Up  ) |
| **LOAD** | BOOL (control input for loading the register) |
| **RST** | BOOL (asynchronous reset) |
| **Output	DOUT** | BOOL (Data  Out  ) |
| | SHR_8PLE is an 8 bit shift register with parallel  Load  and asynchronous reset. The shift direction can be reversed with the input of UP. When UP = 1, bit 7 is first pushed on DOUT and when UP = 0, bit 0 is first pushed to DOUT. For Up -Shift Bit 0 is loaded with DIN and Down - Shift Bit 7 is loaded with DIN. At the input DLOAD one byte of data occures, which with parallel Load  (  LOAD  = 1 and rising edge on  CLK  ) Is loaded into internal registers. In the case of parallel  Load  is first a shift done and then loaded the register. An RST can always delete the register asynchronously. A detailed description of a shift register, see the module SHR_4E. |

![shr_8ple](shr_8ple.gif)
