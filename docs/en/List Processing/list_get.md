<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LIST_GET

| | |
|:---|:---|
| **Type	Function** | STRING(LIST_LENGTH) |
| **Input	SEP** | BYTE (separation sign the list) |
| **POS** | INT (position of list element) |
| **I / O	LIST** | STRING(LIST_LENGTH) (input list) |
| **Output** | STRING (String output) |
| | LIST_GET delivers the item at the position POS from a list. The list consists of  Strings (elements) that begin with the separation character SEP. The first element of the list has the position 1. |

![list_get](list_get.gif)

**Example:**

```iecst
LIST_GET('&ABC&23&&NEXT', 38, 1) = 'ABC' LIST_GET('&ABC&23&&NEXT', 38, 2) = '23' LIST_GET('&ABC&23&&NEXT', 38, 3) = '' LIST_GET('&ABC&23&&NEXT', 38, 4) = 'NEXT' LIST_GET('&ABC&23&&NEXT', 38, 5) = '' LIST_GET('&ABC&23&&NEXT', 38, 0) = ''
```
