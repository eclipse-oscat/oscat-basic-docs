<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function

| | |
|:---|:---|
| **Input	IDATE** | DATE (date) |
| **D** | INT (days to be added) |
| **W** | INT (weeks to be added) |
| **M** | INT (months to be added) |
| **Y** | INT (years to be added) |
| **Output** | DATE (result date) |
| | The function DATE_ADD add days, weeks, months, and add years to a date. First the module adds the specified days and weeks, then months and finally the years. |
| | The input values can be both positive as well be negative. So it can also be subtracted from a date. |
| | Note that especially for negative input values the sum of negative values, i.e. -3000 days does not run below 1.1.1970 because this would have an overflow of data type DATE and undefined values are obtained. |

![date_add](date_add.gif)

**Beispiel:**

Example:	DATE_ADD(1.1.2007,3,1,-1,-2) = 11/12/2005 adds additional 3 days and 1 week and then draws 1 month and	2 years from.
