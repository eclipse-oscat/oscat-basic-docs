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
| **Input	DIR** | BOOL (  Direction,  TRUE means Up  ) |
| **E** | BOOL (  Enable Input) |
| **TR** | TIME (time to run a full ramp) |
| **I / O	RMP** | WORD (output signal) |
| | _RMP_B Is an 16-bit ramp generator. The ramp is generated in an externally declared variable. The ramp is rising when DIR = TRUE and falling if DIR = FALSE. Reaching a final value of the ramp, the generator remains at this value. With the input E the ramp can be stopped at any time, when E = TRUE the ramp runs. The input TR shows the time which is needed to cycle through 0-65535 or the other way around. |

![_rmp_w](_rmp_w.gif)
