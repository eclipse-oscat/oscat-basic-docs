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
| **Input	E** | BOOL (  Enable  for outputs) |
| **SET** | BOOL (Asynchronous Set) |
| **IN** | BYTE (default value for set) |
| **UP** | BOOL (forward switch edge-triggered) |
| **DN** | BOOL (reverse switch edge-triggered) |
| **RST** | BOOL (asynchronous reset) |
| **Output	Q0 .. Q7** | BOOL (outputs) |
| **STATE** | BYTE (status output) |
| | SELECT_8 set only one output to TRUE  as long as E = TRUE. The active output Q0..Q7 can be selected by the SET input and the value at the input IN. A TRUE at SET and a value of 5 at the input IN set the output Q5 to TRUE while all other outputs are set to FALSE. A TRUE at the input RST set output Q0 to TRUE. With inputs UP is switched from an output Qn to Qn +1, while the input DN switches an output Qn to Qn-1. The input EN must be TRUE so that an output is TRUE, if EN is FALSE, all outputs are FALSE. A FALSE at E does not affected the function of other inputs. Thus, even with a FALSE at input EN can be switched up or down with UP or DN . The inputs UP and DN are edge-triggered and respond to the rising edge. The state output always shows which output is currently selected. |

![select_8](select_8.gif)

|  | E | SET | IN | UP | DN | RST | Q | STATE |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reset | X | - | - | - | - | 1 | Q0 if EN=1 | 0 |
| Set | X | 1 | N | - | - | 0 | QN if EN=1 | N |
| up | X | 0 | - | ↑ | 0 | 0 | QN+1 if EN=1 | N + 1 |
| down | X | 0 | - | 0 | ↑ | 0 | QN-1 if EN=1 | N - 1 |
