<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## BUFFER_SEARCH

| | |
|:---|:---|
| **Type	Function** | INT |
| **Input	PT** | POINTER (address of the Buffer) |
| **SIZE** | UINT (size of the buffer) |
| **STR** | STRING (search string) |
| **POS** | INT (from the position being sought) |
| **IGN** | BOOL (Search is case-sensitive) |
| **Output** | INT (position of the string was found) |
| **The function BUFFER _ SEARCH search any array of Bytes on the contents of a string and reports the position of the first character of the string in the array when a matching is found. The Buffer is searched from any position POS. The first element in the array is at position number 0. When called, a Pointer to the array and its size in bytes is passed to the function. Under CoDeSys the call reads** | BUFFER_SEARCH (ADR (Array), SIZEOF (ARRAY), STR, POS, IGN), where ARRAY is the name of the array. ADR() is a standard function which identifies the pointer to the array and SIZEOF() is a standard function, which determines the size of the array. The function returns the string copied from the buffer as STRING. This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. If IGN = TRUE both upper- and lowercase letters are found as a match, while STR must be present in uppercase letters. If IGN = FALSE case sensitive is searched. |

![buffer_search](buffer_search.gif)

**Example:**

```iecst
BUFFER_SEARCH(ADR(aArray), SIZEOF(Array), 'FIND', 0, TRUE) Locates 'FIND', 'Find', 'find' .... in the array. Example: BUFFER_SEARCH(ADR(Array), SIZEOF(ARRAY), 'FIND', 0, FALSE) Only finds 'FIND' in the array.
```
