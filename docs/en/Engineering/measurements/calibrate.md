<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function module

| | |
|:---|:---|
| **Input	X** | REAL (input) |
| **CO** | BOOL (pulse for storing the offset) |
| **CS** | BOOL (pulse for storing the gain factor) |
| **Output	Y** | REAL (Calibrated output signal) |
| **Setup	Y_OFFSET** | REAL (Y value in which the offset is set) |
| **Y_SCALE** | REAL (Y value in which the amplification factor |
| | is set) |
| | CALIBRATE serves for calibrating an analog signal. In order to allow a calibrating two reference values (Y_OFFSET and Y_SCALE) must be set by double-clicking on the icon of the module. Y_OFFSET is the starting value at which the offset is set by a pulse at CO and Y_SCALE is the value at which the gain is determined. A calibration can only be successful if the first offset and gain are then calibrated. |

![calibrate](calibrate.gif)

**Example:**

Example  : An input signal of 4..20 mA can be calibrated at the temperature values from 0 .. 70 ° C. Therefore the setup variables Y_OFFSET = 0 and Y_SCALE = 70 are set. Then the sensor is placed in ice water and after the response of the sensor, a pulse at the input C0 is triggered to initiate a calculation of the correction value for offset and store it internally . Next, then the sensor is applied with 70 ° C and after the response a pules is triggered on the CS input, which calculates in the module a gain factor that is stored internally. The calibration values are permanently stored. That means, they are also not lost when a reset is executed, or turn off the power to the PLC.
