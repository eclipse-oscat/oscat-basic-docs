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
| **Input	START** | BOOL (input) |
| **STOP** | BOOL (input) |
| **TMAX** | TIME (Timeout für ET) |
| **RST** | BOOL (Reset input) |
| **Output	PT** | TIME (elapsed time) |
| **ET** | TIME (Elapsed time since last rising edge) |
| **RUN** | BOOL (TRUE if measure processes) |
| **M_D measures the time  between  a rising edge of START and a rising edge on STOP. PT is the result of the last measurement. Output ET is the elapsed time since the last rising edge of START. M_d requires a rising edge to start the measurement. If at the first call already START is TRUE, it is not seen as a rising edge. Even if STOP is TRUE, a rising edge of START is not counted. Only when all start conditions (STOP = FALSE, RST** | = FALSE and rising edge at START) are present, the output RUN gets TRUE and a measurement is started. With TRUE at the input RST, the outputs can always be reset to 0. If ET reaches the value of TMAX, automatically a reset is generated in the module to reset all outputs to 0. TMAX is internally assigned with default value of T#10d and normally can be unconnected. TMAX serves to define a maximum value range for PT. The output RUN is TRUE if is a measurement is processed. |

![m_d](m_d.gif)
