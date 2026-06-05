<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## _BUFFER_UPPERCASE

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	PT** | POINTER TO BYTE (address of the  Buffer  ) |
| **SIZE** | UINT (size of the buffer) |
| **Output** | BOOL (Returns TRUE) |
| **The function _BUFFER_UPPERCASE interprets each byte in the buffer as ASCII characters and converts it to uppercase  . When called, a pointer to the array and its size in bytes is passed to the function. Under CoDeSys the call reads** | _BUFFER_INIT(ADR(Array), SIZEOF(Array), INIT), where array is the name of the array to be manipulated. ADR is a standard function, which identifies the  Pointer   the array and SIZEOF is a standard function, which determines the size of the array. The function only returns TRUE. By the  Pointer  given array is manipulated directly in memory. |
| | This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. |

![_buffer_uppercase](_buffer_uppercase.gif)

**Example:**

```iecst
_BUFFER_UPPERCASE(ADR(bigarray), SIZEOF(bigarray))
```
