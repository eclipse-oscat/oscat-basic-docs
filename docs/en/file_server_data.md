<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## FILE_SERVER_DATA

FILE_SERVER data structure:

| Name | Type | Properties |
| --- | --- | --- |
| File_open | BOOL | File is open |
| FILE NAME | STRING | File Name |
| MODE | BYTE | Mode - command |
| OFFSET | UDINT | File offset for reading and writing |
| FILE_SIZE | UDINT | Current size of the file in bytes |
| AUTO_CLOSE | TIME | Timing for the automatic closure |
| ERROR | BYTE | Error codes (system dependent) |
