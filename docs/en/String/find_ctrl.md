<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: INT

| | |
|:---|:---|
| **Input	STR** | STRING (input STRING) |
| **POS** | INT (start position) |
| **Output** | INT (the first character is a control character) |
| | FIND_CTRL searches the string str starting at position POS and returns the position at which the next control character is. Control characters are all characters whose value is less than 32 or 127. |

![find_ctrl](find_ctrl.gif)
