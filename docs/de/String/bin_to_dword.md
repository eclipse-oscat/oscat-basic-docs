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
| **Input	BIN** | STRING(40) (Oktale Zeichenkette) |
| **Output** | DWORD (Ausgangswert) |
| | Die Funktion BIN_TO_DWORD konvertiert eine binär kodierte Zeichenkette in einen BYTE Wert. Es werden dabei nur die binären Zeichen sind '0' und '1' interpretiert, alle anderen in BIN vorkommenden Zeichen werden ignoriert. |

![bin_to_dword](bin_to_dword.gif)

**Beispiel:**

Beispiel:	BIN_TO_DWORD('11') ergibt 3.
