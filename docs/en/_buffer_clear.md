<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function : BOOL

| | |
|:---|:---|
| **Input	PT** | POINTER TO BYTE (address of the  Buffer  ) |
| **SIZE** | UINT (size of the buffer) |
| **Output** | BOOL (Returns TRUE) |
| **The function _BUFFER_CLEAR initialize any array of Byte with 0. When called, a pointer to the array and its size in bytes is passed to the function. Under CoDeSys is the call** | _BUFFER_CLEAR(ADR(Array), SIZEOF(Array)), where array is the name of the array to be manipulated. ADR() is a standard function which identifies the pointer to the array and SIZEOF() is a standard function, which determines the size of the array. The function only returns TRUE. The array specified by the pointer is manipulated directly in memory. |
| | This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. |

![_buffer_clear](_buffer_clear.gif)

**Beispiel:**

Example:	_ARRAY_CLEAR(ADRs(bigarray), SIZEOF(bigarray)) initialized bigarray with 0.
