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
| **Input	X** | INT (input) |
| **D** | INT (value to be added to the input value) |
| **M** | INT (maximum value for the output) |
| **Output** | INT (output value) |
| | INC adds to the input X the Value D and ensures that the output INC is not does not exceed the value of M. If the result from the addition of X and D is greater than M, then it starts again at 0. The feature is especially useful when addressing arrays and buffers. Even the positioning of absolute encoders it can be used. INC can be used to decrementieren with a negative D, while INC will ensure that the result is not below zero. If subtract 1 from zero INC starts again at M. |
| **INC** | = X + D, because D can take the maximum value M. |
| | If INC > M so INC starts again at 0. |
| | If INC < 0 so INC starts again at M |

![inc](inc.gif)

**Example:**

```iecst
INC(3, 2, 5) ergibt 5 INC(4, 2, 5) ergibt 0 INC(0,-1,7) ergibt 7
```
