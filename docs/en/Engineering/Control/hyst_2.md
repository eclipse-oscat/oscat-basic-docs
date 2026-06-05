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
| **Input	IN** | REAL (input value) |
| **VAL** | REAL (mean of the hysteresis) |
| **HYS** | REAL (width of hysteresis) |
| **Output	Q** | BOOL (output) |
| **WIN** | BOOL (shows that IN is in between LOW and HIGH) |
| | HYST_2 hysteresis is a module for the logic thresholds by a mean and a hysteresis is defined. The lower threshold value is VAL - HYS / 2 and the upper threshold for VAL + HYS / 2 |
| | A detailed description of the hysteresis and an application example, see HYST_1. |

![hyst_2](hyst_2.gif)

![hyst_2a](hyst_2a.gif)
