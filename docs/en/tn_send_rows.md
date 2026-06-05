<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TN_SEND_ROWS

| | |
|:---|:---|
| **Type** | Function module |
| **INPUT	S_BUF_SIZE** | UINT (number of bytes in S_BUF.BUFFER) |
| **IN_OUT	IP_C** | IP_CONTROL   (Connection data) |
| **S_BUF** | NETWORK_BUFFER (transmit data) |
| **Xus_TN_SCREEN** | us_TN_SCREEN |
| | The module TN_SEND_ROWS is used to automatically update the graphical changes to the Telnet screen, by send the modified lines to the Telnet client. |
| | If you change the Telnet screen a color or a character in a line, this line is always automatically selected for update. The module checks if marked at Xus_TN_SCREEN.bya_Line_Update [0..23] one or more lines, and generates an ANSI-code byte-stream which is sent to the Telnet client. Furthermore, when Xus_TN_SCREEN.bo_Clear_Screen = TRUE a clear screen is triggered. Upon detection of a new Telnet client connection automatically all the rows are marked for  update, so that the whole screen content is rendered. If the required amount of data greater than S_BUF.BUFFER the data is automatically output in blocks. |

![tn_send_rows](tn_send_rows.gif)
