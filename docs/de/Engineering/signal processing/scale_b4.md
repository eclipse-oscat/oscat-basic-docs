<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## SCALE_B4

| | |
|:---|:---|
| **Type	Funktion** | REAL |
| **Input	IN1.. IN4** | Byte (Eingangswerte) |
| **K** | REAL (Multiplikator) |
| **O** | REAL (Offset) |
| **Output** | REAL (Ausgangswert) |
| **Setup	IN1_MIN** | REAL (kleinster Wert für IN1) |
| **IN1_MAX** | REAL (größter Wert für IN1) |
| **IN2_MIN** | REAL (kleinster Wert für IN2) |
| **IN2_MAX** | REAL (größter Wert für IN2) |
| **IN3_MIN** | REAL (kleinster Wert für IN3) |
| **IN3_MAX** | REAL (größter Wert für IN3) |
| **IN4_MIN** | REAL (kleinster Wert für IN4) |
| **IN4_MAX** | REAL (größter Wert für IN4) |
| | SCALE_B4 berechnet aus den Eingangswerten IN und den Setup-Werten IN_MIN und IN_MAX interne Werte, addiert alle internen Werte, multipliziert die Summe mit K und addiert den Offset O. Ein Eingangswert IN=0 bedeutet IN_MIN wird berücksichtigt, IN=255 bedeutet IN_MAX wird berücksichtigt. Wird K nicht beschaltet, so ist der Multiplikator 1. |
| **OUT** | = (in1 * (IN1_MAX – IN1_MIN) / 255 + IN1_MIN |
| | + in2 * (IN2_MAX – IN2_MIN) / 255 + IN2_MIN |
| | + in3 * (IN3_MAX – IN3_MIN) / 255 + IN3_MIN |
| | + in4 * (IN4_MAX – IN4_MIN) / 255 + IN4_MIN) * K + O |
| | SCALE_B4 kann zum Beispiel verwendet werden um Gesamtluftmengen in Lüftungsanlagen zu berechnen, oder überall dort, wo gesteuerte Mischer eingesetzt werden und die resultierende Gesamtmenge berechnet werden muss. Weitergehende Erläuterungen zur Funktionsweise finden Sie auch unter SCALE_B2. |

![scale_B4](scale_b4.gif)
