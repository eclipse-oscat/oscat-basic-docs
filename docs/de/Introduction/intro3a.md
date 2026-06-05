<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Die Zeit und Datumsfunktionen der OSCAT Bibliothek sind abhängig vom Zielsystem so Implementiert das sie die Unterschiede in der Implementierung der Datums / Zeittypen der Einzelsysteme berücksichtigen. Zum Beispiel ist auf CoDeSys Systemen das UNIX TIMEDATE Implementiert, was bedeutet das der Datentyp TD in Sekunden ab 1.1.1970-00:00 als 32 Bit Wert abgebildet wird. In STEP7 hingegen wird der Datentyp TD in Sekunden ab 1.1.1990 abgebildet. Der Wertebereich der Zeit / Datumsfunktionen ist bei CoDeSys Systemen 1.1.1970 – 31.12.2099 und bei STEP7 Systemen 1.1.1990 – 31.12.2099. Die Begrenzung des Wertebereichs auf das Jahr 2099 liegt vor allem an der Tatsache das im Jahr 2100 kein Schaltjahr sein wird.

Weiterhin entsprechen die Datums und Zeitfunktionen der ISO8601 (internationaler Standard für numerische Datumsfunktionen). Hier ist zum Beispiel die Implementierung der Wochentage mit 1 = Montag und 7 = Sonntag vorgeschrieben.
