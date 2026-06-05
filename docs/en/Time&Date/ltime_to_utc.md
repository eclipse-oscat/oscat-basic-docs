<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LTIME_TO_UTC

| | |
|:---|:---|
| **Type	Function** | DATE_TIME |
| **Input	LTIME** | DATE_TIME (local time) |
| **DST** | BOOL (TRUE if daylight saving time is true) |
| **TIME_ZONE_OFFSET** | INT (time difference to UTC in minutes) |
| **Output** | DATE_TIME (UTC, Universal Time) |
| | LTIME_TO_UTC calculates UTC (Universal Time) from a given local time. 
The world time is calculated by subtracting from the TIME_ZONE_OFFSET LTIME local time. If the DST is active (DST = TRUE), an additional hour of LTIME is deducted. |

| **Note** | The summer time is not regulated the same in all countries. The function assumes that in addition to summer time a further hour is added to offset. |

![ltime_to_utc](ltime_to_utc.gif)
