<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: BOOL

| | |
|:---|:---|
| **Input	IN** | DWORD (input) |
| **N** | INT (number of bits 0..31) |
| **Output** | BOOL (output bit) |
| | BIT_OF_DWORD extracts a bit of the DWORD at the input IN. |
| | Bit0 für N=0, Bit1 für N=1 and so on. |

![bit_of_dword](bit_of_dword.gif)
