<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: BOOL

| | |
|:---|:---|
| **Input	STR** | STRING (String input) |
| **Output** | BOOL (TRUE if STR contains only control characters) |
| | IS_CTRL tests whether the string STR are only control characters included. If another character is found the function returns FALSE. If in STR are only control characters included, the function returns TRUE. Control characters are the characters with the decimal 0..31 and 127 |

![is_ctrl](is_ctrl.gif)
