<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DLOG_FILE_TO_SMTP

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	SERVER** | STRING (URL of the SMTP server) |
| **MAIL FROM** | STRING (return address) |
| **MAILTO** | STRING (string_length) (recipient address) |
| **SUBJECT** | STRING (subject text) |
| **SUBJECT** | STRING (subject text) |
| **FILES** | STRING (string_length) (files to be sent) |
| **X** | DLOG_DATA (DLOG data structure) |
| **INPUT	FILE_DELETE** | BOOL (delete files after transfer) |
| **TIMEOUT** | TIME (time) |
| **DTI** | DT (current date-time) |
| **DTI_OFFSET** | INT (time zone offset from UTC) |
| **RETRY** | INT (number of repetitions) |
| **RETRY_TIME** | TIME (waiting period before repetition) |
| **Dns_ip4** | DWORD (IP4 address of the DNS server) |
| **OUTPUT	DONE** | BOOL   (Transfer completed without error) |
| **BUSY** | BOOL   (Transfer active) |
| **ERROR_C** | DWORD   (Error code) |
| **ERROR_T** | BYTE   (Problem type) |
| | The module DLOG_FILE_TO_SMTP is used to automatically transfer the of DLOG_STORE_FILE_CSV generated files as e-mail to an e-mail server. |
| | The module uses internally the SMTP_CLIENT for sending. |
| | The SERVER parameter contains the name of the SMTP server and optionally the user name and password and a port number. If you pass a user name and password, the procedure is according to standard SMTP. |
| **SERVER** | URL Examples: |
| **username** | password@smtp_server |
| **username** | password@smtp_server:portnumber |
| | smtp_server |
| **Special case** |  |
| | If in the username is a '@' included this must be passed as '%' - character, and is then automatically corrected by the module again. |
| **By specifying user and password the Extend-SMTP is used, and automatically the safest possible  Authentication method is used.  If parameter is to specify the MAIL FROM sender address** |  |
| | i.e. oscat@gmx.net |
| | Optionally, an additional "Display Name" be added This is displayed the email client automatically instead of the real return address. Therefore, always an easily recognizable name to be used. |
| | i.e.. oscat@gmx.net;Station_01 |
| | The email client shows as the sender then "Station_01".   Thus, more people will use the same email address but send a own "Alias". |
| | At the MAILTO parameter can To, Cc, Bc be specified. The different groups of recipients are specified by '#' as the separator in a list. Multiple addresses within the same group are divided with the separator ";" . In each group can be defined unlimited count of recipients, the only limitation is the length of the mailto string. |
| | To;To..#Cc;Cc...#Bc;Bc... |

![dlog_file_to_smtp](dlog_file_to_smtp.gif)

**Beispiel:**

Examples. o1@gmx.net;o2@gmx.net#o1@gmx.net#o2@gmx.net defines two TO-addresses, one CC-address and a Bc-address ##o2@gmx.net defines only one BC-address. With subject, a subject text will be specified, as well as with BODY an email text content. The current Date / Time value must be definded at DTI, and at DTI_OFFSET the correction value as an offset in minutes from UTC (Universal Time). If the DTI in UTC time is passed, at DTI_OFFSET a 0 must be passed. The monitoring time can be specified with parameter TIMEOUT. At dns_ip4 must be specified the IP address of the DNS server, if in SERVER a DNS name is specified. If  errors occur during the transmission, they are passed at ERROR_C and ERROR_T. As long as the transfer is running, BUSY = TRUE, and after an error-free completion of the operation, DONE = TRUE. Once a new transfer is started, DONE,  ERROR_T and ERROR_C are reseted. If parameter RETRY = 0, then the SMTP transfer was repeated until it completes successfully. If RETRY state at a value > 0, then the SMTP transfer is just as often repeated at transmission failure. Then this job is simply discarded and the process continues with the next file. With RETRY-TIME the waiting time between the repetitions can be defined. The parameter FILE_DELETE = TRUE a file is deleted on the controller after successful transfer via email. The module has integrated the IP_CONTROL and so must not be externally linked to this, as it would be at default  necessary. Basics: http://de.wikipedia.org/wiki/SMTP-Auth http://de.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol ERROR_T:

| Value | Properties |
| --- | --- |
| 1 | Problem: DNS_CLIENTThe exact meaning of ERROR_C can be read at module DNS_CLIENT |
| 2 | Problem: SMTP ChannelThe exact meaning of ERROR_C can be read at module IP_CONTROL |
| 4 | Problem: FILE_SERVERThe exact meaning of ERROR_C can be read at block FILE_SERVER |
| 5 | Problem: END - TIMEOUTERROR_C  contains the left WORD the end of the step number, and in the right WORD the last response code received by the SMTP server.The parameters must be considered first as a HEX value, divided into two WORDS, and then be considered as a decimal value.Example:ERROR_T = 5ERROR_C = 0x0028_00FAEnd-step number 0x0028 = 40Response-Code 0x00DC = 250 |
