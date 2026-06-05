<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Die folgenden Bausteine sind so konzipiert und aufeinander abgestimmt dass Sie einen modularen Aufbau eines Jalousiecontrollers ermöglichen. Dieses modulare System erlaubt einen schnellen und einfachen Aufbau von einfachen bis komplexen Jalousiecontrollern die exakt auf die Anwendung abgestimmt sind. Das System lässt sich auch später jederzeit erweitern und erlaubt einen beliebigen Ausbau des Funktionsumfangs. Die Anwendungen umfassen Jalousien aller Art, Rollladen, und alle Arten von Beschattungseinrichtungen. Die Module sind so gestaltet das sie sich einfach hintereinander schalten lassen und die Reihenfolge der Verschaltung gleichzeitig die Priorität der Funktionen festlegt. Die Signale UP und DN für den Handbetrieb, sowie die Vorgaben für Winkel und Position im Automatikbetrieb (PI und AI) werden dabei von Modul zu Modul weitergereicht, was einen simplen Signalfluss und einen übersichtlichen Aufbau gewährleistet. Eine Besonderheit ist dabei das Die Signale UP und DN wenn beide gleichzeitig TRUE sind den Automatikmodus einschalten.

Alle Bausteine haben die Eingänge UP und DN mit denen der Manuelle Auf und Ab Befehl empfangen wird und durch QU und QD an den nächsten Baustein weitergereicht wird. Werden beide Eingänge UP und DN auf TRUE gesetzt so schalten die betreffenden Module auf Automatik Modus und werten die Eingänge PI und AI (Position- und Winkel- Eingang für die Jalousie aus. Durch die Reihenschaltung einzelner Funktionen kann im Falle einer Fehlersuche auf einfache Weise der Signalfluss und die Funktionsweise überprüft werden. Durch die Reihenfolge der Module wird auch gleichzeitig die Priorität der einzelnen Funktionen festgelegt und kann ohne großen Aufwand vom Anwender jederzeit geändert werden. Zukünftige oder Kundenspezifische Funktionen können auf diese Weise einfach und schnell in die Vorhandenen Blöcke eingeschaltet werden ohne dabei die vorhandene Programmierung ändern zu müssen. Der Ausgang STATUS gibt ESR kompatible Meldungen über den Zustand des betreffenden Bausteins aus. Wenn keine eigenen Zustandsmeldungen anstehen reicht jeder Baustein die am Eingang S_IN anliegenden Statusmeldungen an den Ausgang STATUS weiter. Zusammenfassung aller Blind Statusmeldungen:

| STATUS | Modul | Beschreibung |
| --- | --- | --- |
| 111 | SECURITY | Sicherheitsstellung bei Feuer |
| 112 | SECURITY | Sicherheitsstellung bei Wind |
| 113 | SECURITY | Sicherheitsstellung bei ALARM |
| 114 | SECURITY | Sicherheitsstellung Türkontakt |
| 115 | SECURITY | Sicherheitsstellung bei Regen |
| 1 | ACTUATOR | Fehler UP und DOWN gleichzeitig |
| 120 | ACTUATOR | Auf Bewegung |
| 121 | ACTUATOR | Ab Bewegung |
| 121 | CONTROL | Auf Bewegung Position |
| 122 | CONTROL | Ab Bewegung Position |
| 123 | CONTROL | Auf Bewegung Winkel |
| 124 | CONTROL | Ab Bewegung Winkel |
| 121 | CONTROL_S | Auf Bewegung |
| 122 | CONTROL_S | Ab Bewegung |
| 123 | CONTROL_S | Auto Positionierung |
| 127 | CONTROL_S | Lockout Time |
| 128 | CONTROL_S | Kalibrierung |
| 129 | CONTROL_S | Extend Mode |
| 130 | INPUT | Standby |
| 131 | INPUT | Manual Timeout |
| 132 | INPUT | Manual Up |
| 133 | INPUT | Manual Down |
| 134 | INPUT | Single click up |
| 135 | INPUT | Single click down |
| 136 | INPUT | Forcedposition |
| 137 | INPUT | Double click 1 |
| 138 | INPUT | Double click 2 |
| 141 | NIGHT | Nachtstellung aktiv |
| 151 | SHADE | Beschattung aktiv |
| 160-175 | SCENE | Aktive Szene |
| 178 | SET | Set operation |
| 179 | SET | Restoreoperation |
