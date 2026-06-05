<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## REAL_TO_STRF

| | |
|:---|:---|
| **Type	Function** | STRING(20) |
| **Input	IN** | REAL (input value) |
| **N** | INT (number of decimal places) |
| **D** | STRING(1) (decimal punctuation character) |
| **Output** | STRING (String output) |
| | REAL_TO_STRF converts a REAL value to a string with a fixed number of decimal N. At the conversion entirely in a normal number format XXX.NNN is converted. At the conversion IN is rounded to N digits after the decimal point and then converted into a  String  to the format XXX.NNN. When N = 0, the REAL number is rounded to 0 digits after the decimal point and the result is passed as an integer without a point and decimal places. If the number IN is less than, as with N decimal places can be captured, a zero is passed. The decimal places are always filled up to N digits with zeros. The maximum string length is 20 digits.  The D input determines which character represents the decimal point. |

![real_to_strf](real_to_strf.gif)

**Example:**

```iecst
REAL_TO_STRF(3.14159,4,'.') = '3.1416' REAL_TO_STRF(3.14159,0,'.') = '3' REAL_TO_STRF(0.04159,3,'.') = '0.042' REAL_TO_STRF(0.001,2',') = '0,00'
```
