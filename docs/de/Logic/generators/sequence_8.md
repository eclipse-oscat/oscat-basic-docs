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
| **Input	IN0..7** | BOOL (Freigabesignal für Q0..7) |
| **START** | BOOL (Startflanke für den Sequenzer) |
| **RST** | BOOL (Asynchroner Reset Eingang) |
| **WAIT 0..7** | TIME (Wartezeit für das Eingangssignal an IN 0..7) |
| **DELAY 0..7** | TIME (Verzögerungszeit, bis das Eingangssignal 	IN0..7 geprüft wird) |
| **Output	Q 0..7** | BOOL (Steuerausgänge) |
| **QX** | BOOL (TRUE, wenn einer der Ausgänge Q0 .. Q7 aktiv ist) |
| **RUN** | BOOL (RUN ist TRUE, wenn der Sequenzer läuft) |
| **STEP** | INT (gibt den momentanen Schritt an) |
| **STATUS** | BYTE (0 wenn kein Fehler vorliegt, sonst > 0) |
| | Eine Funktionsbeschreibung von SEQUENCE_8 ist unter SEQUENCE_4 zu finden. SEQUENCE_8 ist Funktionsidentisch mit SEQUENCE_4. Er hat 8 anstelle von 4 Kanälen.  SEQUENCE_8 findet Anwendung in der OSCAT Bibliothek im Modul LEGIONELLA. |

![sequence_8](sequence_8.gif)
