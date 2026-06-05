<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : STRING

| | |
|:---|:---|
| **Input	STR** | STRING (Eingabestring) |
| **L** | INT (feste Länge des Ausgabestrings) |
| **C** | BYTE (Füllzeichen beim Auffüllen) |
| **M** | INT (Mode zum Auffüllen) |
| **Output** | STRING (Zeichenkette mit fester Länge N) |
| | FIX erzeugt eine Zeichenkette mit fester Länge N. Die Zeichenkette STR am Eingang wird auf die Länge N abgeschnitten beziehungsweise mit dem Füllzeichen C aufgefüllt. Wenn die Zeichenkette STR kürzer ist als die zu erzeugende Länge L wird abhängig von M die Zeichenkette mit dem Füllzeichen C aufgefüllt. Wenn M = 0 werden die Füllzeichen am Ende der Zeichenkette angehängt, ist M = 1 werden die Füllzeichen am Anfang angehängt, und wenn M = 2 wird die Zeichenkette zwischen Füllzeichen zentriert. Falls die Anzahl der nötigen Füllzeichen ungerade ist wird bei M = 2 am Ende ein Füllzeichen mehr als am Anfang angehängt. Die Funktion FIX wertet auch die Globale Setup Konstante STRING_LENGTH aus und begrenzt die maximale Länge L der Zeichenkette auf STRING_LENGTH. |

![fix](fix.gif)
