<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_SC_FILL

| | |
|:---|:---|
| **Type** | Function module |
| **INPUT** | Iin_Y1: INT (Y1 coordinate of the area) |
| **Iin_X1** | INT: (X1 coordinate of the area) |
| **Iin_Y2** | INT (Y2 coordinate of the area) |
| **Iin_X2** | INT: (X2-coordinate of the area) |
| **Iby_CHAR** | BYTE: (character to fill in the the area) |
| **Iby_ATTR** | BYTE: (color code to fill the area) |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| | The module TN_SC_FILL is used to draw a rectangular area, that is filled with the specified character in Iby_FILL. |

![tn_sc_fill](tn_sc_fill.gif)

![tn_sc_fill_sample](tn_sc_fill_sample.gif)

**Beispiel:**

Example: Box with leaders 'X' and white color to blue
