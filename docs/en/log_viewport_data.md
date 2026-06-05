<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## us_LOG_VIEWPORT

us_LOG_VIEWPORT

| Name | Type | Properties |
| --- | --- | --- |
| LINE_ARRAY | ARRAY [1..40] OF INT | LOG-index references |
| COUNT | INT | Number of visible messages |
| UPDATE_COUNT | UINT | Update count |
| MOVE_TO_X | INT | Control of the message display |
| UPDATE | BOOL | Data has been changed -> redraw |
