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
| **Input	IN** | BOOL (switch input) |
| **RST** | BOOL (asynchronous reset input) |
| **Output	Q0 .. Q3** | BOOL (outputs) |
| | DRIVER_4C is a driver circuit whose output states are switched with a rising edge of IN. The output states are predefined in the Setup array SX and may be changed at any time by the user. The array SX [1..6] defines the output states for each switching state SN individually bitwise. Bit 0 of an element switch Q0, Bit1 turns Q1, Bit2 Q2 and Bit3 Q3, the upper 4 bits are respectively ignored. The array is initialized with Bit0 = TRUE for SN = 1, bit 1 for SN = 2. Bit2 for SN = 3 and Bit3 for SN = 4. Thus, the output go through the sequence (0000,0001,0010,0100,1000,0000) for (Q3, Q2, Q1, Q0) . If the element SX[SN] is of array 0 so the SN will automatically jump back to 0, so that an empty element terminates the sequence. At the end of the  timeout  the module automatically jumps back into the condition SN = 0. The  timeout  is only active if the variable TIMEOUT > t#0s is. |
| **Setup	TIMEOUT** | TIME (Maximum  Switch  of the module) |
| **SX** | ARRAY [1..7] OF BYTE:= 1,2,4,8,0,0,0; |
| | (Default setting of the switching sequence) |

![driver_4c](driver_4c.gif)

**Example:**

```iecst
SX = 1,3,7,15,7,3,1 generates the following sequence: Q3,Q2,Q1,Q0 = 0000,0001,0011,0111,1111,0111,0011,0001,0000,......
```
