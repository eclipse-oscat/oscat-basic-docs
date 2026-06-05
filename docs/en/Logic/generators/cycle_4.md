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
| **Input	E** | BOOL (  Enable Input) |
| **T0 _ T3** | TIME (run time of each  States  ) |
| **S0** | BOOL (continuous cycle  Enable  ) |
| **SX** | INT (  State if SL = TRUE) |
| **SL** | BOOL (asynchronous  Load input) |
| **Output	STATE** | INT (status output) |
| | CYCLE_4 generates theStates  0..3 if E = TRUE . The duration of each  State  can be determined by the time constraints T0..T3. The input SL starts when TRUE from a predetermined  STATE SX. The input E has the internal  Default  = TRUE, so that it can also be left open. After a rising edge on E the module always starts with STATE = 0, and if E = FALSE, the output STATE remains at 0. With the input of S0 the cyclic mode is turned on, if S0 = FALSE the module stops at  State  = 3, if S0 = TRUE, the device begins to  State  3 again with  State  0. |

![cycle_4](cycle_4.gif)
