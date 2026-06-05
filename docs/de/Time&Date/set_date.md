<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SET_DATE

| | |
|:---|:---|
| **Type	Funktion** | DATE |
| **Input	YEAR** | INT (Jahreszahl) |
| **MONTH** | INT (Monat) |
| **DAY** | INT (Tag) |
| **Output** | DATE (Zusammengesetztes Datum) |
| | Die Funktion SET_DATE berechnet einen Datum (DATE) aus den Eingangswerten Tag, Monat und Jahr. SET_DATE überprüft dabei nicht die Gültigkeit eines Datums. Zum Beispiel darf auch der 30. Februar gesetzt werden was natürlich den 1.3. oder bei einem Schaltjahr dem 2. März ergibt. SET_DATE kann deshalb auch benutzt werden um einen beliebigen Tag im Jahr zu erzeugen. Dies kann eine durchaus Sinnvolle Anwendung sein. In diesem Fall darf der Monat auch 0 betragen. Eine ungültige Monatsangabe ergibt immer ein Datum in Bezug auf den Januar. Ein ungültiger Monat ( Monat < 1 oder Monat > 12) wird immer als Januar interpretiert. |

![set_date](set_date.gif)

**Beispiel:**

Beispiel:	SET_DATE(2007,1,365) = 31.12.2007 Beispiel:	SET_DATE(2007, 1, 22) = 22.1.2007 Der Wertebereich der Funktion Eingänge ist: YEAR {1970 .. 2099} MONTH {1..12} DAY {INT} Wertebereich des Ausgangs: {1.1.1970 .. 31.12.2099}
