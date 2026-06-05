<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SCALE_R

| | |
|:---|:---|
| **Type	Function** | REAL |
| **Input	X** | REAL (input) |
| **I_LO** | REAL (min input value) |
| **I_HI** | REAL (input value max) |
| **O_LO** | REAL (min output value) |
| **O_HI** | REAL (output value max) |
| **Output** | REAL (output value) |
| | SCALE_R scales an input value REAL and calculates an output value in REAL. The input value X is limited here to I_LO and I_HI. SCALE_D (IN,4,20,0,100) scales an input with 4 .. 20mA to the output 0..100. SCALE_R can also be negative output values and work with a negative slope, the values I_LO and I_HI but must always be specified that ILO < I_HI. |

![scale_r](scale_r.gif)
