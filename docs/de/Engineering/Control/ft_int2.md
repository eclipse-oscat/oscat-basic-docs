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
| **Input	IN** | REAL (Eingangssignal) |
| **K** | REAL (Multiplikator) |
| **RUN** | BOOL (Freigabe Eingang) |
| **RST** | BOOL (Reset Eingang) |
| **OUT_MIN** | REAL (unteres Ausgangs Limit) |
| **OUT_MAX** | REAL (oberes Ausgangs Limit) |
| **Output	OUT** | REAL (Ausgangssignal) |
| **LIM** | BOOL (TRUE wenn der Ausgang an einem Limit steht) |
| | FT_INT2 ist ein Integratorbaustein der intern mit doppelter Genauigkeit rechnet und eine Auflösung von 14 Dezimalstellen sicherstellt. Dies macht FT_INT2 im Gegensatz zu FT_INT für z.B. Verbrauchszähler und ähnliche Anwendungen geeignet. |

![ft_int2](ft_int2.gif)

**Beispiel:**

Beispiel: ein Eingangssignal von 0,0001 bei einer Abtastzeit von 1 Millisekunde und einem Ausgangswert von 100000 ergibt einen Wert von 0,0001 * 0,001 Sekunden = 0,000001 der zum Ausgangswert von 100000 addiert werden soll, was unweigerlich wieder den Wert von 100000 ergibt, denn die Auflösung des Datentyps Real kann nur maximal 8 Stellen erfassen. FT_INT2 löst dieses Problem indem er intern mit doppelter Genauigkeit (14 Dezimalstellen) rechnet und addiert auch kleinste Eingangswerte auf so dass keine Informationen verloren gehen.
