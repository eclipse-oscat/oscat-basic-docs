<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## RAD

| | |
|:---|:---|
| **Type	Function** | REAL |
| **Input	DEG** | REAL (angle in degrees) |
| **Output** | REAL (angle in radians) |
| | The RAD function converts an angle value from degrees to radians. Taking into account that the DEG will not be greater than 360. If DEG is greater than 360, 360 is to be subtracted as long as DEG is again between 0-360 °. |
| **RAD(0) = 0** | RAD(180) = π RAD(360) = 0	RAD(540) = π |

![rad](rad.gif)
