<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : INT

| | |
|:---|:---|
| **Input	WDAY** | STRING(20) (Eingabestring) |
| **LANG** | INT (Sprachauswahl) |
| **Output** | INT (Wochentag) |
| | FSTRING_TO_WEEKDAY dekodiert einen Wochentag in der Form 'MO' in einen Integer, 1 = MO...7= So. Für die Auswertung werden die ersten beiden Buchstaben der Zeichenkette WDAY ausgewertet, alle folgenden werden ignoriert. Falls die Zeichenkette Leerzeichen enthält werden diese entfernt. Die Wochentage können sowohl in Groß- oder Klein- Schreibung vorliegen. Da die Funktion nur die ersten beiden Zeichen auswertet, können die Wochentage auch in ausgeschriebener Form (Montag) vorliegen. |
| | Mo = 1; Di, Tu = 2; We, Mi = 3; Th, Do = 4; Fr = 5; Sa = 6; So, Su = 7 |
| | Als alternative Form kann der Wochentag auch als Zahl 1..7 angegeben werden. LANG spezifiziert die zu verwendende Sprache, 1= Englisch, 2= Deutsch, 0= die im Setup definierte Default Sprache. |

![fstring_to_weekday](fstring_to_weekday.gif)
