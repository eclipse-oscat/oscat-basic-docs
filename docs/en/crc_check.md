<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## CRC_CHECK

The module CRC_CHECK was removed from the library  because the functionality can be fulfilled in their entirety, with the module CRC_GEN. Usually CRC_GEN generates a checksum which is is appended to the original message . If we now build again the checksum of the message with an attached checksum then the new checksum 0. With some specific CRC's where this is not the case, the checksum will be created once again after receive of a message. The checksum is build about all the transferred databytes without checksum and then is compared with the transmitted checksum.
