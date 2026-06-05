<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : REAL

| | |
|:---|:---|
| **Input	X** | REAL (Eingangswert) |
| **Output** | REAL (Nachkommateil von X) |
| | Die Funktion FRACT liefert den Nachkommateil von X. |

![fract](fract.gif)

**Beispiel:**

Beispiel:	FRACT(3.14) ergibt 0.14. Für X größer oder kleiner als +/- 2.14 * 10^9 liefert FRACT stets ein Null zurück. Das die Auflösung eines 32Bit REAL maximal bei 8 Dezimalstellen liegt kann aus Zahlen größer oder kleiner als +/- 2.14 * 10^9 kein Nachkommateil ermittelt werden, weil dieser auch in einer REAL Variable nicht abgespeichert werden kann.
