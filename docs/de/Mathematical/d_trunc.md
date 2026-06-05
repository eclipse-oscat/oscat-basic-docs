<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : DINT

| | |
|:---|:---|
| **Input	X** | REAL (Eingangswert) |
| **Output** | DINT (Ausgangswert) |
| | D_TRUNC liefert den ganzzahligen Teil eines REAL Wertes als DINT. Die IEC Routine TRUNC() unterstützt nicht auf allen Systemen ein TRUNC nach DINT so dass wir aus Gründen der Kompatibilität diese Routine nachgebildet haben. Leider liefert auch ein REAL_TO_DINT nicht auf allen Systemen dasselbe Ergebnis. D_TRUNC prüft welches Ergebnis die IEC Funktionen liefern und nutzt die passende Funktion um ein brauchbares Ergebnis zu liefern. |
| | D_TRUNC(1.6) = 1 |
| | D_TRUNC(-1.6) = -1 |

![d_trunc](d_trunc.gif)
