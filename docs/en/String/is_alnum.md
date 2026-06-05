<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## IS_ALNUM

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	STR** | STRING (String input) |
| **Output** | BOOL (TRUE if STR contains only letters or numbers) |
| | IS_ALNUM test if in the string STR are only letters or numbers. If an incorrect, non-alphanumeric character is found the function returns FALSE. STR contains only letters or numbers, the result is TRUE. Letters are the characters A..Z and a..Z, and numbers are the signs 0..9. In examining the Global Setup constant EXTENDED_ASCII is considered. If EXTENDED_ASCII = TRUE the extended ASCII character-set to be considered in accordance with ISO 8859-1. Umlauts like Ä, Ö, Ü are considered only if the global constant   EXTENDED_ASCII = TRUE. |

![is_alnum](is_alnum.gif)
