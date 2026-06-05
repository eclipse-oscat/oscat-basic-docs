<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : STRING(2)

| | |
|:---|:---|
| **Input	IN** | BYTE (Zeichen das konvertiert werden soll) |
| **Output** | STRING(2) (konvertiertes Zeichen) |
| | TO_UML wandelt einzelne Sonderzeichen des Zeichensatzes größer 127 in eine Kombination zweier Buchstaben um. Es handelt sich dabei um Zeichen des erweiterten ASCII Zeichensatzes nach ISO 8859-1(Latin1). |
| **Es werden folgende Zeichen umgewandelt** |  |
| **Ä >> Ae** | ä >> ae	Ö >> Oe	ö >> oe	Ü >> Ue	ü >> ue |
| | ß >> ss |
| | Alle andern Zeichen werden als STRING mit dem Zeichen IN zurückgegeben. |

![to_uml](to_uml.gif)
