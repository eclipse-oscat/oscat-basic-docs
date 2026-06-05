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
| **Input	SET** | BOOL (Asynchronous set input) |
| **SU, SD** | BOOL (inputs for up and down) |
| **RST** | BOOL (asynchronous reset input) |
| **Output	Y** | REAL (output signal) |
| | TUNE sets, using up and down buttons, an output signal Y. By corresponding setup variables, the increment will be programmed individually. An upper and lower limit for the output Y can be specified  by LIMIT_L and LIMIT_H . with the buttons SU and SD up or down steps are generated. If a key is held down longer than the time T1, then the output Y is continuously adjusted up or down. The speed, which with the output is adjusted here, is given by S1. S1 and S2 indicate the units per second. Is   a button held down longer than the time T2, the device automatically switches to a second speed S2. With the inputs RST and SET the output can at any time be adjusted by RST_VAL resp. SET_VAL to a predetermined value. |
| **Setup	SS** | REAL (step size for small step) |
| **SS** | REAL (step size for small step) |
| **Limit_H** | REAL (upper limit) |
| **RST_VAL** | REAL (initial value after reset) |
| **RST_VAL** | REAL (initial value after reset) |
| **T1** | TIME (time after the first ramp starts) |
| **T1** | TIME (time in which the second ramp starts) |
| **S1** | REAL (speed for first ramp) |
| **S2** | REAL (speed for second ramp) |

![tune](tune.gif)
