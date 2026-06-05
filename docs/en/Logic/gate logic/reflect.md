<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## REFLECT

| | |
|:---|:---|
| **Type	Function** | DWORD |
| **Input	D** | DWORD (input) |
| **L** | INT (number of bits to be rotated) |
| **Output** | DWORD (output value) |
| | REFLECT reverses the order specified by the number of L BitsBits in a DWORD. The most significant bits than specified by the length L remain unchanged. |

![reflect](reflect.gif)

**Example:**

```iecst
REVERSE(10101010 00000000 11111111 10011110, 8)
```
results 10101010 00000000 11111111 01111001 Example:	REVERSE(10101010 00000000 11111111 10011110, 32)
results 01111001 11111111 00000000 01010101 the following example in ST would reverse all the bytes in a DWORD X, but the byte order remains: FOR i := 0 TO 3 DO REVERSE(X, 8); ROR(X,8); END_FOR
