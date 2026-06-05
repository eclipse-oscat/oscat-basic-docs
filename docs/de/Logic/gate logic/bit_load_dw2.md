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
| **Input	I** | DWORD (Eingangs Wert) |
| **D** | BOOL (Wert der zu ladenden Bits) |
| **P** | INT (Position des zu ladenden Bits) |
| **N** | INT (Anzahl der Bits die ab Position P geladen werden) |
| **Output** | DWORD (Ausgang) |
| | BIT_LOAD_DW2 kann mehrere Bits in einem DWORD gleichzeitig setzen oder löschen. Die Position wird mit 0 für Bit 0 und 31 für Bit 31 angegeben. N gibt an wie viele Bits ab der angegebenen Position verändert werden. Wird N = 0 werden keine Bits verändert. Wird P und N so spezifiziert, dass die zu schreibenden Bits über das höchste (Bit 31) hinausreicht so wird wieder bei Bit 0 begonnen. |

![bit_load_dw2](bit_load_dw2.gif)

**Beispiel:**

Beispiele siehe unter BIT_LOAD_B2
