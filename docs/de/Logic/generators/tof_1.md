<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktionsbaustein

| | |
|:---|:---|
| **Input	IN** | BOOL (Eingangssignal) |
| **PT** | TIME (Ausschaltverzögerung) |
| **RST** | BOOL (asynchroner Reset) |
| **Output	Q** | BOOL (Ausgangssignal) |
| | TOF_1 verlängert einen Eingangsimpuls an IN um die Zeit PT. TOF_1 hat die gleiche Funktionalität wie TOF aus der Standard LIB, jedoch mit einem zusätzlichen asynchronen Reset Eingang. |

![tof_1](tof_1.gif)

![tof_1_timing](tof_1_timing.gif)
