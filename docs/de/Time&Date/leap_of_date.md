<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LEAP_OF_DATE

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	IDATE** | DATE (Eingangsdatum) |
| **Output** | BOOL (TRUE, wenn IDATE in einem Schaltjahr liegt) |
| | Die Funktion LEAP_OF_DATE testet, ob das Eingangsdatum in einem Schaltjahr liegt. Die Funktion berechnet, ob ein Datum innerhalb eines Schaltjahres liegt und gibt gegebenenfalls TRUE aus. Der Test hat Gültigkeit für den Zeitrum 1970 - 2099. im Jahr 2100 wird ein Schaltjahr angezeigt obwohl dies keines ist. Da aber der Wertebereich des Datums nach IEC61131-3 nur bis zum Jahr 2106 reicht wird auf diese Korrektur verzichtet. |

![leap_of_date](leap_of_date.gif)

**Beispiel:**

```iecst
LEAP_OF_YEAR(D#2004-01-12) = TRUE
```
