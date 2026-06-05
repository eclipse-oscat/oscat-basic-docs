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
| **Input	SET** | BOOL (Asynchronous Set) |
| **D0..D7** | BOOL (Data  Input  Bit 0..7) |
| **CLR** | BOOL (gradual reset input) |
| **RST** | BOOL (Asynchronous set input) |
| **Output	Q0..Q7** | BOOL (event outputs) |
| | STORE_8 is an 8-event memory. A TRUE one of the inputs D0..D7 sets the corresponding output Q0 .. Q7. The asynchronous set and reset inputs (SET, RST) set all outputs simultaneously to TRUE or FALSE. IF during a reset one of the inputs TRUE after the reset, the corresponding output is immediately set to TRUE. If edge-triggered inputs are required, use TP_R modules before of the module STRORE_8. This allows the user to use both edge triggered as well as condition-triggered inputs  simultaneously. Input CLR clears with a rising edge on CLR only one event, beginning with the highest priority output that is just TRUE.   If with CLR a output Q has cleared which input Q is TRUE, so the output D will be set to TRUE at the next cycle. |

![store_8](store_8.gif)
