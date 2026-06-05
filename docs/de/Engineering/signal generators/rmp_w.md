<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## RMP_W

| | |
|:---|:---|
| **Type** | Funktionsbaustein |
| **Input	SET** | BOOL (Set Eingang) |
| **PT** | TIME (Dauer einer Rampe 0..65535) |
| **E** | BOOL (Freigabeeingang) |
| **UP** | BOOL (Richtung UP=TRUE bedeutet Up) |
| **RST** | BOOL (Reset Eingang) |
| **Output	OUT** | Byte (Ausgangssignal) |
| **BUSY** | BOOL (TRUE, wenn Rampe läuft) |
| **HIGH** | BOOL (Maximaler Ausgangswert ist erreicht) |
| **LOW** | BOOL (Minimaler Ausgangswert ist erreicht) |
| | RMP_W ist ein Rampengenerator mit 16 Bit (2 Byte) Auflösung. Die Rampe von 0.. 65535 wird in maximal 65536 Schritte unterteilt und in einer Zeit von PT einmal komplett durchlaufen. Ein Freigabesignal E schaltet den Rampengenerator an oder aus. Ein asynchroner Reset setzt jederzeit den Ausgang auf 0 und ein Impuls am Set-Eingang setzt den Ausgang auf 65535. Mit einem UD-Eingang kann die Richtung AUF (UD = TRUE) oder Ab (UD = FALSE) vorgegeben werden. Der Ausgang BUSY = TRUE zeigt an, dass eine Rampe aktiv ist. BUSY = FALSE bedeutet der Ausgang ist stabil. Die Ausgänge HIGH und LOW werden TRUE wenn der Ausgang OUT das untere oder obere Limit (0 bzw. 65535) erreicht hat. |
| | Beim festlegen von PT ist zu beachten, dass eine SPS mit 5ms Zykluszeit 65536*5 = 327 Sekunden für eine Rampe benötigt. Wird die Zeit PT kürzer als die Zykluszeit mal 65536 gewählt, wird die Flanke in entsprechend größere Sprünge übersetzt. Die Rampe wird in diesen Fall aus weniger als 65536 Schritten je Zyklus zusammengesetzt.  PT darf T#0s sein, dann schaltet der Ausgang zwischen Minimal- und Maximal-Wert hin und her. |
| | Eine detaillierte Beschreibung finden Sie beim Modul RMP_B. Die Funktion ist absolut identisch mit der Ausnahme, dass der Ausgang OUT 8 Bit anstelle von 16 Bit weit ist. |

![rmp_w](rmp_w.gif)
