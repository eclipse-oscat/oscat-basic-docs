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
| **Input	ENQ** | BOOL (  Enable  Input) |
| **TH1** | TIME (set time HIGH when TS =  LOW) |
| **TL1** | TIME (set time LOW when TS  = LOW) |
| **TH2** | TIME (set time HIGH when TS = HIGH) |
| **TL2** | TIME (set time LOW when TS =  HIGH) |
| **TS** | BOOL (selection for the end times) |
| **Output	Q** | BOOL (binary output) |
| **TL** | TIME (elapsed time when Q = FALSE) |
| **TH** | TIME (elapsed time when Q = TRUE) |
| | GEN_PW2 generates an output signal with a definable time TH? for HIGH and TL for LOW. Using the input TS is switched between two sets of parameters (TL1, TH1 and TL2, TH2). On startup or after a ENQ = TRUE, the module begins with the LOW phase at the output. |

![100000000000005F000000769C068384](100000000000005F000000769C068384.gif)
