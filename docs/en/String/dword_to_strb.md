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
| **Output** | STRING(32) (result STRING) |
| | DWORD_TO_STRB converts a DWORD, Word or byte in a STRING of fixed length. The output string is exactly 32 characters long and is the bitwise notation of the value of IN. The output string consists of the characters '0 'and '1'. The   least significant bit is left in the string. DWORD_TO_STRB can handle input formats, Byte, Word and DWORD types. The output is independent of the input type is always a STRING of 32 characters. If a shorter string is needed, it can be cut with the standard function RIGHT() accordingly. The call RIGHT(DWORD_TO_STRB(X),8) results to a string of 8 characters to the contents of the lower bytes of X. |

![dword_to_strb](dword_to_strb.gif)

**Beispiel:**

Example  : DWORD_TO_STRB(127) = '00000000000000000000000001111111'
