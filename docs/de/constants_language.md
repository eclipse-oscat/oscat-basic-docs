<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Diese Struktur definiert verschiedene Sprachen als String Konstanten. Die Variable  LANGUAGE der Globalen Variablenliste stellt diese in der Bibliothek zur Verfügung.

*.DEFAULT : INT := 1 definiert die default Sprache (1=English, 2=Deutsch, 3= Französisch) Die Default Sprache wird immer dann verwendet wenn die Sprache 0 aufgerufen wird. Ist die Spracheinstellung > 0 so wird die entsprechende Sprache gewählt. Spracheinstellung: 0 (es wird die unter DEFAULT spezifizierte Sprache verwendet)	(1 = Englisch, 2 = Deutsch 3 = Französisch) weitere Sprachen werden definiert indem die Struktur CONSTANTS_LANGUAGE erweitert wird. *.LMAX : INT := 3 	gibt an wie viele Sprachen zur Verfügung stehen *.WEEKDAYS : ARRAY[1..3, 1..7] OF STRING(10) := 'Monday','Tuesday', 'Wednesday','Thursday','Friday','Saturday','Sunday','Montag', 'Dienstag','Mittwoch','Donnerstag','Freitag','Samstag','Sonntag'; *.WEEKDAYS2 : ARRAY[1..3, 1..7] OF STRING(2) := 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su', 'Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'; *.MONTHS : ARRAY[1..3, 1..12] OF STRING(10) := 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 	'November', 'December', 'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'; *.MONTHS3 : ARRAY[1..3, 1..12] OF STRING(3) := 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec', 'Jan','Feb','Mrz','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez'; *.DIRS : ARRAY[1..3,0..15] OF STRING(3) :=	'N','NNE','NE','ENE','E', 'ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW' 'N','NNO','NO','ONO','O','OSO','SO','SSO','S','SSW','SW','WSW', 'W','WNW','NW','NNW';
