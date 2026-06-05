<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function

| | |
|:---|:---|
| **Input	IN** | BYTE (input) |
| **LOW** | REAL (initial value at X = 0) |
| **HIGH** | REAL (initial value at X = 255) |
| **Output** | REAL (output value) |
| | BYTE_TO_RANGE convert a BYTE value to a REAL. An input value of 0 corresponds to the REAL value of LOW and an input value of 255 corresponds to the input value of HIGH. |
| **To convert a BYTE value of 0 .255 to a percent of 0 .100 the module is called, as follows** |  |
| | BYTE_TO_RANGE (X,0,100) |

![byte_to_range](byte_to_range.gif)
