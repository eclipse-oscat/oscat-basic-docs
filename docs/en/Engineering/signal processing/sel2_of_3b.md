<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function: BOOL

| | |
|:---|:---|
| **Input	IN1** | BOOL (input 1) |
| **IN2** | BOOL (input 2) |
| **IN2** | BOOL (input 2) |
| **TD** | TIME (  Delay for output for W) |
| **Output	Q** | BOOL (output) |
| **W** | BOOL (warning) |
| | SEL2_OF_3B evaluates 3 redundant binary inputs and provides the value, that at least 2 of the 3 inputs have, at output Q. If one of the three inputs has a different value than the other two, the output W is set as a warning. A response delay TD can be defined for the output W that at different timing while switching the inputs the Output W does not respond. |

![sel2_of_3b](sel2_of_3b.gif)
