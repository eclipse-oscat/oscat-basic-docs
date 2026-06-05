<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function module

| | |
|:---|:---|
| **Input	MS** | REAL (meters / second) |
| **KMH** | REAL (kilometers / hour) |
| **CN** | REAL (knots = miles / hour) |
| **MH** | REAL (miles / hour) |
| **Output	YMS** | REAL (meters / second) |
| **YKMH** | REAL  (Kilometers / hour) |
| **YKN** | REAL (knots = miles / hour) |
| **YMH** | REAL (miles / hour) |
| | The module SPEED converts various common units in the units for speed. Normally, only the input to be converted is occupied and the remaining inputs remain free. However, if several inputs loaded with values, the values of all inputs are converted accordingly and then summed. |
| | 1 ms = meters / second = 3.6 km / h |
| | 1 kmh = kilometers / hour = 1 / 3, 6 m / s |
| | 1 knot = knot = 1 nautical mile / hour = 0.5144 m / s |
| | Mh = 1 mile per hour = 0.44704 m / s |

![speed](speed.gif)
