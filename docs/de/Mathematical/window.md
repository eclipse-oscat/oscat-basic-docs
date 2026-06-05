<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## WINDOW

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	LOW** | REAL (unterer Grenzwert) |
| **IN** | REAL (Eingangswert) |
| **HIGH** | REAL (oberer Grenzwert) |
| **Output** | BOOL (TRUE, wenn in < HIGH und in > LOW) |
| | Die Funktion WINDOW testet, ob der Eingangswert IN innerhalb der Grenzen, die durch LOW und HIGH definiert sind, liegt. |
| | WINDOW ist genau dann TRUE, wenn IN < HIGH und IN > LOW ist. |

![window](window.gif)
