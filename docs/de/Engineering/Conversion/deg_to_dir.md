<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : STRING(3)

| | |
|:---|:---|
| **Input	DEG** | INT (Himmelsrichtung in Grad) |
| **N** | INT (Maximale Länge der Zeichenkette) |
| **L** | INT (Spracheinstellung: siehe Sprachdefnitionen) |
| **Output** | STRING(3) (Kompassangaben) |
| **DEG_TO_DIR rechnet eine Himmelsrichtung (0..360 Grad) in Kompass Angaben um. Am Eingang DEG liegt die Himmelsrichtung in Grad an (0 = Nord, 90 = Ost, 180 = Süd und 270 = Westen ). Der Ausgang stellt die Himmelsrichtung als String in der Form NNO zur Verfügung. Mit dem Eingang N wird die Maximale Länge der Richtungsangabe begrenzt. Wenn N=1 werden nur in die 4 Himmelsrichtungen N, E, S, W aufgelöst. Ist N = 2 wird zwischen jede Himmelsrichtung eine weitere eingefügt** | NE, SE, SW, NW. Bei N=3 werden auch Richtungen wie NNO ... aufgelöst, Mit N = 3 werden insgesamt 16 Richtungen Ausgewertet. Der Eingang L erlaubt das Umschalten der im Sprachen Setup definierten Sprachen. 0L=0 bedeutet Default Sprache, eine Zahl > 0 ist eine der Vordefinierten Sprachen. nähere Infos zu den Vordefinierten Sprachen finden sie unter Datentypen [CONSTANTS_LANGUAGE](../../Data Types/constants_language.md). |

![deg_to_dir](deg_to_dir.gif)
