<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: DINT

| | |
|:---|:---|
| **Input	DATE_1** | DATE (Date1) |
| **DATE_2** | DATE (date2) |
| **Output** | DINT (difference of the two input dates in days) |
| | The function DAYS_DELTA  calculates the difference between two data in days. |

![days_delta](days_delta.gif)

**Example:**

```iecst
DAYS_DELTA(10.1.2007, 1.1.2007) = -9 DAYS_DELTA(1.1.2007, 10.1.2007) = 9
```

The result of the function is of type DINT because the entire DATE  Range  Includes 49,710 days.
