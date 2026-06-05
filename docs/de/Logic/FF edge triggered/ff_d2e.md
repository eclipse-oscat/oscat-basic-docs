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
| **Input	D0** | BOOL (Data 0 in) |
| **D1** | BOOL (Data 1 in) |
| **CLK** | BOOL (Takteingang) |
| **RST** | BOOL (asynchroner Reset) |
| **Output	Q0** | BOOL (Data 0 out) |
| **Q1** | BOOL (Data 1 out) |
| | FF_D2E ist ein 2 Bit flankengetriggertes D-Flip-Flop mit asynchronem Reset-Eingang. Das D-Flip-Flop speichert die Werte am Eingang D mit einer steigenden Flanke am CLK Eingang. |
| | D1D0CLKRSTQ1Q0 |

![ff_d2e](ff_d2e.gif)
