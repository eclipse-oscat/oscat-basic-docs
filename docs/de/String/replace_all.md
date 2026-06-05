<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## REPLACE_ALL

| | |
|:---|:---|
| **Type	Funktion** | STRING |
| **Input	STR** | STRING (Eingangs String) |
| **SRC** | STRING (Suchstring) |
| **REP** | STRING (Ersatzstring) |
| **Output** | STRING (Ausgangsstring) |
| | REPLACE_ALL ersetzt alle in der Zeichenkette STR vorkommenden Strings SRC mit REP. Eine leere Zeichenkette an SRC ergibt keine Suchergebnisse. |

![replace_all](replace_all.gif)

**Beispiel:**

```iecst
REPLACE_ALL('123BB456BB789BB','BB','/') = '123/456/789/' REPLACE_ALL('123BB456BB789BB','BB','') = '123456789'
```
