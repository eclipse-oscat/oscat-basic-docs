<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: BYTE

| | |
|:---|:---|
| **Input	BIN** | STRING (12) (Octal string) |
| **Output** | BYTE (output value) |
| | The function BIN_TO_BYTE converts a binary encoded string in a BYTE value. There, this method only binary characters are '0 'and '1' is interpreted, others in BIN occurring characters are ignored. |

![bin_to_byte](bin_to_byte.gif)

**Beispiel:**

Example:	BIN_TO_BYTE ('11 ') result 3.
