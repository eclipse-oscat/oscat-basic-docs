<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IS_NCC

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	STR** | STRING (String input) |
| **CMP** | STRING (comparison characters) |
| **Output** | BOOL (TRUE if STR none of the character listed in the STRING CMP |
| | contains) |
| | IS_NCC tests whether the string STR none of the in STR  listed characters are included. Is a character of CMP found in STR, the function returns FALSE. |

![is_ncc](is_ncc.gif)

**Example:**

```iecst
IS_NCC('3.14', ',-+()') = TRUE IS_NCC('-3.14', ',-+()') = FALSE
```
