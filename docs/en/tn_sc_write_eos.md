<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_SC_WRITE_EOS

| | |
|:---|:---|
| **Type** | Function module |
| **INPUT	Iby_ATTR** | BYTE: (color code - font color) |
| **Ist_STRING** | STRING (text) |
| **IN_OUT	Xus_TN_SCREEN** | Us_TN_SCREEN |
| | The module TN_SC_WRITE_EOS passes at the end position of the last, with   TN_SC_WRITE or TN_SC_WRITE_EOS issued text, the text Ist_STRING with the color of  Iby_ATTR. |
| | This allows to continuous passes texts without the need to always pass the new coordinates. |

![tn_sc_write_eos](tn_sc_write_eos.gif)
