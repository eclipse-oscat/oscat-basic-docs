<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## FRMP_B

| | |
|:---|:---|
| **Type	Function** | BYTE |
| **Input	START** | BYTE (start value) |
| **DIR** | BOOL (direction of the ramp) |
| **TD** | TIME (Elapsed time) |
| **TR** | TIME (rise time for ramp from 0..255) |
| **Output** | BYTE (output) |
| | FRMP_B calculates the value of a ramp at a given time TD. The module ensures that no buffer overrun or underrun can take place at the output. The output value is limited in all cases to 0 .. 255. TR sets the time for a full ramp 0 .. 255 and TD is the elapsed time. If DIR = TRUE, a rising ramp is calculated and if DIR = FALSE a falling edge. With the start value an edge can be calculated from any starting point. |

![frmp_b](frmp_b.gif)
