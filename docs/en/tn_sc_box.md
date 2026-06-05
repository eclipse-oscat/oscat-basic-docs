<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_SC_BOX

| | |
|:---|:---|
| **Type** | Function module |
| **INPUT** | Iin_Y1: INT (Y1 coordinate of the area) |
| **Iin_X1** | INT: (X1 coordinate of the area) |
| **Iin_Y2** | INT (Y2 coordinate of the area) |
| **Iin_X2** | INT: (X2-coordinate of the area) |
| **Iby_FILL** | BYTE: (fill in the character of the area) |
| **Iby_ATTR** | BYTE: (color code to fill the area) |
| **Iby_BORDER** | BYTE: (type of frame) |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| | The module TN_SC_BOX is used to draw a rectangular area, that is filled with the specified character in Iby_FILL. With parameter Iby_ATTR fill color can be specified. The fill area is drawn with a border that is given by Iin_BORDER. |
| **Border types** |  |
| | 0 = no border |
| | 1 = frame with a single line |
| | 2 = frame double line |
| | 3 = frame with spaces |

![TN_SC_BOX](TN_SC_BOX.gif)

![tn_sc_box_type.GIF](tn_sc_box_type.GIF)

**Beispiel:**

Example: Box with leaders 'X' and white color to blue Representation with Iin_BORDER value 0,1,2 and 3 (from left to right)
