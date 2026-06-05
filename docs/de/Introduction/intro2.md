<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Gleitpunktzahlen werden im Format REAL abgespeichert. Ein gängiges Datenformat nach IEC754 benutzt dazu ein 24Bit breite Mantisse und einen 8Bit Exponenten. Daraus resultiert eine Genauigkeit von 7-8 Dezimalstellen. Normalerweise ist dies für Anwendungen in der Steuerungstechnik mehr als Ausreichend, kann aber in bestimmten Fällen zu einem Problem führen. Ein Typischer Fall der mit einfacher Genauigkeit nur unzureichend gelöst werden kann sind Verbrauchsmesser. Möchte man bis zu Mehreren Mwh (Megawattstunden) an Gesamtverbrauch Aufsummieren und dabei eine kleinste Leistung von 1mW (Milliwatt) im Abstand von 10ms Messen und berücksichtigen, so benötigt man eine Auflösung von 3.6 * 10^7 (entspricht 10MWs) und dabei würde man 1 * 10^-5 Ws aufaddieren wollen. Um dies zu bewerkstelligen benötigt man eine Auflösung von 12 Stellen.

Die von OSCAT implementierte Doppelte REAL Genauigkeit hat eine Auflösung von etwa 15 Stellen. Der hierfür Implementierte Datentyp [REAL2](Data Types/real2.md) besteht aus R1 und RX, hierbei wird in RX der Wert mir den ersten 7-8 Stellen als Real gespeichert und der Rest in einem Weiteren REAL R1. Dieser Datentyp hat den Vorteil das keine Wandlung von [REAL2](Data Types/real2.md) zu REAL notwendig, ist, vielmehr ist der Teil RX bereits der einfache REAL Wert.
