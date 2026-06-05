<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MODR

| | |
|:---|:---|
| **Type	Funktion** | REAL |
| **Input	IN** | REAL (Dividend) |
| **DIVI** | REAL (Divisor) |
| **Output** | REAL (Rest der Division) |
| | Die Funktion MODR liefert den Rest einer Division analog der Standardfunktion MOD, allerdings für REAL-Zahlen. MODR nutzt intern das Datenformat vom Typ DINT. Hierbei kann es zu einem Überlauf kommen weil DINT maximal +/- 2.14 * 10^9 speichern kann. Der Wertebereich von MODR ist deshalb auf +/- 2.14 * 10^9 begrenzt. Für DIVI = 0 liefert die Funktion 0 zurück. |
| | MODR(A, M) = A - M * FLOOR2(A / M). |

![modr](modr.gif)

**Beispiel:**

Beispiel:	MODR(5.5, 2.5) ergibt 0.5.
