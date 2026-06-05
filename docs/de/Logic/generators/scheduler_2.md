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
| **Input	E0..3** | BOOL (Freigabesignale für Q0..3) |
| **Output	Q0..3** | BOOL (Ausgangssignale) |
| | SCHEDULER_2 aktiviert abhängig von den Setup Variablen C? Und O? Die Ausgänge Q?. SCHEDULER_2 kann einen Ausgang Q? Alle C? Zyklen aktivieren um damit Programmteile mit verschiedenen Zykluszeiten zu starten. Ein optionaler Setup Parameter O? Dient dazu einen Zeitversatz von O? Zyklen für den entsprechenden Ausgang zu definieren um ein gleichzeitiges aktivieren der Ausgänge im ersten Zyklus zu verhindern. |
| **Setup	C0..3** | UINT (Der Ausgang Q? Wird alle C? Zyklen aktiviert) |
| **O0..3** | UINT (Verzögerung für die Ausgänge) |

![scheduler_2](scheduler_2.gif)
