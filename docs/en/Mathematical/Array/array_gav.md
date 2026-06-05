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
| **Input	PT** | Pointer (pointer to the array) |
| **SIZE** | UINT (size of the array) |
| **Output** | REAL (mean value of the array) |
| **[fuzzy] The function _ARRAY_GAV calculates the median value of an arbitrary array of REAL. When called, a pointer to the array and its size in bytes is passed to the function. Under CoDeSys the call reads** | ARRAY_GAV(ADR(Array), SIZEOF(Array)), where array is the name of the array to be manipulated. ADR() is a standard function which identifies the pointer to the array and SIZEOF() is a standard function, which determines the size of the array. In order to determine the maximum, the array referenced by the pointer is scanned directly in memory. The function ARRAY_GAV does not change the content of the array. |
| | This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. |

![array_gav](array_gav.gif)

**Example:**

```iecst
ARRAY_GAV(ADR(bigarray), SIZEOF(bigarray))
```
