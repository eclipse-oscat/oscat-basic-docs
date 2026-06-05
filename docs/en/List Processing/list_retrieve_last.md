<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LIST_RETRIEVE_LAST

| | |
|:---|:---|
| **Type	Function** | STRING(LIST_LENGTH) |
| **Input	SEP** | BYTE (separation sign the list) |
| **I / O	LIST** | STRING(LIST_LENGTH) (input list) |
| **Output** | STRING(LIST_LENGTH) (string output) |
| | LIST_RETRIEVE_LAST passes the last item from a list and deletes the corresponding item in the list. The list consists of   Strings (elements) that begin with the separation character SEP. |

![list_retrieve_last](list_retrieve_last.gif)
