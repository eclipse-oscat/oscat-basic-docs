<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MS_TO_BFT

| | |
|:---|:---|
| **Type** | Function |
| **Input	MS** | INT (force on the Beaufort scale) |
| **Output	MS** | REAL (Wind speed in meters / second) |
| | MS_TO_BFT converts wind speeds of meters per second in the Beaufort scale. |
| **The calculation is done using the formula** |  |
| | MS_TO_BFT = (MS * 1.196172)^2/3 |

![ms_to_bft](ms_to_bft.gif)
