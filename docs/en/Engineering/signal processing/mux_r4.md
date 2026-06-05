<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MUX_R4

| | |
|:---|:---|
| **Type** | Function |
| **Input	IN0** | REAL (input 0) |
| **IN1** | REAL (input value of 1) |
| **IN2** | REAL (input 0) |
| **IN3** | REAL (input value of 1) |
| **A0** | BOOL (address input bit 0) |
| **A0** | BOOL (address input bit 0) |
| **Output** | REAL (IN0 if A0 = 0 and A1 = 0, IN3 if A0 = 1 and A3 = 1) |
| | MUX_R4 selects one of 4 input values. |
| **Logical connection** | IN0 if A0 = 0 & A1 = 0, |
| | IN1 if A0 = 1 & A1 = 0; |
| | IN2 if A0 = 0 & A1 = 1; |
| | IN3 if A0 = 1 & A1 = 1; |

![mux_r4](mux_r4.gif)
