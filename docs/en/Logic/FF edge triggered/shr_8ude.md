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
| **Input	SET** | BOOL (Asynchronous Set) |
| **D0** | BOOL (Data  Input  Bit 0) |
| **D3** | BOOL (Data  Input  Bit 3) |
| **CLK** | BOOL (clock input) |
| **DN** | BOOL (control input  Up  /  Down,  TRUE =  Down  ) |
| **RST** | BOOL (asynchronous reset) |
| **Output	Q0 .. Q7** | BOOL (Data  Out  ) |
| | SHR_8UDE is an 8 bit shift register with Up /Down  sliding direction. A rising edge at CLK, the data Q0 are be pushed to Q7 one step. Q0 is then loaded with D0. The shift direction can be reversed with a TRUE at the input DN. Then D7 is pushed to Q6, Q5, Q4, Q3, Q2, Q1, Q0 and Q7 is loaded with D7. With a TRUE on the Set input, all outputs (Q0.. Q3) set to TRUE and RST all outputs are set to FALSE. Further explanation of shift registers, see SHR_4E and especially at the module SHR_4UDE, which has the same function for 4 bits   as SHR_8UDE for 8 bits. |

![shr_8ude](shr_8ude.gif)
