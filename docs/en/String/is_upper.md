<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IS_UPPER

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	STR** | STRING (String input) |
| **Output** | BOOL (TRUE if STR contains only capital letters) |
| | IS_UPPER checks if in the string STR all capital letters are included. If an incorrect, non capital character is found the function returns FALSE. If in STR are only capital letters included, the function returns TRUE. In examining the Global Setup EXTENDED_ASCII constant is considered. If EXTENDED_ASCII = TRUE the extended ASCII character-set to be considered in accordance with ISO 8859-1. Umlauts like Ä, Ö, Ü are considered only if the global constant   EXTENDED_ASCII = TRUE. |

![is_upper](is_upper.gif)
