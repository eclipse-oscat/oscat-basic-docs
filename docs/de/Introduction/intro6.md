<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Einleitung

Die hier beschriebenen Listen sind als STRING(LIST_LENGTH) gespeicherte Listen die Elemente der Liste beginnen mit dem Zeichen SEP gefolgt vom Element. Die Elemente können alle in Strings zulässigen Zeichen enthalten und können auch eine Leere Zeichenkette sein. Eine Leere Liste wird durch den STRING '' abgebildet, der STRING enthält keine Elemente. Die Länge einer Liste ist die Anzahl der Elemente die in der Liste enthalten sind, die Länge ist bei einer Leeren Liste 0. Die Funktionen zur Verarbeitung von Listen benutzen für die Listen I/O Variablen, damit die unter Umständen langen Listen nicht bei jedem Funktionsaufruf erst im Speicher kopiert werden müssen. Das Separationszeichen SEP der Listen kann vom Anwender Frei festgelegt werden und wird den Funktionen mit dem Eingang SEP übergeben. Das Separationszeichen ist immer nur ein einzelnes Zeichen und kann jedes in einem STRING zulässige Zeichen sein. In den folgenden Beispielen wird als Separationszeichen ein '§' verwendet. Leere Liste:							'' Liste mit einem Leeren Element:			'§' Liste mit 2 Elementen					'§1§NIX' Liste mit 6 Elementen wovon eines Leer ist	'§1§§33§/§1§2'
