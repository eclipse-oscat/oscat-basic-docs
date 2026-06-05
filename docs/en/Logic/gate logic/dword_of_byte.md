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
| **Input	B3** | Byte (input byte 3) |
| **B2** | Byte (input byte 2) |
| **B1** | Byte (input byte 1) |
| **B0** | Byte (input byte 0) |
| **Output** | DWORD (DWORD result) |
| | BYTE_OF_BIT creates from 4 individual bits (B0 .. B3) a DWORD. |
| **A DWORD is composed as follows** | B3-B2-B1-B0. |

![dword_of_byte](dword_of_byte.gif)
