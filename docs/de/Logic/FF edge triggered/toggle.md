<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## TOGGLE

| | |
|:---|:---|
| **Type** | Funktionsbaustein |
| **Input	CLK** | BOOL (Takteingang) |
| **RST** | BOOL (asynchroner Reset) |
| **Output	Q** | BOOL (Ausgang) |
| | TOGGLE ist ein flankengetriggertes Toggle Flip-Flop mit asynchronem Reset-Eingang. Das TOGGLE Flip-Flop invertiert den Ausgang Q bei einer steigenden Flanke von CLK. Der Ausgang ändert bei jeder steigenden Flanke von CLK seinen Zustand. |

![toggle](toggle.gif)
