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
| **Output** | INT (Tag im Jahr des Eingangsdatums) |
| | Die Funktion DAY_OF_YEAR berechnet den Tag des Jahres aus dem Eingangsdatum IDATE. Schaltjahre werden entsprechend dem gregorianischen Kalender berücksichtigt. Die Funktion ist definiert für die Jahre 1970 – 2099. |

![day_of_year](day_of_year.gif)

**Beispiel:**

```iecst
DAY_OF_YEAR(31.12.2007) = 365 DAY_OF_YEAR(31.12.2008) = 366
```
