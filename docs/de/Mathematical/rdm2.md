<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## RDM2

| | |
|:---|:---|
| **Type	Funktion** | INT |
| **Input	LAST** | INT (Letzter berechneter Wert) |
| **LOW** | INT (niedrigster generierter Wert) |
| **HIGH** | INT (höchster generierter Wert) |
| **Output** | INT (Zufallszahl zwischen LOW und HIGH) |
| | RDM2 erzeugt einen Integer Random Wert im Bereich von LOW bis HIGH, wobei LOW und HIGH im Wertebereich enthalten sind. Wird die Funktion nur einmal je Zyklus benutzt kann der Eingangswert LAST auf 0 bleiben. Die Funktion RDM2 benutzt die SPS interne Zeitbasis zur Erzeugung der Zufallszahl. Da RDM2 eine als LAST einen Integer benutzt welcher das letzte Ergebnis zwischen LOW und HIGH darstellt kann es zu einer Situation führen die darin resultiert das RDM2 innerhalb eines Zyklus solange sicher SPS Timer nicht verändert immer das gleiche Ergebnis liefert. Dies passiert immer dann wenn zufällig das Ergebnis auch dem Startwert entspricht. Da dann derselbe Startwert wieder verwendet wird wird innerhalb des gleichen Zyklus auch wieder das gleiche Ergebnis Zustande kommen. Dieser Fall tritt umso öfter auf je kleiner der durch LOW und HIGH bestimmte Bereich für das Ergebnis ist. Man kann diesen Effekt leicht umgehen indem man als Startwert einen Schleifenzähler verwendet der definitiv bei jedem Aufruf einen neuen Wert aufweist, oder noch besser einen Schleifenzähler addiert mit dem letzten Ergebnis als Startwert verwendet. |

![rdm2](rdm2.gif)
