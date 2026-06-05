<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : REAL

| | |
|:---|:---|
| **Input	X** | REAL (Eingangswert) |
| **N** | INT (Exponentialwert) |
| **Output** | REAL (Ergebnis X^N) |
| | EXPN berechnet den Exponentialwert von X^N für Ganzzahlige N. EXPN ist speziell für SPS ohne FloatingPointEinheit geschrieben und ist ca. 30 mal schneller als die IEC Standard Funktion EXPT(). Zu beachten ist der Sonderfall das 0^0 wie mathematisch definiert eine 1 ergibt und nicht eine 0. |
| **EXPN(10,-2) = 0.01** | EXPN(1.5,2) = 2.25 |
| | EXPN(0,0) = 1 |

![expn](expn.gif)
