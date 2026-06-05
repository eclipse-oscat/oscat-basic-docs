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
| **Input	LOW** | REAL (unterer Grenzwert) |
| **IN** | REAL (Eingangswert) |
| **HIGH** | REAL (oberer Grenzwert) |
| **Output** | BOOL (TRUE, wenn in <= HIGH und in >= LOW) |
| | Die Funktion WINDOW2 testet, ob der Eingangswert IN <= HIGH und IN >= LOW ist. Im Gegensatz zur Funktion WINDOW die TRUE liefert wenn IN innerhalb der Grenzen LOW und HIGH liegt liefert WINDOW2 FALSE wenn IN außerhalb der Grenzen  LOW und HIGH liegt. |

![window2](window2.gif)
