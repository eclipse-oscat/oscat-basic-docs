<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## HTTP_GET

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	URL_DATA** | URL (data STRING_TO_URL) |
| **IP_C** | IP_C (parameterization) |
| **S_BUF** | NETWORK_BUFFER (transmit data) |
| **R_BUF** | NETWORK_BUFFER (receive data) |
| **INPUT	IP4** | DWORD (IP address of the HTTP server) |
| **GET** | BOOL (Starts the HTTP query) |
| **MODE** | BYTE (version of the HTTP GET query) |
| **UNLOCK_BUF** | BOOL (release of the receive data buffer) |
| **OUTPUT	HTTP_STATUS** | STRING (HTTP status code) |
| **HTTP_START** | UINT (start position of the message header) |
| **HTTP_STOP** | UINT (stop position of the message header) |
| **BODY_START** | UINT (start position of the message body) |
| **BODY_STOP** | UINT (stop position of the message body) |
| **DONE** | BOOL (task performed without error) |
| **ERROR** | DWORD (error code) |
| | HTTP_GET does at positive edge of Get a GET-command on an HTTP server. IWith MODE the HTTP protocol version can be specified. The requested URL (web link) must be submitted completely processed in the URL_DATA structure. The full URL should therefore be processed before the module call by "STRING_TO_URL.  After a successful query DONE = TRUE, and the parameters HTTP_START and HTTP_STOP point to the data area in which the message header data for further processing and evaluation are to be found. Normally, a message body is present, which in turn is transmitted via BODY_START and BODY_STOP. Also, on HTTP_STATUS is reported the HTTP status code as a string. One of the difficulties in receiving the HTTP data is the end of the data stream. This module pursued multiple strategies. In the process of the HTTP/1.0 the end of  receiving data is detected by disconnection of the host. Furthermore, always the information in the header "Content-Length" is checked, and with this can be clearly recognized, that all data is received. If none of the previous versions is true, so a simple Receive Timeout Error detectes the end of data transmission. The only downside is, that this takes time. Sometimes, depending on the timeout value longer than desired. Therefore it is not bad if a reasonable timeout value is set at IP_CONTROL. ERROR gives at errors, the exact cause (See module IP_CONTROL) |
| **The following MODE can be used** |  |

![http_get](http_get.gif)

| Mode | Protocol Version | Properties |
| --- | --- | --- |
| 0 | HTTP/1.0 | The host terminates automatically the TCP connection, after the transfer of data. |
| 1 | HTTP/1.0 | By applying "Connection: Keep-Alive", the host is instructed to use a persistent connection. The client should end of the connection after stopping activities. |
| 2 | HTTP/1.1 | The host uses a persistent connection and must be stopped by client. |
| 3 | HTTP/1.1 | By use of "Connection: Close"  the host is instructed to stop transmission of data, the TCP connection. |
