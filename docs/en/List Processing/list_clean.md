<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LIST_CLEAN

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	SEP** | BYTE (separation sign the list) |
| **I / O	LIST** | STRING(LIST_LENGTH) (input list) |
| **Output** | BOOL (TRUE) |
| | LIST_CLEAN cleans a list of empty elements. The list consists of   Strings (elements) that begin with the separation character SEP. |
| | LIST_CLEAN('&ABC$23&&NEXT', 38) = '&ABC&23&NEXT' |
| | LIST_CLEAN('&&23&&NEXT&', 38) = '&23&NEXT' |
| | LIST_CLEAN('&&&&', 38) = '' |

![list_clean](list_clean.gif)
