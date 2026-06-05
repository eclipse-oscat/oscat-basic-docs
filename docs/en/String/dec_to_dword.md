<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DEC_TO_DWORD

| | |
|:---|:---|
| **Type	Function** | DWORD |
| **Input	DEC** | STRING(20) (decimal-encoded string) |
| **Output** | DWORD (output value) |
| | The function DEC_TO_DWORD converts a decimal encoded string into a byte value. Here only decimal characters '0 '.. '9' are interpreted, others in DEC occurring characters are ignored . |

![dec_to_dword](dec_to_dword.gif)

**Beispiel:**

Example:	DEC_TO_DWORD('34 ') is 34.
