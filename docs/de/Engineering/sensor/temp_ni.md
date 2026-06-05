<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : REAL

| | |
|:---|:---|
| **Input	RES** | REAL (Widerstandswert in Ohm) |
| **R0** | REAL (Widerstand bei 0 °C) |
| **Output** | REAL (gemessene Temperatur) |
| | RES_NI berechnet die Temperatur eines NI-Widerstandsfühlers aus den Eingangswerten RES (gemessener Widerstandswert) und R0 (Widerstand bei 0°C). |
| **Die Berechnung ist geeignet für einen Temperaturbereich von -60 .. +180 °C und erfolgt nach folgender Formal** |  |
| | RES_NI = R0 + A*T + B*T²+C*T4 |
| | A = 0.5485; B = 0.665E-3; C = 2.805E-9 |

![temp_ni](temp_ni.gif)

![temp_ni_table](temp_ni_table.gif)
