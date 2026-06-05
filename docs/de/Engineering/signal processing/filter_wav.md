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
| **Input	X** | DWORD (Eingangswert) |
| **W** | ARRAY[0..15] of REAL (Gewichtungsfaktoren) |
| **RST** | BOOL (asynchroner Reset Eingang) |
| **Output	Y** | REAL (gefilterter Wert) |
| | FILTER_WAV ist ein Filter mit gewichtetem Mittelwert. Beim Filter mit gewichteten Mittelwert (auch FIR Filter genannt) werden die einzelnen Werte im Puffer mit unterschiedlicher Gewichtung bewertet. |
| **Y** | = X0 * W0 + X1 * W1 + ….+ X15 * W15 |
| | X0 ist der Wert X im momentanen Zyklus, X1 ist der Wert im Zyklus davor usw. Die Faktoren W werden als Array dem Eingang W übergeben. Bei der Anwendung des FIR Filters ist darauf zu achten, dass geeignete Faktoren für die Gewichtung eingesetzt werden. Die Anwendung macht nur dann Sinn wenn diese Faktoren mit geeigneten Methoden oder Entwurfssoftware ermittelt werden. |

![filter_wav](filter_wav.gif)
