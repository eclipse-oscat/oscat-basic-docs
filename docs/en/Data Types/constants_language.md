<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## This structure defines different languages as String  Constants. The variable   LANGUAGE of the global variables list provides itself in the library.

| | | |
|:---|:---|:---|
| ***. DEFAULT** | INT: = 1 defines the  default  Language | |
| ***.LMAX** | INT:= 3 | specifies how many languages are available |
| ***.WEEKDAYS** | ARRAY[1..3, 1..7] OF STRING(10):= ' Monday','Tuesday' | |
| ***.WEEKDAYS2** | ARRAY[1..3, 1..7] OF STRING(2):= | |
| ***.MONTHS** | ARRAY[1..3, 1..12] OF STRING(10):= 'January','February', | |
| ***.MONTHS3** | ARRAY[1..3, 1..12] OF STRING(3):= | |
| ***.DIRS** | ARRAY[1..3,0..15] OF STRING(3):= | 'N','NNE','NE','ENE','E', |

(1 = English, 2 = German, 3 = French)

The  Default  Language is always used when the language 0 is called. If the language setting > 0 then the corresponding language is selected.

Language setting: 0 (the default language specified in DEFAULTis used

(1 = English, 2 = German 3 = French)

other languages are defined by expanding the structure CONSTANTS_LANGUAGE.

'Wednesday','Thursday','Friday','Saturday','Sunday','Monday',

'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday';

'Mo','Tu','We','Th','Fr','Sa','Su',

'Mo','Di','Mi','Do','Fr','Sa','So';

'March','April','May','June','July','August','September','October',	'November','December',

'January','February','March','April','May','June','July','August',

'September','October','November','December';

'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec',

'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','October','Nov','Dec';

'ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW'

'N','NNE','NO','ENE','O','OSO','SO','SSO','S','SSW','SW','WSW'

'W','WNW','NW','NW';
