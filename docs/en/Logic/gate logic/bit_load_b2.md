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
| **Input	I** | BYTE (input value) |
| **D** | BOOL (value of bits to be loaded) |
| **P** | INT (position of the bits to be loaded) |
| **N** | INT (number of bits that are loaded from position P) |
| **Output** | BYTE (output) |
| | BIT_LOAD_B2 can set or delete multiple bits in a byte at the same time. The position is indicated with 0 for Bit0 and 7 for Bit7. N specifies how many bits from the specified location can be changed. If N = 0, no bits are changed. If the P and N is specified that the bits to be written goes over the highest bit (bit 7), so it starts again at bit 0. |
| | BIT_LOAD_B2(2#1111_0000, TRUE, 1, 2) = 2#1111_0110 |
| | BIT_LOAD_B2(2#1111_1111, FALSE, 7, 2) = 2#0111_1110 |

![bit_load_B2](bit_load_b2.gif)
