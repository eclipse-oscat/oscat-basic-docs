<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : TOD

| | |
|:---|:---|
| **Input	HOUR** | INT (Stunde) |
| **MINUTE** | INT (Minute) |
| **SECOND** | REAL (Sekunden und Millisekunden) |
| **Output** | TOD (Ausgangswert Tageszeit) |
| | Die Funktion SET_TOD berechnet eine Tageszeit (TOD) aus den Eingangswerten Stunde, Minute und Sekunden. |

![set_tod](set_tod.gif)

**Beispiel:**

```iecst
Set_TOD(13, 10, 22.33) = 13:10:22.330
```
