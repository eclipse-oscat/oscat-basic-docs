<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SCALE_B2

| | |
|:---|:---|
| **Type	Function** | REAL |
| **Input	IN1** | Byte (input value 1) |
| **IN2** | Byte (input value 2) |
| **K** | REAL (multiplier) |
| **O** | REAL (offset) |
| **Output** | REAL (output value) |
| **Setup	IN1_MIN** | REAL (lowest value for IN1) |
| **IN1_MAX** | REAL (highest value for IN1) |
| **IN2_MIN** | REAL (lowest value for IN2) |
| **IN2_MAX** | REAL (highest value for IN2) |
| | SCALE_B2 calculates from the input value IN and the setup values  IN_MIN and IN_MAX an internal value, then add all the internal values, multiplies the sum by K and add the offset O. An input value IN1 = 0 means IN1_MIN is taken into account, IN1 = 255 means IN1_MAX is considered. K is not connected then the first multiplier |
| **Out  =** | (in1 * (IN1_MAX – IN1_MIN) / 255 + IN1_MIN 	+ in2 * |
| **(IN2_MAX –** | IN2_MIN) / 255 + IN2_MIN) * K + O |
| | SCALE_B2 can be used, for example, to calculate total air quantities in ventilation systems. Also, wherever there are controlled mixers used and the resulting total amount has to be calculated. |

![scale_B2](scale_b2.gif)

![scale_b2_sample](scale_b2_sample.gif)
![scale_b2_sample_](scale_b2_sample_.gif)

**Example:**

Example: IN0 is an air valve, which controls the air volume between 100m³/h and 600m³/h for the setting values IN0 - Controls (0-255). IN1 is an exhaust device that the exhaust air from 0m³/h to 400 m³/h for the control values IN1 controls 0- 255. The setup values for this application are: IN0_MIN = 100, IN0_MAX = 600, IN1_MIN = 0, IN1_MAX = -400. The resulting total air volume for K = 1 and O = 0 (no multiplier and no offset) then varies from -300 (IN0 = 0 and IN1 = 255) to +600 (IN0 = 255 and IN1 = 0). For an input value IN0 = 128 (flap 50%) and IN1 = 128 (fan at 50%) is the output value 250m³ - 200m³ = 50 m³. The input offset can also be used to cascade modules.
