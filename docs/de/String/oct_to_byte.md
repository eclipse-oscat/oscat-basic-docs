<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## OCT_TO_BYTE

| | |
|:---|:---|
| **Type	Funktion** | BYTE |
| **Input	OCT** | STRING(10) (Oktale Zeichenkette) |
| **Output** | BYTE (Ausgangswert) |
| | Die Funktion OCT_TO_BYTE konvertiert eine oktal kodierte Zeichenkette in einen BYTE Wert. Es werden dabei nur die oktalen Zeichen sind '0'..'7' interpretiert, alle anderen in HEX vorkommenden Zeichen werden ignoriert. |

![oct_to_byte](oct_to_byte.gif)

**Beispiel:**

```iecst
OCT_TO_BYTE('11') ergibt 9.
```
