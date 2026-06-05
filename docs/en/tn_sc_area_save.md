<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_SC_AREA_SAVE

| | |
|:---|:---|
| **Type** | Function module |
| **INPUT** | Iin_Y1: INT (Y1 coordinate of the area) |
| **Iin_X1** | INT: (X1 coordinate of the area) |
| **Iin_Y2** | INT (Y2 coordinate of the area) |
| **Iin_X2** | INT: (X2-coordinate of the area) |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| | The module TN_SC_AREA_SAVE allows you to save of rectangular areas of the screen before it is modified by other drawing operations. This is mainly done before the call from the module BAR-MENU and MENU-POPUP  , because these are the elements as an overlay graphic. Means X1, Y1 and X2, Y2 are given the coordinates of the secured area of the screen. The data are saved in the data area Xus_TN_SCREEN.bya_BACKUP [x]. Here the coordinates and the actual characters and color information is stored. The buffer can hold up half the area of the screen. |

![TN_SC_AREA_SAVE](TN_SC_AREA_SAVE.gif)
