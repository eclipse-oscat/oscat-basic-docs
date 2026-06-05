<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MONTH_OF_DATE

| | |
|:---|:---|
| **Type	Function** | INT |
| **Input	IDATE** | DATE (date) |
| **Output** | INT (month in the year of the input date) |
| | The MONTH function calculates the month of the year from the date of input date IDATE. |

![month_of_date](month_of_date.gif)

**Example:**

```iecst
MONTH_OF_DATE(D#2007-12-31) = 12 MONTH_OF_DATE(D#2006-1-1) = 1
```
