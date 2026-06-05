<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## This structure defines location-dependent constants. The variable SETUP the global variables list places it in the library.

| | | |
|:---|:---|:---|
| ***.EXTENDED_ASCII** | BOOL:= TRUE extends the ASCII character set to | special characters eg ÄÖÜ |
| ***.CHARNAME[1..4]** | STRING(253) stores Unicode character names | |
| ***.MTH_OFS** | ARRAY[1..12] OF INT:= 0, 31, 59, 90, 120, 151, 181, 212, | 243, 273, 304, 334; |
| ***.DECADES** | ARRAY[0..8] OF REAL:= 1,10,100,1000,10000,100000, | |

MTH_OFS is used in various date functions, the array represents the respective current day offset for the months of the year. The 1 February of a year eg is the day 31 + 1

1000000,10000000,100000000;
