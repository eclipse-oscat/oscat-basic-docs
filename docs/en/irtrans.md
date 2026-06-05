<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## The module IRTRANS_? provide an interface for infrared  Transmitter  Company IRTrans GmbH. IRTrans offers  transmitter  for RS232 and TCP/IP, all of which can be operated with the following driver components. The basic connection to RS232 or TCP/IP must be made with the appropriate manufacturer routines. The interface modules rely on a  Buffer Interface  to which provides in a  Buffer  (Array  of  Byte) data and in a  Counter  the length of the data packet in bytes. The  IRTrans devices learn the IR key codes and translate them in ASCII  Strings using a configurable database. With the Ethernet variant, this  Strings  then sent over UDP and can be received from a PLC and be evaluated. Thus, for example, the blinds are automatically  shut down when someone turns on the TV without this additional action would be necessary. The PLC can listen in this manner any number of remote controls in different areas and derive appropriate actions from it. Conversely, of course, the release of key codes on the  Transmitter  modules is possible.
