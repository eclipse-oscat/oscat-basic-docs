<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_SC_WRITE_ATTR

| | |
|:---|:---|
| **Type** | Function module |
| **INPUT	Iin_Y** | INT (Y coordinate) |
| **[fzy] Iin_X** | INT: (X coordinate) |
| **Iby_ATTR** | BYTE: (color code) |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| | The module TN_SC_WRITE_ATTR changes at the given coordinates   Iin_Y, Iin_Y the colorcode to change without changing the existing character at that position. |

![tn_sc_write_attr](tn_sc_write_attr.gif)
