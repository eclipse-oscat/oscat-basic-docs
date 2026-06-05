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
| **Input	IN** | BOOL (Eingangssignal) |
| **T1** | TIME (Einschaltverzögerung) |
| **T2** | TIME (Ausschaltverzögerung) |
| **Output	Q** | BOOL (Ausgangspuls) |
| | TONOF erzeugt eine Einschaltverzögerung T1 und eine Ausschaltverzögerung T2 |
| | Das steigende Flanke des Eingangssignals IN wird um T1 verzögert und die Fallende Flanke von IN wird um T2 verzögert. |

![100000000000005000000049529D89CD](100000000000005000000049529D89CD.gif)

![tonof_timing](tonof_timing.gif)
