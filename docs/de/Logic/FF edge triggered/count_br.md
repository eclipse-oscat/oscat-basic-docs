<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## COUNT_BR

| | |
|:---|:---|
| **Type** | Funktionsbaustein |
| **Input	SET** | BOOL (asynchroner Set) |
| **IN** | BYTE (Vorgabewert für Set) |
| **UP** | BOOL (Vorwärts Schalter flankengetriggert) |
| **DN** | BOOL (Rückwärts Schalter flankengetriggert) |
| **STEP** | BYTE (Schrittweite des Counters) |
| **MX** | BYTE (Maximalwert des Counters) |
| **RST** | BOOL (asynchroner Reset) |
| **Output	CNT** | BYTE (Ausgang) |
| | COUNT_BR ist ein Byte Zähler der von 0 bis MX zählt und dann wieder bei 0 beginnt. Der Zähler kann mittels 2 flankengetriggerten Eingängen UP und DN sowohl vorwärts als auch Rückwärts Zählen. beim erreichen eines Endwerts 0 oder MX wird wieder bei 0 beziehungsweise MX weiter gezählt. Der Eingang STEP legt die Schrittweite des Zählers fest. Mit einem TRUE am Eingang SET wird der Zähler auf den an IN anliegenden Wert gesetzt. Ein Reset Eingang RST setzt den Zähler jederzeit auf 0. |
| **Falls die unabhängigen Eingänge UP und DN mit CLK und einen Steuereingang UP/DN ersetzt werden sollen kann dies mittels zwei AND Gattern vor den Eingängen erfolgen** |  |
| | COUNT_BR kann bei jedem UP oder Down Befehl mit individueller Schrittweite Arbeiten, dabei ist zu beachten das der Zähler sich so verhält als ob er intern die Anzahl von STEP Schritte Vorwärts oder Rückwärts zählt. |

![count_br](count_br.gif)

![count_dr_sample](count_dr_sample.gif)

**Beispiel:**

Beispiel: MX = 50, STEP=10 Der Zähler Arbeitet dann wie folgt: 0,10,20,30,40,50,9,19,...... Wird in diesem Beispiel 50 erreicht, so wird dies als Maximalwert erkannt und bei 0 weitergezählt. Intern sieht dies wie folgt aus: 50,0,1,2,3,4,5,6,7,8,9 also genau 50 + 10 wenn nach 50 wieder die 0 kommt. Die Implementation eines Zählers 0...50 in Zehnerschritten sieht wie folgt aus: MX = 59, STEP = 10: ergibt die folge 0,10...50,0,10 der Übergang von 50 auf 0 ist dann genau 10 Schritte.

|  | SET | IN | UP | DN | STEP | RST | CNT |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Reset | - | - | - | - | - | 1 | 0 |
| Set | 1 | N | - | - | - | 0 | N |
| up | 0 | - | ↑ | 0 | N | 0 | CNT + N |
| down | 0 | - | 0 | ↑ | N | 0 | CNT - N |
