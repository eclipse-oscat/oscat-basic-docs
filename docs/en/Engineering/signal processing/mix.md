<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: REAL

| | |
|:---|:---|
| **Input	A** | REAL (input value of 1) |
| **B** | REAL (input value 2) |
| **M** | REAL (ratio) |
| **Output** | REAL (value from the mixing ratio M between A and B) |
| | MIX provides at the output a mixed ratio M value, mixed from values A and B. The input M passes the proportion of B in the range 0..1. |
| | MIX = (M-1)*A + M*B |

![mix](mix.gif)
