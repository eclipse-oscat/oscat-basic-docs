<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_SC_LINE

| | |
|:---|:---|
| **Type** | Function module |
| **INPUT** | Iin_Y1: INT (Y1 coordinate of the line) |
| **Iin_X1** | INT: (X1 coordinate of the line) |
| **Iin_Y2** | INT (Y2 coordinate of the line) |
| **Iin_X2** | INT: (X2-coordinate of the line) |
| **Iby_ATTR** | BYTE: (color code of the line) |
| **Iby_BORDER** | BYTE: (type of line) |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| | The module TN_SC_LINE is used to draw horizontal and vertical lines. By means of the X1/Y1 and X2/Y2 coordinates defines the beginning and the end of the line. The line type is passed by Iin_BORDER and the color code with Iby_ATTR. If when drawing a line and another line of this type cut, automatically the appropriate crossing sign is used. |
| **Border types** |  |
| | 1 = line with single line |
| | 2 = line with double line |
| | > 2 = line is drawn with the specified character in Iin_BORDER |

![tn_sc_line](tn_sc_line.gif)

![tn_sc_line_sample](tn_sc_line_sample.gif)

**Beispiel:**

Example: Horizontal line: type single-line Vertical line: Type Double-Line Horizontal and vertical lines crossed: Single-Line Type Horizontal and vertical lines crossed: Type Double-Line Horizontal line: type character (X)
