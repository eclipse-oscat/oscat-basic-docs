<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : DWORD

| | |
|:---|:---|
| **Input	IN** | DWORD (Eingangs Daten) |
| **POS** | INT (Position) |
| **Output** | DWORD (Ausgangsbyte) |
| | BIT_TOGGLE_DW invertiert ein mit POS spezifiziertes Bit von IN. |
| | BIT_TOGGLE_DW(2#0000_1111, 2) = 2#0000_1011 |
| | BIT_TOGGLE_DW(2#0000_1111, 7) = 2#1000_1111 |

![bit_toggle_dw](bit_toggle_dw.gif)
