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
| **Input	X** | REAL (input) |
| **C** | ARRAY[0..7]  of  REAL (polynomial coefficients) |
| **Output** | REAL (result of the polynomial equation) |
| | F_POLY calculates a polynomial of 7th degree. |
| | F_POLY = C[0] + C[1] * X^1 + C[2] * X^2 + ...C[7] * X^7 |

![f_poly](f_poly.gif)
