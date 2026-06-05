<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SPIDER_ACCESS

| | |
|:---|:---|
| **Type	Function module** |  |
| **IN_OUT	IP_C** | IP_C (parameterization) |
| **S_BUF** | NETWORK_BUFFER (transmit data) |
| **R_BUF** | NETWORK_BUFFER (receive data) |
| **VALUE** | STRING   (Value of the variable) |
| **NAME** | STRING(40)   (Variable Name) |
| **INPUT	MODE** | BYTE (operating mode: 1 = read / write = 2) |
| **ERROR	ERROR** | DWORD   (Error code) |
| **ERROR** |  |
| **With SPIDER_ACCESSvariables can be read wnd written from the PLC, which are provided by visualizations of web servers based on "spider control" from the company iniNet integrated Solution GmbH,   

For the following PLC is this web server integration available** |  |

| | Simatic S7 200/300/400 
SAIA-Burgess PCD 
Wago (750-841)
Beckhoff (CX series)
Phoenix Contact (ILC Reihe)
Selectron
Berthel
Tbox
Beck IPC |

| | In the PLC program of target PLC, the desired variables must be released for web access. Since the communication is performed via HTTP (port 80), the data exchange is no problem, even across firewalls. Global and instance variables can be processed. |
| **Format of variables** |  |
| | At global variables, only the regular variable names has to be given. An instance variable must be specified below. 
"instance name. variable name" |

| **Mode** | Read |
| | If the MODE parameter is set to "1" and the variable name is quoted in "NAME", so cyclically a request to the HTTP to Web Server (PLC) is  performed and the result is displayed the "VLAUE" as a string. |
| **Mode** | Write |
| | If the parameter MODE is set to "2" and at "VALUE" the variable value and in "NAME" the variable name as string, then cyclically an HTTP request to the Web Server (PLC)   is performed |
| | The mode resp. the variable name can be changed in the cyclic mode at any time. If several variables have to be processed, thus only a many module instances as needed must be called. |

![spider_access](spider_access.gif)

| Value | Properties |
| --- | --- |
| 1 | At writing variable values an error occured. |
| > 1 | The exact meaning of ERROR is read at module HTTP_GET |
