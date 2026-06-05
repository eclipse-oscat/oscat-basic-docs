<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## URL

The  Structure  URL stores the individual parts of a URL. URL:

| Data field | Data Type | Description |
| --- | --- | --- |
| PROTOCOL | STRING (10) | Protocol |
| USER | STRING(32) | User Name |
| PASSWORD | STRING(32) | Passwort |
| DOMAIN | STRING(80) | Domain |
| PORT | WORD | Port Nummer |
| PATH | STRING(80) | Pfadangabe |
| QUERY | STRING(120) | Query |
| ANCHOR | STRING (40) | Anker |
| HEADER | STRING(160) | Header |
