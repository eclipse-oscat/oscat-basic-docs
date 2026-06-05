<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MANUAL_2

| | |
|:---|:---|
| **Type** | Function module |
| **Input	IN** | BOOL (Input) |
| **ENA** | BOOL (block  Enable  Input) |
| **ON** | BOOL (Forces the output to TRUE) |
| **OFF** | BOOL (Forces the output to FALSE) |
| **MAN** | BOOL (starting mode in manual mode) |
| **Output	Q** | BOOL (output) |
| **STATUS** | BYTE (ESR compliant status output) |
| | MANUAL_2   , a digital signal and override switches between manual and automatic operation. The module is designed so that a 3-position switch switches between off and auto. In the automatic the signal mode is set to IN, in the case of enforced off, the OFF is set to TRUE and in the case of enforced on, tho ON set to TRUE. If the two inputs ON and OFF are FALSE switch the input IN directly to the output Q. However, are both inputs ON and OFF simultaneously set to TRUE, the state of the input MAN is switched to the output. The input MAN can also be used to define a priority for ON or OFF which passes the value of the MAN is always on the output if both inputs ON and OFF are simultaneously true. Is the input ENA set to FALSE, the output is always set to FALSE, the module is  disabled.  The following table defines the operating modes of the module. The STATUS output is ESR compatible and reports on the status of the module to corresponding ESR components. |

![manual_2](manual_2.gif)

| IN | ENA | ON | OFF | MAN | Q | STATUS |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| - | L | - | - | - | L | 104 | Disabled |
| X | H | L | L | - | X | 100 | Auto Mode |
| - | H | H | L | - | H | 101 | forceHigh |
| - | H | L | H | - | L | 102 | forceLow |
| - | H | H | H | X | X | 103 | Manual Input |
| - | H | H | H | L | L | 103 | ForcewithPriorityfor OFF |
| - | H | H | H | H | H | 103 | ForcewithPriorityfor ON |
