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
| **Input	CI** | REAL (input from controller) |
| **OFFSET** | REAL (output offset) |
| **MAN_IN** | REAL (Manual input) |
| **LIM_L** | REAL (lower output limit) |
| **LIM_H** | REAL (upper output limit) |
| **MANUAL** | BOOL (switch for manual operation) |
| **Output	Y** | REAL  (Control signal) |
| **LIM** | BOOL (TRUE if control signal reaches a limit) |
| | CTRL_OUT adds to the CI input the value of OFFSET and returns the result to Y if MANUAL = FALSE. If MANUAL is TRUE at output Y the input value of MAN_IN + OFFSET is issued. Y is always limited to the boundaries defined by LIM_L and LIM_H. If Y reaches one of the limits, then the output LIM is TRUE. CTRL_OUT can be used to build own rule modules. |
| **Block diagram of CTRL_OUT** |  |

![ctrl_out](ctrl_out.gif)

![ctrl_out_sch](ctrl_out_sch.gif)
