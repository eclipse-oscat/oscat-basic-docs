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
| **Input	PT** | TIME (period time) |
| **AM** | REAL (signal amplitude) |
| **OS** | REAL (signal offset) |
| **DL** | REAL (signal delay 0..1 * PT ) |
| **Output	Q** | BOOL (binary output) |
| **OUT** | REAL (analog output) |
| | GEN_RMP is a  sawtooth generator.  It generates a ramp at the output OUT with the duration of PT and repeats this continuously. The output Q is for exactly one cycle TRUE when the ramp starts at the output OUT. The input AM and OS set the amplitude and the offset for the output OUT. If the inputs OS and AM are not connected the default values are 0 and 1. The output OUT then generates a sawtooth signal of 0 .. 1. The input DL can move the output up to a period (PT) and is used to produce multiple shifted signals to each other. A 0 at the input DL means no displacement. A value between 0 and 1 shifts the signal by up to a period. |
| | The following example shows a trace recording of the input values PT = 10s, AM = 1 and OS = 0 |

![gen_rmp](gen_rmp.gif)

![gen_rmp_trace](gen_rmp_trace.gif)
