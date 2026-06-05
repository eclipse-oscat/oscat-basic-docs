<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TELNET_PRINT

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	IP_C** | IP_C (parameterization) |
| **S_BUF** | NETWORK_BUFFER (transmit data) |
| **INPUT	TEXT** | STRING(string_length) (output text) |
| **S_BUF_SIZE** | UINT (  (Size of the buffer S_BUF  ) |
| **ENABLE** | BOOL (enable communication) |
| **SEND** | BOOL (positive edge - Send offense) |
| **OPTION** | BYTE (Send Options) |
| **BACK_COLOR** | BYTE (background color) |
| **FRONT_COLOR** | BYTE (foreground color) |
| **X_pos** | BYTE (X-coordinate of the cursor position) |
| **Y_pos** | BYTE (Y-coordinate of the cursor position) |
| **PORT** | WORD (port-number) |
| **OUTPUT** | READY: BOOL (module ready) |
| **DONE** | BOOL (positive edge - Transmission completed) |
| | The module enables easy output of text to a TELNET console. At the parameter TEXT is passed the desired string. To unlock the module for communication, ENABLE = 1 must be set, so that the registration takes place at IP_CONTROL. With  parameter PORT can be defined the port number you want, if not value is specified the default  port 23 is activated. With BACK_COLOR and FRONT_COLOR can be defined the colors you want, if the function parameter OPTION is activated. The parameters X_pos and Y_pos pass the desired coordinates of the text. If indicated in X_pos and Y_pos the value "0", the text position is inactive, and the text are always appended at the current cursor  position. The standard Telnet console allows X_pos (horizontal) from 1 to 80 and a   Y_pos (Vertical) 1 to 25. The behavior here can in turn be modified by OPTION (Autowrap, carriage return, line feed, Buf_Flush etc..). If a large quantity of text will be issued, there may be a buffering enabled, so the data are written if either the buffer is full (this is from the module induced independently) or this is signaled by the amended OPTION parameter. By SEND = 1, the data is written into the buffer. The parameters may only be changed again if READY is 1, and with DONE the data acquisition was displayed as a positive edge. |
| **OPTION** |  |
| **FRONT_COLOR** |  |
| **BACK_COLOR** |  |

![telnet_print](telnet_print.gif)

![telnet_print_schema](telnet_print_schema.gif)

| BIT | Function | Description |
| --- | --- | --- |
| 0 | SCREEN_INIT | After connecting to the TELNET console the entire screen is cleared.   If the COLOR OPTION is selected, the screen BACK_COLOR will be deleted. |
| 1 | AUTOWRAP | In AUTOWRAP = 1, the write cursor is on reaching the end of line is automatically set to a next line. If the text output the X,Y positions are always specified with, it is better when AUTOWRAP = 0. |
| 2 | COLOR | Enables the color mode, it will  apply BACK_COLOR and FRONT_COLOR  to the output. |
| 3 | NEW_LINE | In NEW_LINE = 1 is automatically a carriage return and line feed added to the end of the text. So the next text output starts a new line. But this is only useful if no X_pos and Y_pos be specified. |
| 4 | RESERVE |  |
| 5 | RESERVE |  |
| 6 | RESERVE |  |
| 7 | NO_BUF_FLUSH | Prevents the data in the buffer to be sent immediately. Only if the buffer is completely full, or this option is disabled, the data is sent. Allows   fast sending many texts in the same cycle |

| Byte | Color | Byte | Color |
| --- | --- | --- | --- |
| 0 | Black | 16 | Flashing Black |
| 1 | Light Red | 17 | Flashing Light Red |
| 2 | Light Green | 18 | Flashing Light Green |
| 3 | Yellow | 19 | Flashing Yellow |
| 4 | Light Blue | 20 | Flashing Light Blue |
| 5 | Pink / Light Magenta | 21 | Flashing Pink / Light Magenta |
| 6 | Light Cyan | 22 | Flashing Light Cyan |
| 7 | White | 23 | Flashing White |
| 8 | Black | 24 | Flashing Black |
| 9 | Red | 25 | Flashing Red |
| 10 | Green | 26 | Flashing Green |
| 11 | Brown | 27 | Flashing Brown |
| 12 | Blue | 28 | Flashing Blue |
| 13 | Purple / Magenta | 29 | Purple / Magenta |
| 14 | Cyan | 30 | Flashing Cyan |
| 15 | Gray | 31 | Flashing Gray |

| Byte | Color |
| --- | --- |
| 0 | Black |
| 1 | Red |
| 2 | Green |
| 3 | Brown |
| 4 | Blue |
| 5 | Purple / Magenta |
| 6 | Cyan |
| 7 | Gray |
