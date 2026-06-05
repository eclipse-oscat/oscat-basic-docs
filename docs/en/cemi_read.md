<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## CEMI_READ

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	PT** | Pointer  (Pointer to the array) |
| **SIZE** | UINT (size of the array) |
| **Output** | BOOL (TRUE) |
| | CEMI_READ divides a cemi_frame ... |
| | TheKNXnet/IP Protokollstack |
| **The structure of the Protokoll Layers is** |  |
| | Ethernet II Frame |
| | IPv4 Packet |
| **UDP Packet** |  |
| **EIBnet/IP Packet** |  |
| **Service Type** |  |
| **cEMI Packet** |  |
| | cEMI is a „common External Message Interface“ |
| **Message Codes from Network Layer to Data Link Layer** |  |
| **Message Codes from Data Link Layer to Network Layer** |  |
| **Control Byte** |  |
| | The BIT ACK_REQ defines if an acknowledge is required, TRUE means ACK is required. The CONFIRM BIT defines if an ERROR is set, TRUE means ERROR. The REPEAT Bit is TRUE if a message is sent once, at repeatings this Bit is FALSE. |
| **Priority** |  |
| **DRL Byte** |  |
| | Destination Address Flag = TRUE, destination address is group address |
| | Destination Address Flag = FALSE, destination address is physical address |
| | The routing counter defines how often a telegram  is routed on line or area router. 0 means no forwarding, 7 means any routing. At every routing the counter is decreased by one. |
| | The length of the payload determines the amount of user data, 0 means 1 byte and 15 is 16 bytes. |
| **Source Address** |  |
| **Destination Address (group address, dest. Adr. Flag = TRUE)** |  |
| | The group address can be divided into 2 or 3 levels. |
| **Destination Address (physical address, dest. Adr. Flag = FALSE)** |  |
| | The bytes of 9..10 cEMI include the 2-bit long TPCI, 4 bits packet number at numbered control- or data packets, followed by APCI with data. |
| **The TPCI (transport layer protocol information)** |  |
| **00 =** | not numbered data packets UDT |
| | i.e. group telegram |
| **01 =** | numbered data packets NDT |
| **10 =** | not numbered controll data UCD |
| **11 =** | numbered controll data NCD |
| | The Packet Counter passes at NCD and NDT the number of the data packet. |
| **The APCI (application layer protocol information)** |  |

![_array_abs](_array_abs.gif)

![Object 1](Object 1)

| Präambel | SFD | Target MAC Address | Source MAC Address | Typ Field | IPv4 Packet | PAD | CRC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Byte 0..6 | B7 | B8..13 | B14..19 | B20..21 | Min 46 Bytes | 1B | 4B |
| 7 * 55 | D5 |  |  | 0800
(IPV4) |  | 1B | CRC |

| Ver/IHL | TOS | Total Length | ident | Flags Offset | TTL | Protocol | Header Checksum | Source Address | Destination Addres | UDP
Packet |

| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Byte 0 | B 1 | B 2..3 | B4..5 | B6..7 | B 8 | B 9 | B 10..11 | B12..15 | B 16..19 |  |
| 45 | 0 |  |  |  |  | 11 (UDP) |  |  |  |  |

| Source Port | Target Port | Length | Checksum | EIBnet/IP Packet |
| --- | --- | --- | --- | --- |
| B 0..1 | B 2..3 | B4..5 | B6..7 | B 8... |
|  |  |  |  |  |

| Header length | Version | Service Type (Routing) | length | CEMI Packet |
| --- | --- | --- | --- | --- |
| B 0 | B 1 | B2..3 | B4..5 |  |
| 06 | 10 | 0530 |  |  |

| 0201 | Search request |  |
| --- | --- | --- |
| 0202 | Search response |  |
| 0203 | Description request |  |
| 0204 | Description response |  |
| 0205 | Connect request |  |
| 0206 | Connect response |  |
| 0207 | Connection state request |  |
| 0208 | Connection state response |  |
| 0209 | Disconnect request |  |
| 020A | Disconnect response |  |
| 0310 | Device configuration request |  |
| 0311 | Device configuration Ack |  |
| 0420 | Tunneling Request |  |
| 0421 | Tunneling ACK |  |
| 0530 | Routing Indication |  |
| 0531 | Routing lost message |  |

| Message Code | Addl length | Control Byte | DRL Byte | Source Address | Dest. Address | Data Length | TPCI APCI | APCI / Data |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B 0 | B 1 | B 2 | B 3 | B 4..5 | B 6..7 | B 8 | B 9 | B10... |
|  |  | BC |  |  |  |  | 00 |  |

