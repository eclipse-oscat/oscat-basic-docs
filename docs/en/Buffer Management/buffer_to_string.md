<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## BUFFER_TO_STRING

| | |
|:---|:---|
| **Type	 Function** | STRING |
| **Input	PT** | POINTER TO BYTE (address of the Buffer ) |
| **SIZE** | UINT (size of the buffer) |
| **START** | UINT (position from which the String will be from the buffer |
| | copied) |
| **STOP** | UINT (end of Strings in the buffer) |
| **Output** | STRING (a string that was copied from the buffer) |
| **The function BUFFER_To_STRING extracts a String from any array of Byte. The String is copied from any position START from the buffer and ends at the STOP position. The first element in the array is at position number 0. When called aPointer to the array and its size in bytes is passed to the function. Under CoDeSys the call reads** | BUFFER_TO_STRING (ADR (Array), SIZEOF (ARRAY), START, STOP), ARRAY is the name of the array. ADR() is a standard function which identifies the pointer to the array and SIZEOF() is a standard function, which determines the size of the array. The function returns the string copied from the buffer as STRING. This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. Example:	BUFFER_TO_STRING(ADR(Array), SIZEOF(ARRAY), START, STOP) |

![buffer_to_string](buffer_to_string.gif)
