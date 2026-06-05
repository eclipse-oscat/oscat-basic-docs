<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: DWORD

| | |
|:---|:---|
| **Input	HEX** | STRING(20) (hex string) |
| **Output** | DWORD (output value) |
| | The function HEX_TO_DWORD converts a hexadecimal string in a DWORD value. Here only hexadecimal characters  '0'..'9', 'a..f' and 'A'.. 'F' are interpreted, others occurring in HEX characters are ignored. |

![hex_to_dword](hex_to_dword.gif)

**Example:**

```iecst
HEX_TO_DWORD('FF') is 255.
```
