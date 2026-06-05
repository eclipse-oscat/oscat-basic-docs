<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MUX_2

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	D0** | BOOL (Bit 0) |
| **D1** | BOOL (Bit 1) |
| **A0** | BOOL (Adresse) |
| **Output** | BOOL (D0, wenn A0=0 und D1, wenn A0=1) |
| | MUX_2 ist ein 2-Bit Multiplexer. Der Ausgang entspricht D0, wenn A0=0 und er entspricht D1, wenn A0=1. |
| **Logische Verknüpfung** | MUX_2 = D0 & /A0 + D1 & A0 |

![mux_2](mux_2.gif)

![mux_2_trace](mux_2_trace.gif)
