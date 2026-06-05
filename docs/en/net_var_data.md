<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## NET_VAR_DATA

NET_VAR data structure:

| Name | Type | Properties |
| --- | --- | --- |
| CYCLE | UDINT | Cycle Counter |
| STATE | BYTE | Operating condition |
| INDEX | INT | Read / write index |
| ID_MAX | USINT | Number of satellite components |
| Error_id | BYTE | ID number of the faulty module |
| BUF_SIZE | UINT | Size of the buffer (bytes) |
| S_BUF | NETWORK_BUFFER | Network buffer for sending data |
| R_BUF | NETWORK_BUFFER | Network buffers for receiving data |
