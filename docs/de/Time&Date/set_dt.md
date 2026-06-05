<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : DATE_TIME

| | |
|:---|:---|
| **Input	YEAR** | INT (Jahreszahl) |
| **MONTH** | INT (Monat) |
| **DAY** | INT (Tag) |
| **HOUR** | INT (Stunde) |
| **MINUTE** | INT (Minute) |
| **SECOND** | INT (Sekunden) |
| **Output** | DATE_TIME (Zusammengesetztes Zeitdatum) |
| | Die Funktion SET_DT berechnet einen Zeit-Datumswert (DATE_TIME) aus den Eingangswerten Tag, Monat, Jahr, Stunde, Minute und Sekunden. |

![set_dt](set_dt.gif)

**Beispiel:**

```iecst
Set_DT(2007, 1, 22, 13, 10, 22) = DT#2007-1-22-13:10:22
```
