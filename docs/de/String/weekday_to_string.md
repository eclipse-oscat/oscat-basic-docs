<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : STRING(10)

| | |
|:---|:---|
| **Input	WDAY** | INT (Wochentag 1..7) |
| **LANG** | INT (Sprachauswahl 0 = Default) |
| **LX** | INT (Länge der Zeichenkette) |
| **Output** | STRING(10) (Ausgangswert) |
| **WEEKDAY_TO_STRING wandelt einen Wochentag in die entsprechende Zeichenkette. Der Eingang WDAY gibt den entsprechenden Wochentag an** | 1 = Montag und 7 = Sonntag. Der Eingang LANG wählt die gewünschte Sprache aus: 1 = Englisch und 2 = Deutsch. LANG = 0 benutzt die als Default Sprache in der Globalen Setup Variable LANGUAGE_DEFAULT festgelegte Sprache. Der Eingang LX legt die Länge der zu erzeugenden Zeichenkette fest: 0 = Voller Monatsname, 2 = Abkürzung mit 2 Buchstaben, alle anderen Werte am Eingang LX sind nicht definiert. |
| | Die vom Baustein erzeugten Zeichenketten sowie die unterstützten Sprachen sind im Bereich Global Constants definiert und können dort erweitert und verändert werden. |
| | WEEKDAY_TO_STRING(1,0,0) = 'Monday' |
| | abhängig von der Globalen Konstante LANGUAGE_DEFAULT |
| | WEEKDAY_TO_STRING(1,2,0) = 'Montag' |
| | WEEKDAY_TO_STRING(1,0,2) = 'Mo' |

![weekday_to_string](weekday_to_string.gif)
