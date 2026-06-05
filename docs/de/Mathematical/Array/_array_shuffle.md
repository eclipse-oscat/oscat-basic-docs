<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## _ARRAY_SHUFFLE

| | |
|:---|:---|
| **Type	Funktion** | BOOL |
| **Input	PT** | Pointer (Zeiger auf das Array) |
| **SIZE** | UINT (Größe des Arrays) |
| **Output** | BOOL (ergibt TRUE) |
| **Die Funktion _ARRAY_SHUFFLE vertauscht die Elemente eines beliebigen Arrays of REAL nach einem Zufallsprinzip. Beim Aufruf wird der Funktion ein Pointer auf das Array und dessen Größe in Bytes übergeben. Unter CoDeSys lautet der Aufruf** | _ARRAY_SHUFFLE(ADR(Array), SIZEOF(Array)), wobei Array der Name des zu manipulierenden Arrays ist. ADR() ist eine Standardfunktion, die den Pointer auf das Array ermittelt und SIZEOF() ist eine Standardfunktion, die die Größe des Arrays ermittelt. Das durch den Pointer referenzierte Array wird direkt im Speicher manipuliert und steht nach beenden der Funktion direkt zur Verfügung. Die Funktion _ARRAY_SHUFFLE verändert also den Inhalt des Arrays. |
| | Diese Art der Bearbeitung von Arrays ist äußerst effizient, da kein zusätzlicher Speicher benötigt wird und keine Übergabewerte kopiert werden müssen. |
| | Sollte ein Array bearbeitet werden, das nicht verändert werden darf, so ist es vor Übergabe des Pointer und Aufruf der Funktion in ein temporäres Array zu kopieren. |

![array_shuffle](array_shuffle.gif)

**Beispiel:**

Beispiel:	_ARRAY_SHUFFLE(ADR(bigarray), SIZEOF(bigarray)) Ein Aufruf der Funktion _ARRAY_SHUFFLE könnte ein Array wie folgt verändern. Da die Funktion einen PseudoRandom Algorithmus verwendet wird das Ergebnis bei jedem Aufruf ein anderes sein, die Ergebnisse sind nicht reproduzierbar, auch nicht durch einen Neustart des Programms oder der Steuerung. Ausgangsarray: 	(0,1,2,3,4,5,6,7,8,9) Ergebnis:	(5,0,3,9,7,2,1,8,4,6) Das Ergebnis ist aber nicht wiederholbar, die Funktion liefert nach jedem Aufruf oder Auch Neustart eine neue Reihenfolge.
