<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LEAP_DAY

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	IDATE** | DATE (date) |
| **Output** | BOOL (TRUE if the current day is 29 February) |
| | The LEAP_DAY function checks if the input date is a leap or a 29th February. The test is valid for the time window from 1970 to 2099. In the year 2100 a leap year indicated although this is not one. However, since the range of dates according to IEC61131-3 extends only to the year 2106 this correction will be omitted. |

![leap_day](leap_day.gif)

**Example:**

```iecst
LEAP_DAY(D#2004-02-29) = TRUE
```
