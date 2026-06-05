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
| **Input	E** | BOOL (  Enable  Input,  Default  = TRUE) |
| **X** | REAL (input) |
| **K** | REAL (Integration value in 1/s) |
| **I / O	Y** | REAL ( IntegratorOutput) |
| | INTEGRATE is a  Integrator which integrates the value of X to an external value Y. The integrator operates when E = TRUE, the internal  Default  of E = TRUE. |

![integrate](integrate.gif)
