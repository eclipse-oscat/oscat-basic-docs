<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## REPLACE_UML

| | |
|:---|:---|
| **Type	Funktion** | STRING |
| **Input	STR** | STRING (Eingangsstring) |
| **Output** | STRING (Ausgangsstring) |
| | REPLACE_UML ersetzt Umlaute mit einer Kombination aus 2 Zeichen so dass das Ergebnis keine Umlaute mehr enthält. Die Groß und Kleinschreibung wird dabei beachtet. Wenn ein Wort nur aus Großbuchstaben besteht und darin ein Umlaut enthalten ist wird dieser mit einem Großbuchstaben gefolgt von einem Kleinbuchstaben ersetzt, im Falle eines ß welches keine Großschreibung kennt wird es immer mit zwei Kleinbuchstaben ersetzt. Wird die Funktion REPLACE_UML auf ein Wort das nur aus Großbuchstaben besteht angewendet muss anschließend mit der Funktion UPPERCASE() sichergestellt werden dass die Kleinbuchstaben wieder in Großbuchstaben gewandelt werden. |
| | Ä > Ae, Ö > Oe, Ü > Ue, ä > ae, ö > oe, ü > oe, ß > ss. |

![replace_uml](replace_uml.gif)
