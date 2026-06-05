<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## RDM

| | |
|:---|:---|
| **Type	Function** | REAL |
| **Input	LAST** | REAL (last calculated value) |
| **Output** | REAL (random number between 0 and 1) |
| | RDM calculates a pseudo-  random number. This is the PLC's internal  Timer  read and converted into a pseudo-random number. Because RDM's is written as a function and not as a function module, it can not save data between 2 calls and should therefore be used with caution. RDM is only called once per cycle, it produces reasonable good results. But when it is repeatedly called within a cycle, it delivers the same number, most likely because of the PLC  timer  is still on the same value. If the function is repeatedly used within a cycle, so it must be passed with each call a different number of starts (LAST). It shall be called only once per cycle, is sufficient to call RDM(0). As a starting number for each call, the last calculated number of RDM can be used. Supplied by RDM random numbers between 0 and 1, which does not contain 1 (0 <=random number < 1) |

![rdm](rdm.gif)
