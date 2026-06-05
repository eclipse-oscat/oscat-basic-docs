<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : BYTE

| | |
|:---|:---|
| **Input	I** | BYTE (Eingangs Wert) |
| **D** | BOOL (Wert der zu ladenden Bits) |
| **P** | INT (Position des zu ladenden Bits) |
| **N** | INT (Anzahl der Bits die ab Position P geladen werden) |
| **Output** | BYTE (Ausgang) |
| | BIT_LOAD_B2 kann mehrere Bits in einem Byte gleichzeitig setzen oder löschen. Die Position wird mit 0 für Bit0 und 7 für Bit7 angegeben. N gibt an wie viele Bits ab der angegebenen Position verändert werden. Wird N = 0 werden keine Bits verändert. Wird die P und N so spezifiziert das die zu schreibenden Bits über das höchste (Bit 7) hinausreicht so wird wieder bei Bit 0 begonnen. |
| | BIT_LOAD_B2(2#1111_0000, TRUE, 1, 2) = 2#1111_0110 |
| | BIT_LOAD_B2(2#1111_1111, FALSE, 7, 2) = 2#0111_1110 |

![bit_load_B2](bit_load_b2.gif)
