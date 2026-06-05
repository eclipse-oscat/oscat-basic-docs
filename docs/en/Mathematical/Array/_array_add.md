<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## _ARRAY_ADD

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	PT** | Pointer  (Pointer to the array) |
| **SIZE** | UINT (size of the array) |
| **X** | REAL (added value) |
| **Output** | BOOL (TRUE) |
| **The function _ARRAXY_ADD adds to each element of an arbitrary array  of  REAL value X. When called a Pointer  to  the array and its size in bytes is passed to the function. Under CoDeSys the call reads** | _ARRAY_ADD(ADR(Array), SIZEOF(Array), X), where array is the name of the array to be manipulated. ADR() is a standard function which identifies the pointer to the array and SIZEOF() is a standard function, which determines the size of the array. The function only returns TRUE. The array specified by the pointer is manipulated directly in memory. |
| | This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. |
| **Call** | _ARRAY_ADD(ADR(bigarray), SIZEOF(bigarray), X) |

![_array_add](_array_add.gif)

**Beispiel:**

Example:	[0,-2,3,-1-5]	[0,-2,3,-1-5], X = 3 is converted into [3,1,6,2,-2]
