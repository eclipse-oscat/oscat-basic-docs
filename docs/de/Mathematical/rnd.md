<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## RND

| | |
|:---|:---|
| **Type	Funktion** | REAL |
| **Input	X** | REAL (Eingangswert) |
| **N** | Integer (Anzahl der Stellen) |
| **Output** | REAL (Gerundeter Wert) |
| | Die Funktion RND rundet den Eingangswert IN auf N Stellen. Folgt der letzten Stelle eine Stelle größer 5 wird die letzte Stelle aufgerundet. RND nutzt intern die Standard Funktion TRUNC() welche den Eingangswert in einen INTEGER vom Typ DINT wandelt. Hierbei kann es zu einem Überlauf kommen weil DINT maximal +/- 2.14 * 10^9 speichern kann. Der Wertebereich von RND ist deshalb auf +/- 2.14 * 10^9 begrenzt. Siehe hierzu auch die Funktion ROUND welche den Eingangswert auf N Nachkommastellen rundet. |

![rnd](rnd.gif)

**Beispiel:**

```iecst
RND(355.55, 2) = 360 RND(3.555, 2) = 3.6 ROUND(3.555, 2) = 3.56
```
