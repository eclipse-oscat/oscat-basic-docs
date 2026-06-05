<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: STRING

| | |
|:---|:---|
| **Input	C** | BYTE (Character Code) |
| **L** | INT (length of string) |
| **Output** | STRING (result STRING) |
| | FILL creates a string consisting of the symbol C with the length L. |
| | FILL(49,5) = '11111' |
| | The FILL function evaluates the Global Setup constant STRING_LENGTH and limits the maximum length L of the string to STRING_LENGTH. |

![fill](fill.gif)
