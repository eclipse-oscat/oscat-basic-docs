<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SCALE

| | |
|:---|:---|
| **Type	Function** | REAL |
| **Input	X** | Byte (input) |
| **K** | Byte (multiplier) |
| **O** | REAL (offset) |
| **MX** | REAL (maximum output value) |
| **MN** | REAL (minimum output value) |
| **Output** | REAL (output value) |
| | SCALE multiplies the input X with K, and adds the offset O. The calculated   value will be limited to the values of MN and MX and the result is passed to output. |
| | SCALE = LIMIT(MN, X * K + O, MX) |

![scale](scale.gif)
