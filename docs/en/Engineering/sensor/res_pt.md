<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: REAL

| | |
|:---|:---|
| **Input	T** | REAL (temperature in °C) |
| **R0** | REAL (resistance at 0° C) |
| **Output** | REAL (resistance) |
| | RES_PT calculates the resistance of a PT resistance sensor from the input values T (temperature in °C) and R0 (resistance at 0°C). |
| **The calculation is done using the formula** |  |
| | for temperatures > 0 °C |
| | RES_PT = R0 * (1 + A*T + B*T²) |
| | and for temperatures below 0 ° C |
| | RES_PT = R0 * (1 + A*T + B*T² + C*(T-100)*T³ |
| | A = 3.90802E-3 |
| | B = -5.80195E-7 |
| | C = -427350E-12 |
| | The calculation is suitable for temperatures from -200.. +850°C. |

![res_pt](res_pt.gif)

![res_pt_tabelle](res_pt_tabelle.gif)
