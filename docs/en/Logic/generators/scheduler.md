<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SCHEDULER

| | |
|:---|:---|
| **Type** | Function module |
| **Input	E0..3** | BOOL (release signal for Q0..3) |
| **Output	Q0..3** | BOOL (output signals) |
| | SCHEDULER is used to call time dependent program parts. For example, complex calculations that are needed only rarely, can be called at fixed intervals. The outputs Q? of the module will be active only for one cycle and release the execution of the program part. The setup time T? specify at which intervals the outputs are enabled. SCHEDULER checks per CPU cycle only one output, so that in maximum one output per cycle  can be active. In the extreme case when all call times T? are T#0s, in each cycle one output should be set, so that first Q0, then Q1, etc. to Q3 are set and then again to start Q0. The call times can therefore up to 3 CPU cycles and differ from the predetermined value T? . |
| **Setup	T0..3** | TIME (cycle time) |

![scheduler](scheduler.gif)
