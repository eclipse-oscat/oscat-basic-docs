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
| **PT1** | TIME (Impulsdauer) |
| **PTD** | TIME (Delay bis neuer Impuls erzeugt werden kann) |
| **RST** | BOOL (asynchroner Reset) |
| **Output	Q** | BOOL (Ausgangspuls) |
| | TP_1D ist ein flankengetriggerter Pulsgenerator der bei steigender Flanke an IN einen Ausgangsimpuls an Q mit der Dauer PT1 erzeugt. Wird während des Ausgangsimpulses eine weitere steigende Flanke an IN erzeugt, so verlängert sich der Ausgangsimpuls so dass nach der letzten steigenden Flanke der Ausgang für die Dauer von PT TRUE bleibt. Nach Ablauf der Pulsdauer PT1 blockiert der Baustein für die Zeit PTD den Ausgang. ein neuer Impuls kann erst nach Ablauf der Zeit PTD wieder gestartet werden. Der Baustein kann jederzeit mit einem TRUE am Eingang RST zurückgesetzt werden. Der Ausgang W zeigt an das der Baustein im Wartezyklus ist und solange W = TRUE kann kein neuer Impuls gestartet werden. |

![tp_1d](tp_1d.gif)
