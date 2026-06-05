<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: REAL

| | |
|:---|:---|
| **Input	PT** | Pointer (pointer to the array) |
| **SIZE** | UINT (size of the array) |
| **Output** | REAL (median of the array) |
| **The function _ARRAY_MEDIAN calculates the median value of an arbitrary array of REAL. When called a pointer  to the array and its size in bytes is passed to the function. Under CoDeSys the call reads** | _ARRAY_MEDIAN(ADR(Array), SIZEOF(Array)), where array is the name of the array to be manipulated. ADR() is a standard function, which identifies the pointer to the array and SIZEOF() is a standard function, which determines the size of the array. In order to determine the median value the array referenced by the pointer is sorted in the memory and remains after function end sorted. The function _ARRAY_MEDIAN thus changes the contents of the array. |
| | This type of processing arrays is very efficient because no additional memory is required and no surrender values must be copied. |
| | If an array is processed, which should not be changed, so it has to be copied to a temporary array before handing over the  Pointer  and calling the function. |

![_array_median](_array_median.gif)

**Example:**

```iecst
_ARRAY_MEDIAN(ADR(bigarray), SIZEOF(bigarray)) Median Value:
```
The median is the middle value to a sorted set of values. 
 Median  of (12, 0, 4, 7, 1) is 4 After running the function the array remains sorted in memory (0, 1, 4, 7, 12). If the array contains an even number of elements the median is the average of the two middle values of the array.
