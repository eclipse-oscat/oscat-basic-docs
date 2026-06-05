<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## HOLIDAY

| | |
|:---|:---|
| **Type** | Function module |
| **Input	Date_in** | DATE (input date) |
| **Langue** | INT (desired language) |
| **FRIDAY** | BOOL (Y is true on Friday when TRUE) |
| **SATURDAY** | BOOL (Y is true on Saturdays if TRUE) |
| **SUNDAY** | BOOL (Y is TRUE if TRUE on Sundays) |
| **I / O	HOLIDAYS** | ARRAY [0..29] of HOLIDAY_DATA |
| **Output	Y** | BOOL (TRUE if DATE_IN is a holiday) |
| **Name** | STRING(30) (name of present-day holiday) |
| | The HOLIDAY function shows the output Y with TRUE holidays and also provides the name of the current holiday at the output NAME. HOLIDAY can, in addition to celebration days during the weekdays Friday, Saturday or Sunday be active and deliver at the output Y TRUE, depending on whether the inputs are FRIDAY, SATURDAY or SUNDAY set to TRUE. In the array HOLIDAYS are name and date of holidays defined and also universally adaptable to other countries. Holidays can be defined as a fixed date, with a distance of Easter or the week before a fixed date. The input LANGU selects the appropriate language from the setup data so that expenditure for Friday, Saturday and Sunday can be customized language-specific. [fzy] The languages are global constants in the "LOCATION SETUP" defined and can be expanded or adapted. |
| | In the external array HOLIDAYS up to 30 holidays can be defined. Examples are located in the description of the data type HOLYDAY_DATA. |

![holiday](holiday.gif)
