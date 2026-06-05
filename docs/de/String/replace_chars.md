<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## REPLACE_CHARS

| | |
|:---|:---|
| **Type	Funktion** | STRING |
| **Input	STR** | STRING (Eingangsstring) |
| **SRC** | STRING (Suchzeichen) |
| **REP** | STRING (Ersatzzeichen) |
| **Output** | STRING (Ausgangsstring) |
| | REPLACE_CHARS ersetzt alle Zeichen  in SRC die in STR vorkommen mit den Zeichen an der gleichen Stelle in REP. |

![replace_chars](replace_chars.gif)

**Beispiel:**

```iecst
REPLACE_CHARS('abc123', '0123456789', ABCDEFGHIJ') = 'abcABC'
```
