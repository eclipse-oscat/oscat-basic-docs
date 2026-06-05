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
| **Input	STR** | STRING (String input) |
| **Output** | INT (of the last character, which is a number or point) |
| | The function FINDB_NUM searches STR from right to left and returns the last position that is a number. |
| | Numbers are the letters "0..9" and "." |

![findb_num](findb_num.gif)

**Example:**

```iecst
FINDB_NUM('4+33+1hh') = 6
```
