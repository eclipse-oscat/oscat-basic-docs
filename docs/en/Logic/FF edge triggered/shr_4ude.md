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
| **DN** | BOOL (control input  Up / Down  TRUE = D  own  ) |
| **RST** | BOOL (asynchronous reset) |
| **Output	Q0** | BOOL (Data  Out  0) |
| **Q1** | BOOL (Data  Out  1) |
| **Q1** | BOOL (Data  Out  1) |
| **Q3** | BOOL (Data  Out  3) |
| | SHR_4UDE is a 4-bit shift register with Up  / Down  sliding directions. A rising edge at CLK, Q2 is moved to Q3, then moves the Q1 to Q2, Q0 to Q1 and D0 to Q0. The shift direction can be reversed with a TRUE at the input DN, then the D3 is pushed to Q3 - to Q2 - to Q1 - to Q0. With a TRUE on the Set input, all outputs (Q0.. Q3) are set to TRUE and with RST all the inputs are set to FALSE. |

![shr_4ude](shr_4ude.gif)

![shr_4ude_trace](shr_4ude_trace.gif)
