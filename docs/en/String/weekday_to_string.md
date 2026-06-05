<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: STRING (10)

| | |
|:---|:---|
| **Input	WDAY** | INT (weekday 1..7) |
| **LANG** | INT (Language 0 = Default  ) |
| **LX** | INT (length of string) |
| **Output** | STRING (10) (output value) |
| **WEEKDAY_TO_STRING converts a weekday in the corresponding string. The input WDAY indicates the corresponding day of the week** | 1 = Monday and 7 = Sunday. The input LANG chooses the language: 1 = English and 2 = German. LANG = 0 used as  Default  the language specified in the Global Setup variable LANGUAGE_DEFAULT. [fzy] The input LX sets the length of the string to be generated: 0 = full month name, 3 = 3-letter abbreviation, all other values at the input LX are undefined. |
| | The strings produced by the module, and the supported languages are defined in the Global  Constants  and can be expanded and changed. |
| | WEEKDAY_TO_STRING(1,0,0) = '  Monday  ' |
| | dependent on the global constant LANGUAGE_DEFAULT |
| | WEEKDAY_TO_STRING(1,2,0) = '  Monday  ' |
| | WEEKDAY_TO_STRING(1,0,2) = '  Mon  ' |

![weekday_to_string](weekday_to_string.gif)
