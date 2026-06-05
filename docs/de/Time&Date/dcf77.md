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
| **Input	REC** | BOOL (Eingang für den DCF77 Empfänger) |
| **SET** | BOOL (Asynchroner SET Eingang) |
| **[SDT](../Data Types/sdt.md)** | DT (Anfangswert für RTC) |
| **DSI** | BOOL (Sommerzeit Eingang) |
| **Output	TP** | BOOL (Puls zum Setzen von nachgeschalteten Uhren) |
| **DS** | BOOL (TRUE, wenn Sommerzeit herrscht) |
| **WDAY** | INT (Wochentag) |
| **ERROR** | BOOL (TRUE, wenn REC kein Signal liefert) |
| **RTC** | DT (Synchronisierte Weltzeit UTC) |
| **RTC1** | DT (Synchronisierte Lokalzeit) |
| **MSEC** | INT (Millisekunden von RTC und RTC1) |
| **SYNC** | BOOL (TRUE, wenn RTC mit DCF synchron ist) |
| **Setup	SYNC_TIMEOUT** | TIME (Default = T#2m) |
| **TIME_OFFSET** | INT (Zeit Offset für RTC1, Default = 1 Stunde) |
| **DST_EN** | BOOL (Sommerzeit für RTC1, Default = TRUE) |
| | Die Funktion DCF77 dekodiert das Serielle Signal eines DCF77 Empfängers und steuert 2 interne Uhren RTC und RTC1, oder über den Ausgang TP auch externe (nachgeschaltete) Uhren. Ein Ausgang DS wird TRUE, wenn Sommerzeit herrscht. Der Ausgang WDAY gibt den Wochentag an (1 = Montag). Der Ausgang ERROR wird TRUE, wenn kein gültiges Signal Empfangen wird. Die Internen Uhren laufen aber trotzdem weiter, wenn Sie bereits synchronisiert sind. Ein  weiterer Ausgang SYNC zeigt an dass die internen Uhren mit DCF77 synchronisiert sind und wird FALSE, wenn sie länger als durch die Setup-Variable SYNC_TIMEOUT festgelegte Zeit nicht mehr synchronisiert wurden. Die internen Uhren laufen in jedem Fall mit der Genauigkeit des SPS-Timers weiter. Durch einen Doppelklick auf das Symbol im CFC Editor können weitere Setup-Variablem definiert werden. Hierbei legt SYNC_TIMEOUT fest, nach welcher Zeit das Ausgangssignal SYNC, FALSE wird, wenn die internen Uhren RTC und RTC1 nicht mehr durch DCF77 synchronisiert wurden. Die Variable TIME_OFFSET legt die Zeitdifferenz der Lokalzeit (RTC1) von der UTC fest. Default ist 1 Stunde für MEZ (Mitteleuropäische Zeit). Die Variable TIME_OFFSET ist vom Typ INTEGER damit auch Zeitzonen mit negativem Offset (Westlich von Greenwich) möglich sind. |
| | Durch DST_EN wird festgelegt, ob RTC1 automatisch auf Sommerzeit schalten soll oder nicht. Der Ausgang MSEC erweitert die auf RTC und RTC1 zur Verfügung gestellte Zeit um Millisekunden. Der Eingang [SDT](../Data Types/sdt.md) dient dazu die internen Uhren RTC und RTC1 auf einen definierten Anfangswert zu setzen damit sofort nach den Start eine gültige Uhrzeit zur Verfügung steht. Während des ersten Zyklus wird Datum und Zeit von [SDT](../Data Types/sdt.md) nach RTC kopiert, und läuft ab dem ersten Zyklus. Falls nötig kann mit den asynchronen Setz Eingang SET die interne UHR jederzeit neu gestellt werden. Sie wird aber nach einem Zyklus wieder von einem Gültigen DCF77 Signal überschrieben, ausser der Eingang SET bleibt auf TRUE. Sobald ein gültiges DCF77 Signal dekodiert wurde wird RTC und RTC1 auf die entsprechende genauere DCF77 Zeit synchronisiert. Am Eingang [SDT](../Data Types/sdt.md) kann zum Beispiel die Uhrzeit aus der in der SPS enthaltenen Hardware Uhr verwendet werden, es muss aber sichergestellt werden das DCF77 erst dann aufgerufen wird wenn bereits eine gültige Uhrzeit an [SDT](../Data Types/sdt.md) anliegt, den DCF77 liest diesen Wert nur ein einziges mal im ersten Zyklus ein, oder immer dann wenn der Eingang SET auf TRUE steht. |

![dcf77](dcf77.gif)
