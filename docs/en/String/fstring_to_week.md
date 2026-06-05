<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: BYTE

| | |
|:---|:---|
| **Input	WEEK** | STRING(60) (String input) |
| **LANG** | INT (language) |
| **Output** | BYTE (Bitpattern of week days) |
| | FSTRING_TO_WEEK decode a list of days on the form 'MO,TU,3'in a Bitpattern (bit6 = MO...Bit0 = So) For the evaluation each of the first two letters of the list elements are evaluated, the rest are ignored. If the string contains spaces they will be removed. The days of the week can be present in both upper-or lowercase. LANG specifies the language used, 1 = English, 2 = German, 0 is the default language defined in the setup. |
| | Mo = 1; Di, Tu = 2; We, Mi = 3; Th, Do = 4; Fr = 5; Sa = 6; So, Su = 7 |
| | Since the function evaluates only the first two characters, the weekdays may also be spelled out (Monday) format. |
| | As an alternative form, the weekday can be specified as number 1..7. |
| | The list includes the weekdays unsorted and separated by commas. |
| | FSTRING_TO_WEEK ('Mo,Tu,Sa',2) = 2#01100010. |

![fstring_to_week](fstring_to_week.gif)
