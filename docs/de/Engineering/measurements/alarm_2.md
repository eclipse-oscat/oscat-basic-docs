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
| **Input	X** | REAL (Eingangswert) |
| **RST** | BOOL (Reset Eingang für Alarm Ausgang) |
| **Output	LOW** | BOOL (TRUE, wenn X < TRIGGER_LOW) |
| | ALARM_2 prüft ob X die Grenzen HI_1 oder HI_2 nach oben übersteigt und setzt dabei die Ausgänge Q1_HI oder Q2_HI auf TRUE. Falls die Grenzen LO_1 oder LO_2 unterschritten werden wird entsprechend Q1_LO oder Q2_LO auf TRUE gesetzt. Die Ausgänge bleiben solange TRUE wie die entsprechende Grenze über- beziehungsweise unter-schritten wird. Um ein Flattern der Ausgänge zu unterbinden kann alternativ auch eine Hysterese HYS eingestellt werden. Wird HYS auf einen Wert > 0 gesetzt, so wird der entsprechende Ausgang erst dann gesetzt wenn die Grenze um mehr als HYS / 2 überschritten beziehungsweise unterschritten wird. Entsprechend muss der Eingang X die Grenze um mehr als HYS / 2 unter beziehungsweise überschreiten bevor die entsprechenden Ausgänge wieder gelöscht werden. |
| | ALARM_2 kann zum Beispiel mit HI_1 und LO_1 den Pegel eines Flüssigkeitsbehälters steuern und mit HI_2 und LO_2 einen Alarm auslösen wenn ein kritischer Pegel unterschritten beziehungsweise überschritten wird. |

![10000000000000F00000010C320ECBAA](10000000000000F00000010C320ECBAA.png)
