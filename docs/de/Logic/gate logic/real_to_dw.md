<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## REAL_TO_DW

| | |
|:---|:---|
| **Type	Funktion** | DWORD |
| **Input	IN** | REAL (Eingang) |
| **Output** | DWORD (Ausgangswert) |
| | REAL_TO_DW kopiert das Bitmuster eines REAL (IN) in ein DWORD. Es werden dabei die einzelnen Bits kopiert ohne auf deren Bedeutung zu achten. Die Funktion DW_TO_REAL ist die Umkehrfunktion so das die Konvertierung von REAL_TO_DW und anschließend DW_TO_REAL wiederum den Ausgangswert ergibt. Die IEC Standardfunktion REAL_TO_DWORD wandelt den REAL Wert in einen Festzahlenwert und Rundet an der kleinsten Stelle des DWORD. |

![real_to_dw](real_to_dw.gif)
