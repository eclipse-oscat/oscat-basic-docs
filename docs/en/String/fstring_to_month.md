<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: INT

| | |
|:---|:---|
| **Input	MTH** | STRING(20) (String input) |
| **LANG** | INT (language) |
| **Output** | INT (month number 1..12) |
| | FSTRING_TO_MONTH determines from a string containing a month name or abbreviation the value of the month. The function can handle both the month names and abbreviations as input as well as a number of the month. |
| | FSTRING_TO_MONTH('Januar',2) = 1 |
| | FSTRING_TO_MONTH('Jan',2) = 1 |
| | FSTRING_TO_MONTH('11',0) = 11 |
| | The input LANG selects the used language, 0 = the default in the Setup , 1 = English .... more info about the language settings, see the chapter Data Types. |

![fstring_to_month](fstring_to_month.gif)
