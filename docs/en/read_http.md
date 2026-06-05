<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## READ_HTTP

| | |
|:---|:---|
| **Type	Function module** |  |
| **INPUT	SIZE** | UINT	(Buffer size) |
| **POS** | INT		(position as of that the search is started) |
| **SRC** | STRING	(Search string) |
| **IN_OUT	PT** | POINTER	(Address of the buffer) |
| **OUTPUT** | VALUE		(Parameters of the header information) |
| | After a successful HTTP-GET  Request  always a HTTP header (message header) and a message body (message body) is available in the buffer. In the HTTP header various information about the requested HTTP page is stored. The following message body contains the actual requested data. With READ_HTTP the HTTP header information can be analyzed. The module searches any array of bytes on the contents of a string and then evaluates the following parameters, and returns that string as its result. The data in the buffer are automatically converted to upper case, so all search string at SRC has to be too, given in capital letters. With POS it can begin its search at any position. The first element in the array is at position number 1 |

![read_http](read_http.gif)

**Beispiel:**

Example of an HTTP response (header information): HTTP/1.0 200 OK<CR><LF> Content-Length: 2165<CR><LF> Content-Type: text/html<CR><LF> Date: Mon, 15 Sep 2008 16:59:08 GMT<CR><LF> Last-Modified: Wed, 18 Jun 2008 12:35:52 GMT<CR><LF> Mime-Version: 1.0<CR><LF><CR><LF> If SRC does not include a search term, automatically the HTTP version and the HTTP status code in the buffer is searched and evaluated. As a result, according to the above example "1.0 200 OK" is returned. If SRC is in a search term, this header information is searched in the buffer and the value as a string eg 'Content-Length' = "2165" is returned.
