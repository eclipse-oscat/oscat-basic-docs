<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## ROUND

| | |
|:---|:---|
| **Type	Funktion** | REAL |
| **Input	IN** | REAL (Eingangswert) |
| **N** | Integer (Anzahl der Nachkommastellen) |
| **Output** | REAL (Gerundeter Wert) |
| | Die Funktion ROUND rundet den Eingangswert in auf N Nachkommastellen. Folgt der letzten Stelle ein Digit größer 5 wird die letzte Stelle aufgerundet. ROUND nutzt intern die Standard Funktion TRUNC() welche den Eingangswert in einen INTEGER vom Typ DINT wandelt. Hierbei kann es zu einem Überlauf kommen weil DINT maximal +/- 2.14 * 10^9 speichern kann. Der Wertebereich von ROUND ist deshalb auf +/- 2.14 * 10^9 begrenzt. |

![round](round.gif)

**Beispiel:**

Beispiel:	ROUND(3.555, 2) = 3.56
