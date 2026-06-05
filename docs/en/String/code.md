<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	 Function  : BYTE

| | |
|:---|:---|
| **Input	STR** | STRING (string) |
| **INT** | POS (position at which the character is read) |
| **Output** | BYTE (code of the character at position POS) |
| | CODE determines the numerical code for a character at the position POS in STR. Is CODE called with a position with less than 1 or greater than the length of STR, 0 is returned. |

![code](code.gif)

**Beispiel:**

Example: CODE('ABC 123',4) = 32 (The character '' is encoded with the value of 32).
