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
| **Input	N** | INT (Clock Teiler) |
| **Output	Q** | BOOL (Taktausgang) |
| | CLK_N erzeugt einen Impuls alle X Millisekunden basierend auf der SPS internen 1ms Referenz. Die Impulse sind exakt einen SPS Zyklus lang und werden alle 2^N Millisekunden erzeugt. |
| | Die Periodendauer beträgt 1ms für N=0, 2ms für N=1, 4ms für N=2 usw. |
| | CLK_N ersetzt die Bausteine CLK_1ms, CLK_2ms, CLK_4ms und CLK_8ms aus älteren Bibliotheken. |
| **Das nachfolgende Bild zeigt das Ausgangssignal für N=0** |  |

![clk_n](clk_n.gif)

![clk_n_trace](clk_n_trace.gif)
