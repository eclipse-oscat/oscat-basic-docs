<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Function module

| | |
|:---|:---|
| **Input	ENABLE** | BOOL (enable input) |
| **MIN_TIME_MS** | TIME (Minimum cycle time) |
| **MAX_TIME_MS** | TIME (maximum cycle time) |
| **TP_Q** | TIME (pulse width of the output pulse to XQ) |
| **Output	XQ** | BOOL (binary output) |
| | GEN_RDT generates pulses with a defined pulse width and random spacing. The output pulses with the pulse width TP_Q be generated at random intervals TX. TX fluctuates randomly between time MIN_TIME_MS and MAX_TIME_MS. The module generates output pulses at XQ only when the ENABLE input is TRUE. |

![gen_rdt](gen_rdt.gif)
