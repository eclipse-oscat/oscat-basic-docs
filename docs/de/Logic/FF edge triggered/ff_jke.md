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
| **Input	SET** | BOOL (asynchroner Set) |
| **J** | BOOL (Takt-synchroner Set) |
| **CLK** | BOOL (Takteingang) |
| **K** | BOOL (Takt-synchroner Reset) |
| **RST** | BOOL (asynchroner Reset) |
| **Output	Q** | BOOL (Ausgang) |
| | FF_JKE ist ein flankengetriggertes JK-Flop-Flop mit asynchronen Set und Reset Eingängen. Das JK-Flip-Flop setzt den Ausgang Q, wenn bei einer steigenden Flanke von CLK der Input J TRUE ist. Q wird FALSE, wenn bei einer steigenden Taktflanke der Eingang K TRUE ist. Sind die beiden Eingänge J und K bei einer Steigenden Taktflanke TRUE, so wird der Ausgang negiert. Er schaltet bei jedem Takt das Ausgangssignal um. |
| | DCLKRSTQSET |

![ff_jke](ff_jke.gif)
