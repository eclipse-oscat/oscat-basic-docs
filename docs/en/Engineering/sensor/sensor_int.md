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
| **Input	 VOLTAGE** | REAL (measured in volts) |
| **CURRENT** | REAL (Current measured in amperes) |
| **RP** | REAL (parallel parasitic resistance in ohms) |
| **RS** | REAL (serial parasitic resistance in ohms) |
| **Output** | REAL (resistance of the sensor) |
| | SENSOR_INT calculate the sensor resistance, taking into account the parasitic resistances, which usually affect the measurement. The A / D converter measures either current at a fixed voltage or voltage at a fixed current. The resulting resistance is not only the resistance of the sensor, but is composed of the resistance of the sensor and two parasitic resistances RS and RP. Since the parasitic resistances remain constant, they can be compensated and the real resistance of the sensor can be calculated. |
| | RPRSRXABBetween the terminals A and B  measured resistance (measured by current and voltage) is a total resistance of the sensor resistance in parallel to the parasitic resistance RP and the line resistance RS. RS and RP, are compensated the real resistance RX is calculated. The modules can TEMP_ then be calculated as the exact temperature. |

![sensor_int](sensor_int.gif)
