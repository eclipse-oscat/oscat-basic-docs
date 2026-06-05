<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	TEMP_NTC

| | |
|:---|:---|
| **Input	RES** | REAL (measured resistance in ohms) |
| **RN** | REAL (resistance of the sensor at 25°C) |
| **B** | REAL (specification of the sensor) |
| **Output** | REAL (measured temperature) |
| | TEMP_NTC calculates from the measured resistance and the parameters of the sensor, the measured temperature. RN is the resistance of the sensor at 25°C, and B depends on the sensor and the specification of the sensor. |
| **The module calculates the temperature according to the following formula** |  |

![temp_ntc](temp_ntc.gif)

![temp_ntc_formula](temp_ntc_formula.gif)
