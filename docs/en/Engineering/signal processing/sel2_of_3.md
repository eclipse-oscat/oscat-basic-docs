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
| **Input	IN1** | REAL (input value of 1) |
| **IN2** | REAL (input value 2) |
| **IN3** | REAL (input value 3) |
| **D** | REAL (tolerance) |
| **Output	Y** | REAL (baseline) |
| **W** | INT (warning) |
| **E** | BOOL (  Error  Output) |
| | SEL2_OF_3 evaluates 3 inputs (IN1 .. IN3) and checks whether the deviation of the input value is less than or equal to D. The average of the three inputs is output at output Y. The individual inputs are only considered if they are not further away from another input than D. If the mean value of only 2 inputs, the number of unrecognized input is passed at W. If W = 0, all 3 inputs are considered. If all 3 inputs vary more than D, the output is set to W = 4  and the output E = TRUE. The output Y is not changed in this case and remains at the last valid zero. " |
| | A typical application for the module is the acquisition of 3 sensors which measures the same process variable in order to reduce measurement error as measured by different measures or broken wire. |

![sel2_of_3](sel2_of_3.gif)
