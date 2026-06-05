<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## REAL_TO_FRAC

| | |
|:---|:---|
| **Type	Funktion** | FRACTION |
| **Input	X** | REAL (Eingangswert) |
| **N** | INT (maximalwert des Nenners) |
| **Output** | FRACTION (Ausgangswert) |
| | REAL_TO_FRAC konvertiert eine Gleitpunktzahl (REAL) in einen Bruch. Die Funktion liefert den Datentyp FRACTION der aus einer Struktur mit 2 Werten besteht. Mit dem Eingang X kann die maximale Größe des Zählers vorgegeben werden. |
| **Datentyp FRACTION** |  |
| ***.NUMERATOR** | INT	(Zähler des Bruches) |
| ***.DENOMINATOR** | INT	(Nenner des Bruches) |

![real_to_frac](real_to_frac.gif)

**Beispiel:**

Beispiel: REAL_TO_FRAC(3.1415926, 1000) ergibt 355 / 113. 355 / 133 ergibt die beste Approximation für Nenner < 1000.
