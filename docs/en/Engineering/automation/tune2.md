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
| **SU, SD** | BOOL (inputs for up and down in small increments) |
| **FU, FD** | BOOL (inputs for up and down in large increments) |
| **RST** | BOOL (asynchronous reset input) |
| **Output	Y** | REAL (output signal) |
| | TUNE2 sets  an output signal Y using up and down buttons. By corresponding setup variables, the step size for small and large steps are programmed individually. An upper and lower limit for the output Y can be specified  by LIMIT_L and LIMIT_H . with the SU and SD keys small steps can be generated up or down. The buttons FU and FD respectively produce large steps at the output Y. If a key is held down longer than TR, then the output Y continuously adjusted up or down. The speed which with the output here is adjusted, is for the two pairs of keys   S1 and S2 set individually. S1 and S2 indicate the units per second. S1 is the speed of the button SU and SD, and S2 according to FU and FD. With the inputs of the RST and SET  the Output can be set at any time, on a value predetermined by RST_VAL SET_VAL. |
| **Setup	SS** | REAL (step size for small steps) |
| **FS** | REAL (step size for big steps) |
| **SS** | REAL (step size for small step) |
| **Limit_H** | REAL (upper limit) |
| **RST_VAL** | REAL (initial value after reset) |
| **RST_VAL** | REAL (initial value after reset) |
| **TR** | TIME (time in which the ramp starts) |
| **S1** | REAL (speed for small ramp) |
| **S2** | REAL (speed for large ramp) |

![tune2](tune2.gif)
