<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## BUFFER_COMP

| | |
|:---|:---|
| **Type	Function** | INT |
| **Input	PT1** | POINTER (address of the first Buffer ) |
| **Size1** | INT (size of the first buffer) |
| **PT2** | POINTER (address of the second Buffer ) |
| **SIZE2** | INT (size of the second buffer) |
| **START** | INT (search begin from start) |
| **Output** | INT (position found) |
| | The function BUFFER_COMP checks whether the content of the array PT2 occurs in the array PT1 from position START. If PT2 is found in PT1, so the function returns the position in PT1, starting from 0. If PT2 is not found in PT1, -1 is returned. BUFFER_COMP can also be used for comparison of two equally sized arrays. |
| **When called, a Pointer to the array and its size in bytes is passed to the function. In CoDeSys the call reads** | BUFFER_COMP(ADR(BUF1), SIZEOF(BUF1), ADR(BUF2), SIZEOF(BUF2)), where BUF1 and BUF2 are the names of the arrays to be manipulated. ADR() is a standard function which indentifies the Pointer to the array and SIZEOF() is a standard function, which determines the size of the array. The function only returns TRUE. The array specified by the Pointer is manipulated directly in memory. This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. |

![buffer_comp](buffer_comp.gif)

**Example:**

```iecst
BUFFER_COMP(ADR(BUF1), SIZEOF(BUF1), ADR(BUF2), SIZEOF(BUF2))
```
