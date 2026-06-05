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
| **Input	I0** | BOOL (Eingangssignal 0) |
| **I1** | BOOL (Eingangssignal 1) |
| **I2** | BOOL (Eingangssignal 2) |
| **I3** | BOOL (Eingangssignal 3) |
| **E** | BOOL (Enable Eingang) |
| **MODE** | INT (Betriebsmodus) |
| **Output	OUT** | BOOL (Ausgangssignal) |
| **TP** | BOOL (TRUE wenn sich Ausgang verändert hat) |
| | INTERLOCK_4 packt die 4 Eingangswerte I0..I3 in die Bits (0..3) des Ausgangs OUT. Bei jeder Veränderung des Ausgangs wird der Ausgang TP für einen Zyklus TRUE damit weitere Bausteine zur Verarbeitung getriggert werden können. Ist der Eingang E = FALSE bleiben alle Ausgänge auf 0 bzw. FALSE. Der Eingang MODE stellt verschiedene Betriebsmode des Bausteins ein. |

![interlock_4](interlock_4.gif)

| MODE | Bedeutung |
| --- | --- |
| 0 | Eingänge werden direkt im Ausgangsbyte dargestelltz.B. I0, I2 = TRUE	OUT = 2#0000_0101 |
| 1 | Nur der Eingang mit der höchsten Eingangsnummer wird ausgegeben, die anderen werden ignoriert.z.B. I0,I1,I2 = TRUE:	OUT = 2#0000_0100 |
| 2 | Nur der zuletzt aktivierte Eingang wird ausgegeben. |
| 3 | Ein aktivierter Eingang disabled alle anderen Eingänge. |
