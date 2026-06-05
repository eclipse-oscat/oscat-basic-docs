<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LIST_ADD

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	SEP** | BYTE (separation sign the list) |
| **INS** | STRING (New Item) |
| **I / O	LIST** | STRING(LIST_LENGTH) (input list) |
| **Output** | BOOL (TRUE) |
| | LIST_ADD adds another element to the end of a list. The list consists of  Strings (elements) that begin with the separation character SEP. |

![list_add](list_add.gif)

**Example:**

```iecst
LIST_ADD('&ABC&23&&NEXT', 38, 'NEW') = '&ABC&23&&NEXT&NEW'
```
