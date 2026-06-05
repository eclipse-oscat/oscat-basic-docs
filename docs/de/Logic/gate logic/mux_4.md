<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MUX_4

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	D0** | BOOL (Eingang 0) |
| **D1** | BOOL (Eingang 1) |
| **D2** | BOOL (Eingang 2) |
| **D3** | BOOL (Eingang 3) |
| **Output** | BOOL (D0, wenn A0=0 und A1 = 0, usw...) |
| | MUX_4 ist ein 4-Bit Multiplexer. Der Ausgang entspricht D0, wenn A0=0 und A1=0. Er entspricht D3, wenn A0=1 und A1=1. |
| **Logische Verknüpfung** | MUX_4  = 	D0 & /A0 & /A1 + D1 & A0 & /A1 |
| | + D2 & /A0 & A1 + D3 & A0 & A1 |

![mux_4](mux_4.gif)

![mux_4_trace](mux_4_trace.gif)
