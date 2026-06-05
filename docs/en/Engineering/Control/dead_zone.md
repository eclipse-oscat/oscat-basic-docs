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
| **Input	X** | REAL (input) |
| **L** | REAL (  Lockout  Value) |
| **Output** | REAL (output value) |
| | DEAD_ZONE  is a  linear  transfer function with dead zone. The output equals the input signal when the absolute value of the input is greater than L. |
| | DEAD_ZONE  = X if ABS(X) > L |
| | DEAD_ZONE = 0 if ABS(X) <= L |

![dead_zone](dead_zone.gif)

![dead_zone_diag](dead_zone_diag.gif)
