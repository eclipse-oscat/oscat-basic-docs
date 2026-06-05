<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LIST_RETRIEVE

| | |
|:---|:---|
| **Type	Function** | STRING |
| **Input	SEP** | BYTE (separation sign the list) |
| **POS** | INT (position of list element) |
| **I / O	LIST** | STRING(LIST_LENGTH) (input list) |
| **Output** | STRING(LIST_LENGTH) (string output) |
| | LIST_RETRIEVE passes the item at the position POS from a list and deletes the corresponding item in the list. The list consists of   Strings (elements) that begin with the separation character SEP. The first element of the list is at position 1. The function returns an empty string if no element is at the position POS. |

![list_retrieve](list_retrieve.gif)

**Beispiel:**

Example : LIST_RETRIEVE('&ABC&23&&NX&, 38, 1) = 'ABC'	LIST = '&23&&NX&' LIST_RETRIEVE('&ABC&23&&NX', 38, 2) = '23'	LIST = '&ABC&&NX' LIST_RETRIEVE('&ABC&23&&NX', 38, 3) = ''	LIST = '&ABC&23&NX' LIST_RETRIEVE('&ABC&23&&NX', 38, 4) = 'NEXT'	LIST = '&ABC&23&' LIST_RETRIEVE('&ABC&23&&NX', 38, 5) = ''	LIST = '&ABC&23&&NX' LIST_RETRIEVE('&ABC&23&&NX', 38, 0) = ''	LIST = '&ABC&23&&NX'
