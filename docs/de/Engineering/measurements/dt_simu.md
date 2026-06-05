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
| **Input	START** | DT (Anfangs DATETIME) |
| **SPEED** | REAL (Geschwindigkeit für den Ausgang DTS) |
| **Output	DTS** | DT (Simulierte DATETIME) |
| | DT_SIMU simuliert am Ausgang DTS einen Zeit Datumswert der mit dem Anfangswert START beginnt und mit der Geschwindigkeit SPEED weiter läuft. Wird der Eingangswert SPEED nicht belegt arbeitet der Baustein mit dem internen Vorgabewert 1.0 und der Ausgang DTS läuft mit 1 Sekunde / Sekunde vorwärts. Mit dem Eingang SPEED kann am Ausgang DTS eine beliebig schnelle oder langsame Uhr simuliert werden. Der Baustein kann in der Simulationsumgebung eingesetzt werden um eine RTC zu simulieren und zusätzlich die Geschwindigkeit der RTC zum Testen angepasst werden. Wird der Eingang SPEED = 0 gesetzt, so wird der Ausgang DTS bei jedem SPS Zyklus um eine Sekunde weitergestellt. |

![dt_simu](dt_simu.gif)
