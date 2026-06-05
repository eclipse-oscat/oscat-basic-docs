<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SNTP_CLIENT

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	IP_C** | IP_C (parameterization) |
| **S_BUF** | NETWORK_BUFFER (transmit data) |
| **R_BUF** | NETWORK_BUFFER (receive data) |
| **INPUT	IP4** | DWORD (IP address of the SNTP server) |
| **ACTIVATE** | BOOL (Starts the query) |
| **OUTPUT	ERROR** | DWORD (error code) |
| **DONE_P** | BOOL (positive edge finish without error) |
| **UDT** | DT (Date and time output as Universal Time) |
| **XMS** | INT (millisecond of Universal Time UDT) |
| | The SNTP_CLIENT is used to synchronize local time with an SNTP server. For this, the Simple Network Time Protocol is used which is designed to provide a reliable time information over networks with variable packet delay. The SNTP is technically completely identical with NTP, which here means no differences. Therefore, all known SNTP and NTP server can be used, whether it be on the local network or via the Internet. For IP4 a IP-address of a SNTP / NTP server is specified. A positive edge at ACTIVATE starts the query. The elapsed time between sending and receiving of the time is measured and a time correction is calculated. Then, the received time will be corrected by this value. Upon successful completion DONE_P is one positive edge, and the current time is passed at UDT. On XMS the associated fractional seconds as milliseconds are passed. The values of UDT and XMS are only valid when DONE_P = TRUE, since this is a static time value, and is only used for setting of pulse-controlled time. ERROR gives at error the exact cause (See block IP_CONTROL). |

![sntp_client](sntp_client.gif)
