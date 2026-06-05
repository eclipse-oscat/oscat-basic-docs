<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LOWERCASE

| | |
|:---|:---|
| **Type	Function** | STRING |
| **Input	STR** | STRING (String input) |
| **Output** | STRING (STRING in lowercase) |
| | The function LOWERCASE converts the   String  STR to lower case. During conversion, the Global Setup EXTENDED_ASCII constant is considered. If EXTENDED_ASCII = TRUE extended ASCII character set are evaluated according to ISO 8859-1. Umlauts like Ä, Ö, Ü are considered only if the global constant   EXTENDED_ASCII = TRUE. A detailed description of the code change is found in the function TO_LOWER. |

![lowercase](lowercase.gif)
