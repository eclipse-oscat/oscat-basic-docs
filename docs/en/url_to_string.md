<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## URL_TO_STRING

| | |
|:---|:---|
| **Type	Function** | STRING (string_length) |
| **Input	IN** | STRING( Unified Resource Locator  ) |
| **Output** | URL (URL) |
| | URL_TO_STRING generates from stored data in IN with type URL a Unified  Resource  Locator  as String . |
| **A URL is as follows** |  |
| **protokoll** | //user:passwort@domain:port/path?query#anchor |

![url_to_string](url_to_string.gif)

**Beispiel:**

Example:  ftp://hugo:nono@oscat.de:1234/download/manual.html some parts of the URL are optional, such as user name, password, Anchor,  Query  ...
