<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## CONSTANTS_LOCATION

Diese Struktur definiert Ortsabhängige Konstanten. Die Variable LOCATION der Globalen Variablenliste stellt diese in der Bibliothek zur Verfügung. *.DEFAULT : INT := 1; (1=Deutschland, 2=Österreich, 3=Frankreich, 4=Belgien-Deutsch, 5= Italien-Südtirol). *.LMAX : INT := 5;	gibt an wie viele Orte definiert sind. *.LANGUAGE : ARRAY[1..5] of INT := 2,2,3,2,2; für jede Location wird die Sprache definiert.
