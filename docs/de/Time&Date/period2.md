<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## PERIOD2

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	DP** | ARRAY[0..3,0..1] of DATE (Perioden) |
| **DX** | DATE (zu testendes Datum) |
| **Output** | BOOL (TRUE wenn DX innerhalb einer der Perioden liegt) |
| | PERIOD2 prüft ob das Datum DX innerhalb einer von 4 spezifizierten Perioden liegt. Die Perioden werden in einem ARRAY[0..3,0..1] of DATE spezifiziert. Im Gegensatz zur Funktion PERIOD prüft PERIOD2 auch das Jahr. Die Perioden werden im ARRAY DP spezifiziert, wobei DP[N,0] das Anfangsdatum der Periode N DP[N,1] das Enddatum der Periode N ist. |
| **Die Funktion Prüft nach der Formel** | DX >= DP[N,0] AND DX <= DP[N,1]. Es wird Dabei jeweils N=0 bis 3 geprüft. Wenn DX in eine der 4 Perioden fällt wird der Ausgang auf TRUE gesetzt. |
| | Die einzelnen Perioden Müssen nicht sortiert vorliegen. PERIOD2 kann benutzt werden um Ferien oder Urlaubszeiten zu definieren. PERIOD2 prüft nicht wiederkehrende Perioden, wobei die Funktion PERIOD jährlich wiederkehrende Perioden Prüft. |

![period2](period2.gif)
