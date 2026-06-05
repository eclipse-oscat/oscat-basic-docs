<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SCALE_B8

| | |
|:---|:---|
| **Type	Function** | REAL |
| **Input** | IN1 .. 8 bytes (input values) |
| **K** | REAL (multiplier) |
| **O** | REAL (offset) |
| **Output** | REAL (output value) |
| **Setup	IN_MIN** | REAL (lowest value for IN) |
| **IN_MAX** | REAL (highest value for IN) |
| | SCALE_B8 calculates from the input values IN and the setup values IN_MIN and IN_MAX internal values, then add all the internal values, multiplies the sum by K and add the offset O. An input value IN = 0 means IN_MIN is included, IN = 255 means IN_MAX is not considered. K is not connected then the first multiplier |
| **OUT** | = (in1 * (IN1_MAX – IN1_MIN) / 255 + IN1_MIN |
| | + in2 * (IN2_MAX – IN2_MIN) / 255 + IN2_MIN |
| | + in3 * (IN3_MAX – IN3_MIN) / 255 + IN3_MIN |
| | + in4 * (IN4_MAX – IN4_MIN) / 255 + IN4_MIN |
| | + in5 * (IN5_MAX – IN5_MIN) / 255 + IN5_MIN |
| | + in6 * (IN6_MAX – IN6_MIN) / 255 + IN6_MIN |
| | + in7 * (IN7_MAX – IN7_MIN) / 255 + IN7_MIN |
| | + in8 * (IN8_MAX – IN8_MIN) / 255 + IN8_MIN) * K + O |
| | SCALE_B8 can be used, for example,to calculate total air quantities in ventilation systems, or wherever controlled mixers are used and the resulting total needs to be calculated . More detailed explanations you can find at SCALE_B2. |

![scale_B8](scale_b8.gif)
