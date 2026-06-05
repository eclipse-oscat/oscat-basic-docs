<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_SC_WRITE

| | |
|:---|:---|
| **Type** | Function module |
| **INPUT	Iin_Y** | INT (Y coordinate) |
| **[fzy] Iin_X** | INT: (X coordinate) |
| **Iby_ATTR** | BYTE: (color code - font color) |
| **Ist_STRING** | STRING (text) |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| | The module TN_SC_WRITE passes the text Ist_STRING at the coordinates    Iin_Y, Iin_Y  and the color of Iby_ATTR. |
| | Is specified color code = 0, then the string is displayed without change the existing old color information at he respective character positions. |

![tn_sc_write](tn_sc_write.gif)