| 10 | Raw Request |  |
| --- | --- | --- |
| 11 | Data Request | Transmitting a Data Frame |

| 13 | Poll Data Request |  |
| --- | --- | --- |
| 25 | Poll Data Service |  |
| 29 | Data Service |  |
| 2B | Busmonitor Service |  |
| 2D | RAW Service |  |
| 2E | Data Service |  |
| 2F | RAW Con? |  |

| Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | Repeat | 1 | Priority | ACK_REQ | CONFIRM |

| 00 | System Function |
| --- | --- |
| 01 | Alarm Function |
| 10 | High Priority |
| 11 | Normal priority |

| B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dest.
Address Flag | Routing Counter | Lengths of usable data in bytes |

| B15 | B14 | B13 | B12 | B11 | B10 | B9 | B8 | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area | Linie | participant |

| B15 | B14 | B13 | B12 | B11 | B10 | B9 | B8 | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | main group | middle group | subgroup |
| 0 | main group | subgroup |

| B15 | B14 | B13 | B12 | B11 | B10 | B9 | B8 | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Area | Linie | participant |

| B15 | B14 | B13 | B12 | B11 | B10 | B9 | B8 | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TPCI | Packet Counter | APCI | first databyte |

| APCI | Data 5..0 | action |  |
| --- | --- | --- | --- |
| 0000 | 000000 | value request | READ_VALUE_REQUEST |
| 0001 | Value | value answer after request | READ_VALUE_RESPONSE |
| 0010 | Value | Value send without request | WRITE_VALUE_REQUEST |
| 0011 | 000000 | set physical address | SET_PA_REQUEST |
| 0100 | 000000 | request physical address | READ_PA_REQUEST |
| 0101 | 000000 | answer to phys. adress request | READ_PA_RESPONSE |
| 0110 |  | analogue value request | READ_ADC_REQUEST |
| 0111 |  | analogue value receive | READ_ADC_RESPONSE |
| 1000 | 00xxxx | memory request CC | READ_CCMEM_REQUEST |
| 1001 | 00xxxx | memory answer CC | READ_CCMEM_RESPONSE |
| 1010 | 00xxxx | memory write CC | WRITE_CCMEM_REQUEST |
| 1011 | 000000 | memory request AC | READ_ACMEM_REQUEST |
| 1011 | 000001 | memory answer AC | READ_ACMEM_RESPONSE |
| 1011 | 000010 | memory write AC | WRITE_ACMEM_REQUEST |
| 1011 | 000011 | memory write bit by bit AC | WRITE_ACMBIT_REQUEST |
| 1011 | 000100 | manufacturer Info query | READ_MINF_REQUEST |
| 1011 | 000101 | manufacturer info response | READ_MINF_RESPONSE |
| 1011 | 111xxx | manufacturer internal area |  |
| 1100 | 000000 | mask revision request | READ_MVER_REQUEST |
| 1101 | 000000 | mask revision response | READ_MVER_RESPONSE |
| 1110 | 000000 | CC restart | RESTART_REQUEST |
| 1111 | 010000 | write CC memory bit | WRITE_CCMBIT_REQUEST |
| 1111 | 010001 | authorize level request (permission) | AUTHORIZE_REQUEST |
| 1111 | 010010 | authorize level response | AUTHORIZE_RESPONSE |
| 1111 | 010011 | authorize key set | SET_KEY_REQUEST |
| 1111 | 010100 | authorize key response | SET_KEY_RESPONSE |
| 1111 | 010101 | property value request | READ_PROPVAL_REQUEST |
| 1111 | 010110 | response to property value request | READ_PROPVAL_RESPONSE |
| 1111 | 010111 | property value write | WRITE_PROPVAL_REQUEST |
| 1111 | 011000 | property description request | READ_PROPDES_REQUEST |
| 1111 | 011001 | property description response | READ_PROPDES_RESPONSE |
| 1111 | 011100 | physical address of ser no | READ_PA_SER_REQUEST |
| 1111 | 011101 | response to request of SER_REQ | READ_PA_SER_RESPONSE |
| 1111 | 011110 | set phys. address for ser. no. | SET_PA_SERNO_REQUEST |
| 1111 | 011111 | request of service state | SERVICE_INFO_REQUEST |
| 1111 | 100000 | set system id | SET_SYSID_REQUEST |
| 1111 | 100001 | request of system id | READ_SYSID_REQUEST |
| 1111 | 100010 | response to system id request | READ_SYSID_RESPONSE |
