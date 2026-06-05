<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## _RMP_NEXT

| | |
|:---|:---|
| **Type** | Function module |
| **Input	E** | BOOL (  Enable Input) |
| **IN** | BOOL (input) |
| **TR** | TIME (rise time for ramp from 0..255) |
| **TF** | TIME (fall time for ramp 255..0) |
| **TL** | TIME (lock time between a change of direction) |
| **I / O** | I/O |
| **OUTPUT	DIR** | BOOL (direction of change in IN) |
| **UP** | BOOL (signals a rising ramp) |
| **DN** | BOOL (signals a falling ramp) |
| | RMP_NEXT follows at the output OUT to the input signal IN with the in TR and TF defined rising or falling flanks. Unlike RMP_SOFT the flank of RMP_NEXT runs until it underrun or overrun the endpoint and is therefore suitable for control tasks. Changing the value of IN so a rising ramp with TR or a falling flank with TF starts at the output OUT until the value of OUT has overrun or underrun the IN. The output then remains at this value. The outputs of UP and DN shows just whether a rising or a falling edge are created. The output DIR indicates the direction of change at IN, if IN is not changed, the output remains at the last state. The lock time TL determines the delay time between the direction reversal. |
| **The following graph shows the waveform at OUT when changing the input signal at IN** |  |

![_rmp_next](_rmp_next.gif)

![_rmp_next_sample](_rmp_next_sample.gif)
