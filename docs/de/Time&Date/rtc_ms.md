<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## RTC_MS

| | |
|:---|:---|
| **Type** | Funktionsbaustein |
| **Input	SET** | BOOL (Set Eingang) |
| **SDT** | DT (Set Datum und Zeit) |
| **SMS** | INT (Set Millisekunden) |
| **Output	XDT** | DT (Datums und Zeit Ausgang) |
| **XMS** | INT (Millisekunden Ausgang) |
| | RTC_MS ist ein Uhrenbaustein mit einer Auflösung von Millisekunden und Datum. Die Uhrzeit wird automatisch beim ersten Start und immer dann wenn SET auf TRUE ist auf den Wert von SDT und SMS gesetzt. Wenn SET = FALSE läuft die Zeit selbständig weiter und liefert am Ausgang XDT das aktuelle Datum und die Uhrzeit, sowie am Ausgang XMS die Millisekunden. Der Ausgang XMS zählt in jeder Sekunde von 0 - 999 und beginnt mit der nächsten Sekunde wieder bei 0. Die Genauigkeit der Uhr hängt vom Millisekunden Timer der SPS ab. |

![rtc_ms](rtc_ms.gif)
