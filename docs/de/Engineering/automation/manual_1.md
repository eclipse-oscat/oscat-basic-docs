<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MANUAL_1

| | |
|:---|:---|
| **Type** | Funktionsbaustein |
| **Input	IN** | BOOL (Eingangssignal) |
| **MAN** | BOOL (Umschaltung auf Handbetrieb) |
| **M_I** | BOOL (Signalpegel bei Handbetrieb) |
| **SET** | BOOL (Asynchroner Set bei Handbetrieb) |
| **RST** | BOOL (Asynchroner Reset bei Handbetrieb) |
| **Output	Q** | BOOL (Ausgangssignal) |
| **STATUS** | BYTE (ESR kompatibler Status Ausgang) |
| | MANUAL_1 kann ein digitales Signal im Handbetrieb überschreiben. Solange MAN = FALSE folgt der Ausgang Q Eingang direkt dem Eingang IN. Sobald MAN = TRUE wird folgt der Ausgang dem Zustand des Eingangs M_I. Mit den Eingängen SET und RST kann im Handbetrieb ein asynchrones Setzen und Löschen des Ausgangs erzeugt werden. SET und RST sind nur während des Handbetriebs aktiv. Wird im Handbetrieb an SET oder RST eine steigende Flanke registriert, so folgt der Ausgang nicht mehr dem Eingang M_I sondern bleibt auf dem Zustand den eine steigende Flanke an SET (Ausgang = TRUE) beziehungsweise RST (Ausgang = FALSE) erzeugt hat. Sobald der Eingang MAN wieder auf FLASE geht folgt der Ausgang Q wieder dem Eingang IN. |

![manual_1](manual_1.gif)
