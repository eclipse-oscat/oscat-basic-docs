<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_SC_XY2_ERROR

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **INPUT** | X1: INT: (X1 coordinate of the area) |
| **Y1** | INT: (Y1 coordinate of the area) |
| **X2** | INT: (X2-coordinate of the area) |
| **Y2** | INT: (Y2 coordinate of the area) |
| | The module TN_SC_XY2_ERROR checks whether the specified coordinates   are within the screen area. The area may not cross off the screen. If the check fails, as result is passes TRUE. |

![tn_sc_xy2_error](tn_sc_xy2_error.gif)
