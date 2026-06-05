<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktionsbaustein

| | |
|:---|:---|
| **Input	M** | REAL (Entfernung in Meter) |
| **AE** | REAL (Entfernung in Astronomischen Einheiten) |
| **PC** | REAL (Entfernung in Parsec) |
| **LJ** | REAL (Entfernung in Lichtjahren) |
| **Output	YM** | REAL (Entfernung in Meter) |
| **YAE** | REAL (Entfernung in Astronomischen Einheiten) |
| **YPC** | REAL (Entfernung in Parsec) |
| **YLJ** | REAL (Entfernung in Lichtjahren) |
| | Der Baustein ASTROrechnet verschiedene in der Astronomie gebräuchliche Entfernungseinheiten um. Normalerweise wird nur der zu konvertierende Eingang belegt und die restlichen Eingänge bleiben frei. Werden jedoch mehrere Eingänge gleichzeitig mit Werten beaufschlagt, so werden die Werte aller Eingänge entsprechend umgewandelt und dann aufsummiert. |
| | 1 AE = 149,597870 * 109 m |
| | 1 PC = 206265 AE |
| | 1 LJ = 9,460530 * 1015 m = 63240 AE = 0,30659 PC |

![astro](astro.gif)
