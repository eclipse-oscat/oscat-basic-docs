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
| **Input	STR** | STRING (Eingabe STRING) |
| **POS** | INT (Startposition) |
| **Output** | INT (Position des ersten Zeichens das kein Steuerzeichen ist) |
| | FIND_CHAR durchsucht die Zeichenkette STR ab der Position POS und gibt die Position zurück an der das erste Zeichen steht das kein Steuerzeichen ist. Steuerzeichen sind alle Zeichen deren Wert kleiner 32 oder 127 ist. Bei der Prüfung wird die Globale Setup Konstante EXTENDED_ASCII berücksichtigt. Wenn EXTENDED_ASCII = TRUE ist werden Zeichen des erweiterten ASCII Zeichensatzes nach ISO 8859-1 berücksichtigt. Umlaute wie Ä,Ö,Ü werden nur dann berücksichtigt wenn die Globale Konstante  EXTENDED_ASCII = TRUE ist. Wenn EXTENDED_ASCII = FALSE ist werden Zeichen des erweiterten Zeichensatzes mit einem Wert > 127 als Steuerzeichen interpretiert. |

![find_char](find_char.gif)
