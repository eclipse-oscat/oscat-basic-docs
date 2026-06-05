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
| **Output** | INT (position of the last letter that is not a number) |
| | The function FINDB_NONUM STR searches from right to left and returns the last position which is not a number. |
| | Numbers are the letters "0..9" and "." |

![findb_nonum](findb_nonum.gif)

**Example:**

```iecst
FINDB_NONUM('4+33+1') = 5
```
