<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : BOOL

| | |
|:---|:---|
| **Input	X, Y** | REAL (Eingangswerte) |
| **N** | INT (Anzahl der Stellen die verglichen werden sollen) |
| **Output** | BOOL (Ergebnis) |
| | CMP vergleicht 2 REAL Werte ob die ersten N Stellen gleich Sind. |

![cmp](cmp.gif)

**Beispiel:**

Beispiele: CMP(3.140,3.149,3) = TRUE	CMP(3.140,3.149,4) = FALSE CMP(0.015,0,016,1) = TRUE	CMP(0.015,0,016,2) = FALSE Bei der Funktion CMP ist zu beachten das durch die Duale Kodierung der Zahlen eine 0.1 im Dezimalsystem nicht unbedingt immer als 0.1 im Binärsystem dargestellt werden kann. Vielmehr kann es vorkommen das die 0.1 etwas kleiner oder größer dargestellt wird weil die Auflösung der Zahlencodierung im Binärsystem nicht exakt eine 0.1 zulässt. Aus diesem Grund kann die Funktion nicht immer zu 100% einen Unterschied von 1 an der letzten Stelle erkennen. Weiterhin ist zu beachten das ein Datentyp REAL mit 32 Bit nur eine Auflösung von 7 - 8 Dezimalstellen bietet.
