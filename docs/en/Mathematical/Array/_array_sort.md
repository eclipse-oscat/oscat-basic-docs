<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: BOOL

| | |
|:---|:---|
| **Input	PT** | Pointer (pointer to the array) |
| **SIZE** | UINT (size of the array) |
| **Output** | BOOL (TRUE) |
| **The function _array_SORT sorts an arbitrary array of REAL in ascending order. When called, a pointer to the array and its size in bytes is transferred to the function. Under CoDeSys the call is** | _ARRAY_SORT(ADR(Array), SIZEOF(Array)), where array is the name of the array to be manipulated. ADR() is a standard function which identifies the pointer to the array and SIZEOF() is a standard function, which determines the size of the array. |
| | The function only returns TRUE. The array specified by the pointer is manipulated directly in memory. |
| | This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. |

![_array_sort](_array_sort.gif)

**Example:**

```iecst
_ARRAY_SHUFFLE (ADRs(bigarray), SIZEOF(bigarray))
```
