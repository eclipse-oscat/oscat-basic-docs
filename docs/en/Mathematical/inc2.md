<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: INT

| | |
|:---|:---|
| **Input	X** | INT (input) |
| **D** | INT (value to be added to the input value) |
| **L** | INT (lower limit) |
| **U** | INT (upper limit) |
| **Output** | INT (output value) |
| | INC2 addes valued D to the input X and ensures that the output INC does not exceed the value U (upper limit) or under-run the value L (low limit). If the result from the addition of X and D  is larger than U so it begins again with L. It is ensured that at negative D when reaching L counted again at U on. The feature is especially useful when addressing arrays and buffers. Even the positioning of absolute encoders it can be used. INC2 can be used to decrementieren with a negative D, while INC2 will ensure that the result is not below zero. |
| **INC2** | = X + D, where L <= INC2 <= U. |

![inc2](inc2.gif)

**Beispiel:**

Example:	INC2(2, 2, -1, 3) result -1 INC2(2, -2, -1, 3) result 0 INC2(2, 1, -1, 3) result 3 INC2(0, -2, -1, 3) result 3
