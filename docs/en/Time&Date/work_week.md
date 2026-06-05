<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: INT

| | |
|:---|:---|
| **Input	IDATE** | DATE (date) |
| **Output** | INT (working week of the input date) |
| | The function WORK_WEEK calculates the week from the date of input IDATE. The week starts with 1 for the first week of the year. The first Thursday of the year is always in the first week. If a year starts with a Thursday or end on a Thursday this year has 53 calendar weeks. If the first day of the year a Tuesday, Wednesday or Thursday so the week begins one early as December of last year. If the first day of the year is Friday, Saturday or Sunday, the last week of the year extends into January. The calculation is done in accordance with ISO8601. |
| | As the work week (Work Week ) International is not always used consistent, before the application of the function is to clarify, whether the work week according to ISO8601 is desired in the desired application function. |

![work_week](work_week.gif)
