<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## STRING_TO_URL

| | |
|:---|:---|
| **Type	 Function** | URL |
| **Input	STR** | STRING (string_length) (  Unified  Resource  Locator  ) |
| **DEFAULT_PROTOCOL** | STRING(replacement protocol) |
| **DEFAULT_PATH** | STRING (alternate path) |
| **Output** | URL (URL) |
| | STRING_TO_URL split a URL (  Uniform  Resource  Locator  ) into its components and stores it in the data type URL. If in STR no path or protocoll is specified, so the function sets the missing values automatically with the specified replacement values. |
| **A URL is as follows** |  |
| **Protocol** | / /  user  :  Password  @  domain  :  port  /  path  ?  query  #  anchor |

![string_to_url](string_to_url.gif)

**Beispiel:**

Example:  ftp://hugo:nono@oscat.de:1234/download/manual.html some parts of the URL are optional, such as user name, password, Anchor,  Query  ...
