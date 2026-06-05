<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : BOOL

| | |
|:---|:---|
| **Input	UTC** | DATE_TIME (Weltzeit) |
| **Output** | BOOL (TRUE, wenn Sommerzeit) |
| | Die Funktion DST überprüft, ob im Augenblick Sommerzeit herrscht, oder nicht. Sie kann dazu benutzt werden eine vorhandene nicht-Sommerzeit fähige Uhr sekundengenau auf Sommer- und Winterzeit umzustellen. |
| **Die Funktion DST schaltet am letzten Sonntag des März um 01** | 00 UTC (02:00 MEZ) auf Sommerzeit (03:00 MESZ) und am letzten Sonntag des Oktober um 01:00 UTC (03:00 MESZ) auf 02:00 MEZ zurück. Der Ausgang von DST ist dann TRUE, wenn Sommerzeit herrscht. |
| **Die Sommerzeit wird aufgrund von UTC (Weltzeit) berechnet. Eine Berechnung von Ortszeit nach Sommerzeit ist generell nicht möglich weil im letzten Sonntag des Oktobers die Stunde von 02** | 00 - 03:00 MEZ beziehungsweise MESZ doppelt existiert. Die Sommerzeit wird in allen Ländern der EU seit 1992 zur selben Sekunde nach Weltzeit umgestellt. In Mitteleuropa um 02:00, in England um 01:00 und in Griechenland um 04:00. Durch die Berechnung mithilfe der Weltzeit wird die Sommerzeit für alle Europäischen Zeitzonen richtig berechnet. |

![dst](dst.gif)
