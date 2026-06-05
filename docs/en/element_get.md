<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## ELEMENT_GET

| | |
|:---|:---|
| **Type	Function** | STRING(ELEMENT_LENGTH) |
| **Input	SEP** | BYTE (separation character of the elements) |
| **POS** | INT (of the item) |
| **I / O	ELEMENT** | STRING(ELEMENT_LENGTH) (input list) |
| **Output** | STRING (String output) |
| | ELEMENT_GET passes the item at the position POS  from a list. The list consists of strings which are separated by the separation character SEP. The first element of the list has the position 0 |

![element_get](element_get.gif)

**Beispiel:**

Examples: ELEMENT_GET('ABC,23,,NEXT', 44, 0) = 'ABC' ELEMENT_GET('ABC,23,,NEXT', 44, 1) = '23' ELEMENT_GET('ABC,23,,NEXT', 44, 2) = '' ELEMENT_GET('ABC,23,,NEXT', 44, 3) = 'NEXT' ELEMENT_GET('ABC,23,,NEXT', 44, 4) = '' ELEMENT_GET('', 44, 0) = ''
