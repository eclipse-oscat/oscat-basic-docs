<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: WORD

| | |
|:---|:---|
| **Input	I** | WORD (input value) |
| **D** | BOOL (value of bits to be loaded) |
| **P** | INT (position of the bits to be loaded) |
| **N** | INT (number of bits that are loaded from position P) |
| **Output** | WORD (output) |
| | BIT_LOAD_W2 can set or delete multiple bits in a WORD at the same time. The position is indicated with 0 for Bit 0 and 15 for Bit 15. N specifies how many bits from the specified location can be changed. If N = 0, no bits are changed. If P and N is specified that the bits to be written goes over the highest bit (bit 15), so it starts again at bit 0. |

![bit_load_w2](bit_load_w2.gif)

**Beispiel:**

Examples, see BIT_LOAD_B2
