<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## MANUAL

| | |
|:---|:---|
| **Type	Function** | BOOL |
| **Input	IN** | BOOL (Input) |
| **ON** | BOOL (manual mode on) |
| **OFF** | BOOL (manual mode off) |
| **Output** | BOOL (output) |
| | MANUAL can override an input signal IN with TRUE or FALSE. |
| | The typical use of MANUAL by means of a switch with 3 positions (OFF, AUTO, ON) where the connections are OFF at OFF and On at On and AUTO of the switch remains open. |
| **The following diagram shows the possible connection of a switch with 3 positions** |  |

![manual](manual.gif)

![manual%20sample](manual%20sample.gif)

| IN | ON | OFF | Q |  |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |  |
| 1 | 0 | 0 | 1 |  |
| - | - | 1 | 0 | Manual operation position OFF |
| - | 1 | 0 | 1 | Manual operation position ON |
