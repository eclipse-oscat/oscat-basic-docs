<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function module

| | |
|:---|:---|
| **Input	IN** | BYTE (input byte) |
| **Output	B0 .. B7** | BOOL (output bits) |
| | BYTE_TO_BITS split a byte (IN) into its individual bits (B0 .. B7). The input IN is defined as a DWORD to handle either byte, word, or DWORD at the input. If a Word or DWORD used at the input, only the bits 0th .7 are processed. A DWORD can then, using the default command SHR  , be shifted by 8 bits to the right and then the next byte can be processed. |

![byte_to_bits](byte_to_bits.gif)
