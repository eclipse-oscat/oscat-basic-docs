<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : TIME

| | |
|:---|:---|
| **Input	IN** | REAL (Anzahl Stunden mit Nachkommastellen) |
| **Output** | TIME (Tageszeit) |
| | Die Funktion HOUR_TO_TOD berechnet eine Tageszeit (TIMEOFDAY) aus dem Eingangswert in Stunden als REAL. |

![hour_to_tod](hour_to_tod.gif)

**Beispiel:**

```iecst
HOUR_TO_TOD(12.1) = 12:06:00
```
