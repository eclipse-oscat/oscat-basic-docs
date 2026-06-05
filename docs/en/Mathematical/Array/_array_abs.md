<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## _ARRAY_ABS

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	PT** | Pointer  (Pointer to the array) |
| **SIZE** | UINT (size of the array) |
| **Output** | BOOL (TRUE) |
| **The function _ARRAY_ABS calculates the elements of an arbitrary array  Of  REAL in an absolute value. When called, a pointer to the array and its size in bytes is transferred to the function. Under CoDeSys the call reads** | _ARRAY_ABS(ADR(Array), SIZEOF(array)), where array is the name of the array to be manipulated. ADR() is a standard function which identifies the pointer to the array and SIZEOF() is a standard function, which determines the size of the array. The function only returns TRUE. The array specified by the pointer is manipulated directly in memory. |
| | This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. |
| **Call** | _ARRAY_ABS(ADR(bigarray), SIZEOF(bigarray)) |

![_array_abs](_array_abs.gif)

**Beispiel:**

Example:	[0,-2,3,-1-5]	is converted to [0,2,3,1,5]
