<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	 Function  : STRING

| | |
|:---|:---|
| **Input	IN** | DWORD (input value) |
| **Output** | STRING(8) (result  string  ) |
| | DWORD_TO_STRH converts a DWORD, Word or byte in a STRING of fixed length. The output string is exactly 8 characters long and is the hexadecimal notation of the value of IN. The output string consists of the characters '0 '.. '1' and 'A '.. 'F'. The least significant hexadecimal character is right in the string. DWORD_TO_STRH can process input as byte, word and DWORD types. The output is independent of the input type is always a STRING of 32 characters. If a shorter string is needed, it can be cut with the standard function RIGHT() accordingly. The call RIGHT(DWORD_TO_STRH(X),4) results to a string of 4 characters to the contents of the lower 2 bytes of X. |

![dword_to_strh](dword_to_strh.gif)

**Example:**

```iecst
DWORD_TO_STRH(127) = '0000007F'
```
