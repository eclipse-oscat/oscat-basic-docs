<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MONTH_TO_STRING

| | |
|:---|:---|
| **Type	Function** | STRING (10) |
| **Input	MTH** | INT (Month 1..12) |
| **LANG** | INT (Language 0 = Default  ) |
| **LX** | INT (length of string) |
| **Output** | STRING (10) (output value) |
| **MONTH_TO_STRING convert a month number to its equivalent string. The input MTH passes the month** | 1 =January, 12 = December. The input LANG chooses the language: 1 = English and 2 = German. LANG = 0 used as  Default  the language specified in the Global Setup variable LANGUAGE_DEFAULT. The input LX sets the length of the string to be generated: 0 = full month name, 3 = 3-letter abbreviation, all other values at the input LX are undefined. |
| | The strings produced by the module, and the supported languages are defined in the Global  Constants  and can be expanded and changed. |
| | MONTH_TO_STRING(1,0,0) = 'January' |
| | dependent on the global constant LANGUAGE_DEFAULT |
| | MONTH_TO_STRING(1,2,0) = 'Januar' |
| | MONTH_TO_STRING(1,2,3) = 'Jan' |

![month_to_string](month_to_string.gif)
