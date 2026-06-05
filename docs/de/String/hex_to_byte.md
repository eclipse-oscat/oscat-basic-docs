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
| **Input	HEX** | STRING(5) (Hexadezimale Zeichenkette) |
| **Output** | BYTE (Ausgangswert) |
| | Die Funktion HEX_TO_BYTE konvertiert eine hexadezimale Zeichenkette in einen BYTE Wert. Es werden dabei nur die hexadizimalen Zeichen sind '0'..'9', 'a..f' und 'A' .. 'F' interpretiert, alle anderen in HEX vorkommenden Zeichen werden ignoriert. |

![hex_to_byte](hex_to_byte.gif)

**Beispiel:**

```iecst
HEX_TO_BYTE('FF') ergibt 255.
```
