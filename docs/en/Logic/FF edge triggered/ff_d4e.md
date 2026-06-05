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
| **Input	D0** | BOOL (Data 0 in) |
| **D1** | BOOL (Data 1 in) |
| **D2** | BOOL (Data 2 in) |
| **D3** | BOOL (Data 3 in) |
| **CLK** | BOOL (clock input) |
| **RST** | BOOL (asynchronous reset) |
| **Output	Q0** | BOOL (Data 0 Out) |
| **Q1** | BOOL (Data 1 Out) |
| **Q2** | BOOL (Data 2 Out) |
| **Q3** | BOOL (Data 3 Out) |
| | FF_D2E is a 4-bit edge-triggered D-Flip-Flop with asynchronous reset input. The D-Flip-Flop stores the values at the input D at a rising edge on CLK. Detailed information can be found in the block FF_D2E. |

![ff_d4e](ff_d4e.gif)
