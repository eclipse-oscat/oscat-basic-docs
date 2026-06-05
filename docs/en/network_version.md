<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## NETWORK_VERSION

| | |
|:---|:---|
| **Type	Function** | DWORD |
| **Input	IN** | BOOL (if TRUE the module provides the   release date) |
| **Output** | (Version of the library) |
| | NETWORK_VERSION provides if IN = FALSE the current version number as DWORD. If IN is set to TRUE then the  release  date of the current version as a DWORD is returned. |

![network_version](network_version.gif)

**Beispiel:**

Example:	NETWORK_VERSION(FALSE) = 111 for version 1.11 DWORD_TO_DATE(NETWORK_VERSION(TRUE)) = 2011-2-3
