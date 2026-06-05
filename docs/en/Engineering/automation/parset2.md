<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## PARSET2

| | |
|:---|:---|
| **Type** | Function module |
| **Input	X** | REAL (input) |
| **Output	P1** | REAL (parameter 1 out) |
| **P2** | REAL (Parameter 2 Output) |
| **P3** | REAL (Parameter 3 Output) |
| **P4** | REAL (Parameter 4 Output) |
| | Parset selects from up to 4 sets of parameters one and returns the values at the outputs P1 to P4. The values for the parameter sets are defined with the setup variables. If the TC setup variable to a value > 0 is set, the outputs do not change abruptly to a new value, but run in a ramp   to the new value so that the final value is reached after time TC. This allows the smooth transition between different sets of parameters. The choice of parameters is the controlled variable X and the thresholds L1 to L3 set. |
| **Setup	X01, X11, X21, X31** | REAL (values for parameters P1) |
| **X02, X12, X22, X32** | REAL (values for parameters P2) |
| **X03, X13, X23, X33** | REAL (values for parameters P3) |
| **X04, X14, X24, X34** | REAL (values for parameters P4) |
| **L1, L2, L3** | REAL (  Limits  for the parameter switching |
| **TC** | TIME (ramp time at the outputs P) |

![parset2](parset2.gif)

| X | P1 | P2 | P3 | P4 |
| --- | --- | --- | --- | --- |
| X < L1 | X01 | X02 | X03 | X04 |
| L1 < X < L2 | X11 | X12 | X13 | X14 |
| L2 < X < L3 | X21 | X22 | X23 | X24 |
| X >= L3 | X31 | X32 | X33 | X34 |
