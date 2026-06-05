<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DEC_TO_DWORD

| | |
|:---|:---|
| **Type	Funktion** | DWORD |
| **Input	DEC** | STRING(20) (dezimale kodierte Zeichenkette) |
| **Output** | DWORD (Ausgangswert) |
| | Die Funktion DEC_TO_DWORD konvertiert eine dezimal kodierte Zeichenkette in einen BYTE Wert. Es werden dabei nur die dezimalen Zeichen sind '0'..'9' interpretiert, alle anderen in DEC vorkommenden Zeichen werden ignoriert. |

![dec_to_dword](dec_to_dword.gif)

**Beispiel:**

```iecst
DEC_TO_DWORD('34') ergibt 34.
```
