<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## PRINT_SF

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	PRINTF_DATA** | ARRAY[1..11] OF STRING(string_length)						(Parameter data) |
| **STR** | STRING (  String_length  ) (String result) |
| | With PRINT_SF a STRING can be added dynamically with a part of a string. The position of the substring to be inserted is indicated by '~' tilde character and the subsequent number defines the parameter number. '~ 1' to '~ 9' are thus processed automatically. If the insert of the substring reached the maximum number of characters, so instead of the substring  '..' is inserted. |
| | VAR |
| **LITER** | REAL := 545.4; |
| **FUELLZEIT** | INT := 25; |
| **NAME** | STRING: = 'tank content'; |
| **PARA** | ARRAY[1..11] OF STRING(string_length); |
| **PS** | PRINT_SF; |
| | END_VAR |
| **PARA[1]** | = REAL_TO_STRING(liters);  (* Parameter 1: string to convert *) |
| **PARA[2]** | = INT_TO_STRING(filling time);  (* Parameter 2: string to convert *) |
| **PARA[3]** | = NAME;  (* Parameter 3: *) |
| **PS.STR** | =  ' ~3: ~1 Liter, filling time: ~2 Min.' ;  (* Text output-mask *) |
| **PS.PRINTF_DATA** | = PARA;  (* Pass parameter data structure *) |
| | PS();  (* Module version *) |
| | The string PS. STR then has the following content |
| **'Tank Capacity** | 545.4 liters, filling time: 25 min' |

![print_sf](print_sf.gif)
