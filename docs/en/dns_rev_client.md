<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## DNS_REV_CLIENT

| | |
|:---|:---|
| **Type** | Function module |
| **IN_OUT	IP_C** | IP_C (parameterization) |
| **S_BUF** | NETWORK_BUFFER (transmit data) |
| **R_BUF** | NETWORK_BUFFER (receive data) |
| **INPUT	ACTIVATE** | BOOL (query start by positive edge) |
| **DOMAIN** | STRING 	(Domain name or IP as String) |
| **IP4_DNS** | DWORD (IPv4 address of the DNS server) |
| **OUTPUT	IP4** | DWORD (IPv4 address of the requested domain) |
| **DONE** | BOOL (IP of the domain has been queried successfully) |
| **ERROR** | DWORD (error code) |
| | DNS_REV_CLIENT determine from the given IP address   the officially registered domain name. For this purpose a reverse DNS query on the configured IP address with a DNS server is made. With positive edge of ACTIVATE the specified IP is stored so that they no longer must be present. If the query result in more matches, it will always use the last record. As IP4_DNS can be used any public DNS servers. If the PLC is sitting behind a DSL router,   this router can be used as a DNS server through its gateway address. Which ultimately leads to faster even with repeated requests response times because they are managed in the router cache. With positive results DONE = TRUE the DOMAIN contains the officially registered domain name until the start of the next query by positive edge of ACTIVATE. ERROR gives ao error, the error code. (See error codes). |
| **Error Codes** |  |

![dns_rev_client.GIF](dns_rev_client.GIF)

| Value | Source | Description |
| --- | --- | --- |
| B3 | B2 | B1 | B0 |  |  |
| nn | nn | nn | xx | IP_CONTROL | Error from module IP_CONTROL |
| xx | xx | xx | 00 | DNS_CLIENT | No error: The request completed successfully |
| xx | xx | xx | 01 | DNS_CLIENT | Format error: The name server was unable to interpret the query. |
| xx | xx | xx | 02 | DNS_CLIENT | Server failure: The name server was unable to process this query due to a problem with the nameserver. |
| xx | xx | xx | 03 | DNS_CLIENT | Name Error: Meaningful only for responses from an authoritative name server, this code signifies that the domain name referenced in the query does not exist |
| xx | xx | xx | 04 | DNS_CLIENT | Not Implemented: The name server does not support the requested kind of query |
| xx | xx | xx | 05 | DNS_CLIENT | Refused: The name server refuses to perform the specified operation for policy reasons |
| xx | xx | xx | 06 | DNS_CLIENT | YXDomain: Name Exists when it should not |
| xx | xx | xx | 07 | DNS_CLIENT | YXRRSet. RR: Set Exists when it should not |
| xx | xx | xx | 08 | DNS_CLIENT | Nxrrset. RR: Set that should exist does not |
| xx | xx | xx | 09 | DNS_CLIENT | Server Not Authoritative for zone |
| xx | xx | xx | 0A | DNS_CLIENT | Name not contained in zone |
