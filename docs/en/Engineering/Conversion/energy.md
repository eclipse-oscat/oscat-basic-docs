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
| **Input	J** | REAL (Joule) |
| **C** | REAL (calorie) |
| **WH** | REAL (Watt hours) |
| **Output	YJ** | REAL (Joule) |
| **YC** | REAL (calorie) |
| **YWH** | REAL (Watt hours) |
| | The module converts ENERGY in different, in practice common units of energy. Normally, only the input to be converted is occupied and the remaining inputs remain free. However, if several inputs loaded with values, the values of all inputs are converted accordingly and then summed. |
| | 1 J = 1 Ws (Watt * Seconds) = 1 Nm (Newton * meters) |
| | 1 C = 4,1868 J = 1,163 * 10  -3  Wh (watt * hours) |
| | 1 Wh = 3,6 * 103 J = 860 C |

![energy](energy.gif)
