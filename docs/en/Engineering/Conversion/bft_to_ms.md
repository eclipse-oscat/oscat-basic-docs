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
| **Input	BFT** | INT (wind force on the Beaufort scale) |
| **Output	MS** | REAL (Wind speed in meters / second) |
| | BFT_TO_MS calculete wind speeds on the Beaufort scale in meters per second. |
| **The calculation is done using the formula** |  |
| | BFT_TO_MS = 0.836m/s * B^3/2 |

![bft_to_ms](bft_to_ms.gif)
