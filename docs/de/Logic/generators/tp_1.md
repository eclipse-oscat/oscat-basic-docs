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
| **PT** | TIME (Impulsdauer) |
| **RST** | BOOL (asynchroner Reset) |
| **Output	Q** | BOOL (Ausgangspuls) |
| | TP_1 ist ein flankengetriggerter Pulsgenerator der bei steigender Flanke an IN einen Ausgangsimpuls an Q mit der Dauer PT erzeugt. Wird während des Ausgangsimpulses eine weitere steigende Flanke an IN erzeugt, so verlängert sich der Ausgangsimpuls so dass nach der letzten steigenden Flanke der Ausgang für die Dauer von PT TRUE bleibt. Der Baustein kann jederzeit mit einem TRUE am Eingang RST zurückgesetzt werden. |
| **Zeitverhalten von TP_1** |  |

![tp_1](tp_1.gif)

![tp_1_trace](tp_1_trace.gif)
