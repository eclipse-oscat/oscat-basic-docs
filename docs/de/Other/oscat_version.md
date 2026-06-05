<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion : DWORD

| | |
|:---|:---|
| **Input	IN** | BOOL (wenn TRUE liefert der Baustein das Release Datum) |
| **Output** | (Version der Bibliothek) |
| | OSCAT_VERSION gibt wenn IN = FALSE die aktuelle Versionsnummer als DWORD zurück. Wird IN auf TRUE gesetzt so wird das Release Datum der aktuellen Version als DWORD zurückgegeben. |

![oscat_version](oscat_version.gif)

**Beispiel:**

```iecst
OSCAT_VERSION(FALSE) = 201 für Version 2.60 DWORD_TO_DATE(OSCAT_VERSION(TRUE)) = 2008-1-1
```
