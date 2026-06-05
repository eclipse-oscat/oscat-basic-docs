<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## BYTE_TO_STRH

| | |
|:---|:---|
| **Type	Funktion** | STRING |
| **Input	IN** | BYTE (Eingangswert) |
| **Output** | STRING(2) (Ergebnis STRING) |
| | BYTE_TO_STRH konvertiert ein Byte in einen STRING fester Länge. Der Ausgangsstring ist exakt 2 Stellen lang und entspricht der Hexadezimalen Schreibweise des Wertes von IN. Der Ausgangsstring besteht aus den Zeichen '0' .. '9' und 'A' .. 'F'. Das  niederwertigste Zeichen steht rechts im STRING. |

![byte_to_strh](byte_to_strh.gif)

**Beispiel:**

```iecst
BYTE_TO_STRH(15) = '0F'
```
