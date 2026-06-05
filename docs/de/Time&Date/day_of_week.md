<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : INT

| | |
|:---|:---|
| **Input	IDATE** | DATE (Eingangsdatum) |
| **Output** | INT (Monat im Jahr des Eingangsdatums) |
| | Die Funktion DAY_OF_WEEK berechnet den Wochentag aus dem Eingangsdatum IDATE. |
| | Montag = 1... Sonntag = 7. Die Berechnung erfolgt gemäß ISO8601. |

![day_of_week](day_of_week.gif)

**Beispiel:**

```iecst
DAY_OF_WEEK(D#2007-1-8) = 1
```
