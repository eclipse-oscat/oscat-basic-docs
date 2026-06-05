<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktion

| | |
|:---|:---|
| **Input	IN** | REAL (Eingangswert) |
| **Output** | DWORD (Ausgangswort zum A/D Wandler) |
| **Setup	BIT_0** | INT (Stelle des niederwertigesten Bits des Datenwortes) |
| **BIT_N** | INT (Stelle des höchstwertigsten Bits des Datenwortes) |
| **SIGN** | INT (Sign Bit, 15 für Bit 15) |
| **LOW** | REAL (kleinster Wert des Eingangs) |
| **HIGH** | REAL (größter Wert des Eingangs) |
| | AOUT1 erzeugt aus dem REAL Eingangswert IN einen digitalen Ausgangswert für D/A Wandler oder andere Ausgangsbausteine die Digitale Daten verarbeiten. Mittels Setup Variablen kann der digitale Ausgangswert an verschiedenste Bedürfnisse angepasst werden. Der Eingangswert IN wird mittels den Angaben in LOW und HIGH sowie der mit BIT_0 und BIT_N spezifizierten Länge Des Datenwortes umgewandelt und am Ausgang bereitgestellt. BIT_0 spezifiziert die Position des niderwertigsten (Bit0) Datenbits in den Ausgangsdaten und BIT_N spezifiziert die Position des höchstwertigen Datenbits in den Ausgangsdaten. Die Länge des Datenbereichs wird durch BIT_N - BIT_0 + 1 automatisch errechnet. Wenn mit SIGN die Position eines Vorzeichen Bits angegeben wird so wird das Vorzeichen aus dem Eingangswert auf die spezifizierte Position von SIGN in den Ausgangsdaten kopiert. |

![aout1](aout1.gif)

![aout1_config](aout1_config.gif)
