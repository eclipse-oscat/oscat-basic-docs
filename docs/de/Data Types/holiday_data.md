<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## HOLIDAY_DATA

| | | |
|:---|:---|:---|
| ***.NAME** | STRING(30) | Name des Feiertages |
| ***.DAY** | SINT | Tag des Feiertages |
| ***.MONTH** | SINT | Monat des Feiertages |
| ***.USE** | SINT | aktiviert den Feiertag (0=aus, 1=ein) |

Die Struktur HOLIDAY_DATA findet Verwendung zur Definition und Beschreibung von Feiertagen.

Die Struktur wird zum Beispiel von Modulen wie CALENDAR_CALC und HOLIDAY verwendet, indem ein Array vom Datentyp HOLIDAY_DATA zur Definition der jährlichen Feiertage verwendet wird.

Es sind 3 verschiedene Arten von Definitionen vorgesehen:

DAY 1..31, MONTH 1..12, USE 1 (Feiertag an einem festen Datum)

DAY ±X, MONTH 0, USE 1 (Feiertag ist X Tage vor oder nach Ostern)

DAY 1..31, MONTH 1..12, USE -7..-1 (Feiertag an einem Wochentag vor einem Datum, hierbei ist -1 Montag und -7 Sonntag.

**Beispiel:**

Beispiele:

(NAME := 'Neujahr', DAY := 1, MONTH := 1, USE := 1) Feiertag mit einem festen Datum USE=1 bedeutet er ist aktiv.

(NAME := 'Neujahr', DAY := 1, MONTH := 1, USE := 0) Feiertag mit einem festen Datum USE=0 bedeutet er ist nicht aktiv.

(NAME := 'Karfreitag', DAY := -2, MONTH := 0, USE := 1) Feiertag mit einem festen Offset vom Ostersonntag, in diesem Fall ist der Karfreitag 2 Tage vor dem Ostersonntag.

(NAME := 'Buß und Bettag', DAY := 23, MONTH := 11, USE := -3) Feiertag am letzten Mittwoch vor dem 23.11. eines Jahres.

Beispiele für Feiertagsdefinitionen:

Array für Bayerische Feiertage

HOLIDAY_DE : ARRAY[0..29] OF HOLIDAY_DATA := (name := 'Neujahr', day := 1, month := 1, use := 1),

(name := 'Heilig Drei Könige', day := 6, month := 1, use := 1),

(name := 'Karfreitag', day := -2, month := 0, use := 1),

(name := 'Ostersonntag', day := 0, month := 0, use := 1),

(name := 'Ostermontag', day := 1, month := 0, use := 1),

(name := 'Tag der Arbeit', day := 1, month := 5, use := 1),

(name := 'Christi Himmelfahrt', day := 39, month := 0, use := 1),

(name := 'Pfingstsonntag', day := 49, month := 0, use := 1),

(name := 'Pfingstmontag', day := 50, month := 0, use := 1),

(name := 'Fronleichnam', day := 60, month := 0, use := 1),

(name := 'Augsburger Friedensfest', day := 8, month := 8, use := 0),

(name := 'Maria Himmelfahrt', day := 15, month := 8, use := 1),

(name := 'Tag der Deutschen Einheit', day := 3, month := 10, use := 1),

(name := 'Reformationstag', day := 31, month := 10, use := 0),

(name := 'Allerheiligen', day := 1, month := 11, use := 1),

(name := 'Buss und Bettag', day := 23, month := 11, use := 0),

(name := '1. Weihnachtstag', day := 25, month := 12, use := 1),

(name := '2. Weihnachtstag', day := 26, month := 12, use := 1);

Array für Österreichische Feiertage

HOLIDAY_AT : ARRAY[0..29] OF HOLIDAY_DATA := (name := 'Neujahr', day := 1, month := 1, use := 1),

(name := 'Heilig Drei Könige', day := 6, month := 1, use := 1),

(name := 'Karfreitag', day := -2, month := 0, use := 1),

(name := 'Ostersonntag', day := 0, month := 0, use := 1),

(name := 'Ostermontag', day := 1, month := 0, use := 1),

(name := 'Christi Himmelfahrt', day := 39, month := 0, use := 1),

(name := 'Pfingstsonntag', day := 49, month := 0, use := 1),

(name := 'Pfingstmontag', day := 50, month := 0, use := 1),

(name := 'Fronleichnam', day := 60, month := 0, use := 1),

(name := '', day := 8, month := 8, use := 0),

(name := 'Maria Himmelfahrt', day := 15, month := 8, use := 1),

(name := '', day := 3, month := 10, use := 0),

(name := '', day := 31, month := 10, use := 0),

(name := 'Allerheiligen', day := 1, month := 11, use := 1),

(name := 'Maria Empfängnis', day := 8, month := 12, use := 1),

(name := '1. Weihnachtstag', day := 25, month := 12, use := 1),

(name := '2. Weihnachtstag', day := 26, month := 12, use := 1);

Französische Feiertage

HOLIDAY_FR : ARRAY[0..29] OF HOLIDAY_DATA := (name := 'Nouvel an', day := 1, month := 1, use := 1),

(name := 'St Valentin', day := 14, month := 2, use := 0),

(name := 'Vendredi Saint (alsace)', day := -2, month := 0, use := 0),

(name := 'Dimanche de pâques', day := 0, month := 0, use := 1),

(name := 'Lundi de pâques', day := 1, month := 0, use := 1),

(name := 'Jeudi de Ascension', day := 39, month := 0, use := 1),

(name := 'dimanche de Pentecôte ', day := 49, month := 0, use := 1),

(name := 'jeudi de la Trinité', day := 60, month := 0, use := 0),

(name := 'Fête du travail', day := 1, month := 5, use := 1),

(name := 'Victoire 1945 ', day := 8, month := 5, use := 1),

(name := 'Prise de La bastille', day := 14, month := 7, use := 1),

(name := '15 Août 1944', day := 15, month := 8, use := 1),

(name := 'Halloween', day := 31, month := 10, use := 0),

(name := 'Armistice 1918', day := 11, month := 11, use := 1),

(name := 'Noël', day := 25, month := 12, use := 1),

(name := 'Saint Étienne (alsace)', day := 26, month := 12, use := 0),

(name := 'Fête de la musique', day := 21, month := 6, use := 0);

Belgien Deutschsprachig

HOLIDAY_BED : ARRAY[0..29] OF HOLIDAY_DATA :=	(name := 'Neujahr', day := 1, month := 1, use := 1),

(name := 'Ostersonntag', day := 0, month := 0, use := 1),

(name := 'Ostermontag', day := 1, month := 0, use := 1),

(name := 'Tag der Arbeit', day := 1, month := 5, use := 1),

(name := 'Christi Himmelfahrt', day := 39, month := 0, use := 1),

(name := 'Pfingsten', day := 49, month := 0, use := 1),

(name := 'Pfingstmontag', day := 50, month := 0, use := 1),

(name := 'Nationalfeiertag', day := 21, month := 7, use := 1),

(name := 'Mariä Himmelfahrt', day := 15, month := 8, use := 1),

(name := 'Allerheiligen', day := 1, month := 11, use := 1),

(name := 'Feiertag DG', day := 15, month := 11, use := 1),

(name := 'Heiligabend', day := 24, month := 12, use := 1),

(name := '1. Weihnachtstag', day := 25, month := 12, use := 1),

(name := '2. Weihnachtstag', day := 26, month := 12, use := 1),

(name := 'Silvester', day := 31, month := 12, use := 1);

Italien Südtirol

HOLIDAY_ITD : ARRAY[0..29] OF HOLIDAY_DATA := (name := 'Neujahr', day := 1, month := 1, use := 1),

(name := 'Heilig Drei Könige', day := 6, month := 1, use := 1),

(name := 'Ostersonntag', day := 0, month := 0, use := 1),

(name := 'Ostermontag', day := 1, month := 0, use := 1),

(name := 'Tag der Befeiung Italiens', day := 25, month := 4, use := 1),

(name := 'Tag der Arbeit', day := 1, month := 5, use := 1),

(name := 'Pfingsten', day := 49, month := 0, use := 1),

(name := 'Pfingstmontag', day := 50, month := 0, use := 1),

(name := 'Tag der Republik Italien', day := 2, month := 6, use := 1),

(name := 'Mariä Himmelfahrt', day := 15, month := 8, use := 1),

(name := 'Allerheiligen', day := 1, month := 11, use := 1),

(name := 'Mariä Empfängnis', day := 8, month := 12, use := 1),

(name := 'Heiligabend', day := 24, month := 12, use := 0),

(name := '1. Weihnachtstag', day := 25, month := 12, use := 1),

(name := '2. Stephanstag', day := 26, month := 12, use := 1); *)
