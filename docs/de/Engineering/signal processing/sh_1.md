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
| **Input	IN** | REAL (Eingangssignal) |
| **PT** | TIME (Abtastzeit) |
| **Output	OUT** | REAL (Ausgangssignal) |
| **TRIG** | BOOL (Trigger Output) |
| | SH_1 ist ein Sampleund Hold Baustein mit einstellbarer Abtastzeit. Er speichert alle PT das Eingangssignal IN am Ausgang OUT. Nach jedem update von OUT bleibt TRIG für einen Zyklus TRUE. |
| **Das Folgende Beispiel erläutert die Funktionsweise von SH_1** |  |

![sh_1](sh_1.gif)

![sh_1_sample](sh_1_sample.gif)
![sh_1_trace](sh_1_trace.gif)
