<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Globale Konstanten

| | |
|:---|:---|
| **SETUP** |  |
| | SETUP definiert allgemeine Grundeinstellungen. Die Einstellungen sind in der TYP Definition [CONSTANTS_SETUP](Data Types/constants_setup.md) definiert. |
| **LOCATION** |  |
| | LOCATION definiert Ortseinstellungen, hierzu zählen unter anderem auch Feiertagsdefinitionen. Die Einstellungen sind in der TYP Definition [CONSTANTS_LOCATION](Data Types/constants_location.md) definiert. |
| **STRING_LENGTH** | INT := 250. |
| | STRING_LENGTH ist per Default 250 Zeichen, und wird von STRING Funktionen benutzt um eine Bereichsüberschreitung bei Verarbeitung von STRINGS zu vermeiden. STRING_LENGTH legt auch innerhalb der OSCAT LIB die maximale STRING Länge fest welche bei häufiger Nutzung des Datentyps STRING zu hohem Speicherverbrauch führen kann. Wenn in einer Anwendung nur kurze STRINGS verarbeitet werden müssen so kann über diese SETUP Konstante die STRING Länge entsprechend reduziert werden. Wir empfehlen STRINGS innerhalb der Anwendung unter Zuhilfenahme dieser  Konstante zu definieren. Werden längere STRINGS als 80 Zeichen zur Verarbeitung nötig kann diese Konstante auf Werte bis 255 erhöht werden. |
| **NEUER_STRING** | STRING(STRING_LENGTH). |
| | Durch diese Definition ist auch der neu definierte STRING automatisch auf die Länge von STRING_LENGTH definiert und kann wenn nötig global geändert werden. |
| **LIST_LENGTH** | INT := 250. |
| | LIST_LENGTH ist per Default 250 Zeichen und legt die Größe von Listen fest. |

Die OSCAT Bibliothek versucht globale Variablen zu vermeiden, um möglichst einfach in fremde Umgebungen integriert werden zu können. Globale Variablen sind nicht für Funktion oder den Datenaustausch zwischen Bausteinen nötig. Das Setup und die Konfiguration ist vollständig innerhalb der Module realisiert, um höchste Modularität und Portabilität zu gewährleisten. Für physikalische und mathematische Konstanten haben wir uns aus Gründen der Übersichtlichkeit jedoch dazu entschlossen, Globale Konstanten zu verwenden. MATH : MATH definiert mathematische Konstanten. Die Konstanten sind in der TYP Definition [CONSTANTS_MATH](Data Types/constants_math.md) definiert. PHYS : PHYS definiert physikalische Konstanten. Die Konstanten sind in der TYP Definition [CONSTANTS_PHYS](Data Types/constants_phys.md) definiert. LANGUAGE : LANGUAGE definiert Spracheinstellungen. Die Einstellungen sind in der TYP Definition [CONSTANTS_LANGUAGE](Data Types/constants_language.md) definiert.
