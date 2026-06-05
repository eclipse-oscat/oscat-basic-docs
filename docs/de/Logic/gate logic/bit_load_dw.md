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
| **Input	IN** | DWORD (Eingang) |
| **VAL** | BOOL (Wert des zu ladenden Bits) |
| **POS** | INT (Position des zu ladenden Bits) |
| **Output** | DWORD (Ausgang) |
| | BIT_LOAD_DW kopiert das am Eingang VAL anliegende Bit an die Position N im DWORD IN. Das niederwertigste Bit B0 wird mit der Position 0 bezeichnet. |

![bit_load_dw](bit_load_dw.gif)
