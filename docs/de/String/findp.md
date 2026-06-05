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
| **Input	STR** | STRING (Eingabestring) |
| **SRC** | STRING (Suchstring) |
| **POS** | INT (Position ab der gesucht wird) |
| **Output** | INT (Position des ersten Buchstabens des gefundenen Strings) |
| | FINDP sucht in einer Zeichenkette STR ab der Position POS nach einer Zeichenkette SRC. Wird die Zeichenkette SRC gefunden so wird die Position des ersten Zeichens von SRC innerhalb von STR ausgegeben. Wird die Zeichenkette ab der Position POS nicht gefunden wird eine 0 ausgegeben. Wird eine Leere Zeichenkette als Suchstring vorgegeben liefert der Baustein das Ergebnis 0. |

![findp](findp.gif)

**Beispiel:**

Beispiel: 	FINDP('ein Fuchs ist ein Tier','ein',1) = 1; FINDP('ein Fuchs ist ein Tier','ein',2) = 15; FINDP('ein Fuchs ist ein Tier','ein',16) = 0;
