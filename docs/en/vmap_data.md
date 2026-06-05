<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## VMAP_DATA

VMAP_DATA data structure:

| Name | Type | Properties |
| --- | --- | --- |
| FC | DWORD | function code: release bit mask |
| V_ADR | INT | Virtual Address Range: Start address |
| V_SIZE | INT | Virtual address space: number of WORD |
| P_ADR | INT | Real address space: Start address |
| TIME_OUT | TIME | Watchdog |
