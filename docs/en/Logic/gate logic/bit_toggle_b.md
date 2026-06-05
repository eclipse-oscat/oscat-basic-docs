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
| **Input	IN** | BYTE (input data) |
| **POS** | INT (Position) |
| **Output** | BYTE (output byte) |
| | BIT_TOGGLE_B inverts a specified bit at IN. |
| | BIT_TOGGLE_W(2#0000_1111, 2) = 2#0000_1011 |
| | BIT_TOGGLE_W(2#0000_1111, 7) = 2#1000_1111 |

![bit_toggle_b](bit_toggle_b.gif)
