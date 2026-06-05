<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## LINEAR_INT

| | |
|:---|:---|
| **Type** | Funktion |
| **Input	X** | REAL (Eingangssignal) |
| **XY** | ARRAY[1..20,0..1] (Aufsteigend sortierte Wertepaare) |
| **PTS** | INT (Anzahl der Wertepaare) |
| **Output** | REAL (Ausgangssignal) |
| | LINEAR_INT ist ein linearer Interpolations Baustein. Eine beliebige Kennlinie wird mit maximal 20 Koordinatenwerten (X,Y) beschrieben und dadurch in bis zu 19 lineare Segmente zerlegt. Die Definition der Koordinatenwerte wird in einem Array übergeben welches die Kennlinie mit einzelnen X,Y Wertepaaren beschreibt. Die Wertepaare müssen aufsteigend nach dem X_Wert Sortiert sein. Wird ein X-Wert außerhalb des durch die Wertepaare beschriebenen Bereiches abgefragt, so wird das erste beziehungsweise letzte lineare Segment extrapoliert und der entsprechende Wert Ausgegeben. Um die Anzahl der Definitionspunkte flexibel zu halten wird am Eingang PTS die Anzahl der Punkte vorgegeben. Die mögliche Punktezahl liegt im Bereich 3 bis 20, wobei jeder Einzelpunkt mit X- und Y-Wert dargestellt ist. |

![linear_int](linear_int.gif)

**Beispiel:**

Beispiel: VAR BEISPIEL : ARRAY[1..20,0..1] := -10,-0.53, 10,0.53, 100,88.3, 200,122.2; END_VAR für obige Definition ergeben sich folgende Ergebnisse: LINEAR_INT(0, Beispiel, 4) = 0; LINEAR_INT(30.0, Beispiel, 4) = 20.0344; LINEAR_INT(66.41, Beispiel, 4) = 55.54229; LINEAR_INT(800.0, Beispiel, 4) = 325.6;
