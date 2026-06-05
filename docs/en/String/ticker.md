<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function module

| | |
|:---|:---|
| **Input	N** | INT (length of the display  Strings  ) |
| **PT** | TIME (slide delay,  Default  = T#1s) |
| **I / O	TEXT** | STRING (String input) |
| **Output	DISPLAY** | STRING (String output) |
| | TICKER generate at the output DISPLAY a running script. At the output DISPLAY a substring of text with the length N is output. DISPLAY is passed to output in a time frame of PT and starts at each pass from one place to the left of the input string TEXT. The scrolling text is generated only when N < than the length of TEXT. If N >= length of text then the  String  TEXT is directly represented at the output of DISPLAY. |

![ticker](ticker.gif)
