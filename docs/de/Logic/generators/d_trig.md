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
| **Input	IN** | DWORD (Eingangssignal) |
| **Output	Q** | BOOL (Ausgangssignal) |
| **X** | DWORD (Veränderung des Eingangssignals) |
| | Der Funktionsbaustein D_TRIG erzeugt nach einer Veränderung am Eingang IN einen Ausgangsimpuls für exakt einen SPS Zyklus. Der Baustein funktioniert vergleichbar mit den Standardfunktionsbausteinen R_TRIG und F_TRIG und dem in der OSCAT Bibliothek enthaltenen Baustein B_TRIG. Während B_TRIG, R_TRIG und F_TRIG einen Booleschen Eingang überwachen, triggert der Baustein D_TRIG auf jede Veränderung des DWORD-Eingangs IN. Wenn sich der Eingangswert verändert hat, so wird der Ausgang Q für einen SPS Zyklus auf TRUE gesetzt und der Ausgang X gibt an, um welchen Wert sich der Eingang IN verändert hat. Der Eingang, sowie der Ausgang sind von Typ DWORD. Der Eingang kann auch WORD und BYTE Typen verarbeiten. Beim Ausgang X ist zu beachten, dass DWORD kein Vorzeichen hat und deshalb eine Veränderung um -1 am Eingang nicht -1 sondern die Zahl 2^32-2 ausgibt. Mit der Standardfunktion DWORD_TO_INT kann der Ausgang X in einen Integer umgewandelt werden, welcher dann auch negative Veränderungen richtig darstellt. |
| **Das nachfolgende Beispiel zeigt die Anwendung von D_TRIG wenn sich der Eingang vom Wert 5 nach 2 verändert** |  |

![d_trig](d_trig.gif)

![d_trig_sample](d_trig_sample.gif)
