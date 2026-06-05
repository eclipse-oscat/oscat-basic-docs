<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : INT

| | |
|:---|:---|
| **Input	DIR** | STRING(3) (Himmelsrichtung in Kompassangaben) |
| **L** | INT (Sprachauswahl) |
| **Output** | INT (Himmelsrichtung in Grad) |
| | DIR_TO_DEG wandelt eine Himmelsrichtung in der Form NNO in Grad um. Es werden dabei bis zu 3 Stellen ausgewertet, was einer Auflösung von 22.5° entspricht. Der Ausgang ist vom Typ Integer. Der Eingang muss in Großbuchstaben vorliegen und Osten darf mit O oder E bezeichnet werden. Die Zeichenkette NO wird in 45° gewandelt. L spezifiziert die zu verwendende Sprache, für detaillierte Informationen siehe Datentyp [CONSTANTS_LANGUAGE](../../Data Types/constants_language.md). |
| **Die Himmelsrichtungen sind** | 0° = Nord, 90° = Ost, 180° = Süd und 270° = Westen. Die Umwandlung erfolgt nach folgender Tabelle: |

![dir_to_deg](dir_to_deg.gif)

| N | 0° | NNO, NNE | 23° | NO | 45° | ONO, ENE | 68° |
| --- | --- | --- | --- | --- | --- | --- | --- |
| O | 90° | OSO, ESE | 113° | SO, SE | 135° | SSO, SSE | 158° |
| S | 180° | SSW | 203° | SW | 225° | WSW | 248° |
| W | 270° | WNW | 293° | NW | 315° | NNW | 338° |
