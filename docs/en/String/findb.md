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
| **Input	STR1** | STRING (String input) |
| **STR1** | STRING (String input) |
| **Output** | INT (position of last occurrence of STR2 in STR1) |
| | The function FINDB searched for the presence of STR2 in STR1 and returns the last position of STR2 in STR1. |
| | If STR2 is not found, a 0 is returned. |

![findb](findb.gif)

**Beispiel:**

Example:	FINDB('abs12fir12bus12', '12') = 14
