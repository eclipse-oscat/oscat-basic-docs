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
| **Input	IN1..IN4** | BOOL (Eingang für Bitpattern S1..S4) |
| **TS** | TIME (Schaltzeit) |
| **Output	Q** | BOOL (Ausgangssignal) |
| | SIGNAL_4 erzeugt ein Ausgangssignal Q das einem von 4 Bitpattern (S1 .. S4) entspricht. Das Bitpattern wird in TS langen Schritten Ausgegeben. Die Eingänge IN1..IN4 sind priorisierte Eingänge. Ein TRUE an IN1 überschreibt allen anderen Eingänge, IN2 überschreibt IN3 und IN4 hat die niedrigste Priorität. Eine weiterführende Beschreibung der Funktion von SIGNAL_4 befindet sich unter SIGNAL. Die 4 verschiedenen Bitpattern sind in Setup Variablen S1 .. S4 abgelegt und können vom Anwender jederzeit angepasst werden. |
| **Der Baustein hat per folgende Bitpattern voreingestellt, welche aber vom Anwender bei Bedarf verändert werden können** |  |
| | S1 = 2#1111_1111 |
| | S2 = 2#1111_0000 |
| | S3 = 2#1010_1010 |
| | S4 = 2#1010_0000 |
| **Setup	S1 .. S4** | BYTE (Bitpattern S1 .. S4) |

![signal_4](signal_4.gif)

![signal_4%20pattern](signal_4%20pattern.gif)
