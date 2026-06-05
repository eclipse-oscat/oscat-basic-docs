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
| **Input	DEC** | STRING(10) (dezimale kodierte Zeichenkette) |
| **Output** | BYTE (Ausgangswert) |
| | Die Funktion DEC_TO_BYTE konvertiert eine dezimal kodierte Zeichenkette in einen BYTE Wert. Es werden dabei nur die dezimalen Zeichen sind '0'..'9' interpretiert, alle anderen in DEC vorkommenden Zeichen werden ignoriert. |

![dec_to_byte](dec_to_byte.gif)

**Beispiel:**

```iecst
DEC_TO_BYTE('34') ergibt 34.
```
