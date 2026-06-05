<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Type	Funktionsbaustein

| | |
|:---|:---|
| **Input	IN** | DWORD (Eingang vom A/D Wandler) |
| **Output	OUT** | REAL (Ausgangswert) |
| **SIGN** | BOOL (Vorzeichen) |
| **ERROR** | BOOL (Error Bit) |
| **OVERFLOW** | BOOL (Overflow Bit) |
| **Setup	SIGN_BIT** | INT (Bitnummer des Vorzeichens) |
| **ERROR_BIT** | INT (Bitnummer des Fehlerbits) |
| **ERROR_CODE_EN** | BOOL (Auswertung des Error Codes Ein) |
| **ERROR_CODE** | DWORD (Fehlercode des Eingangs IN) |
| **OVERFLOW_BIT** | INT (Bitnummer des Overflow Bits) |
| **OVERFLOW_CODE_EN** | BOOL (Overflow Codes Auswertung Ein) |
| **OVERFLOW_CODE** | DWORD (Overflow Code des Eingangs IN) |
| **BIT_0** | INT (Bitnummer des niederwertigsten Datenbits) |
| **BIT_N** | INT (Bitnummer des höchstwertigsten Datenbits) |
| **OUT_MIN** | REAL (Ausgangswert bei CODE_MIN) |
| **OUT_MAX** | REAL (Ausgangswert bei CODE_MAX) |
| **CODE_MIN** | DWORD (Minimaler Eingangswert) |
| **CODE_MAX** | DWORD (Maximaler Eingangswert) |
| **ERROR_OUTPUT** | REAL (Ausgangswert der bei ERROR) |
| **OVERFLOW_OUTPUT** | REAL  (Ausgangswert der Bei OVERFLOW) |
| | AIN1 setzt den Digitalen Ausgangswert eines A/D Wandlers in einen dem Messwert entsprechenden REAL Wert um. Der Baustein kann mittels Setup Variablen auf die unterschiedlichsten Digitalwandler angepasst werden. |
| | Ein SIGN_BIT legt fest an welchen Bit der D/A Wandler das Vorzeichen übermittelt. Wird diese Variable nicht definiert oder auf einen Wert größer 31 gesetzt so wird kein Vorzeichen ausgewertet. Der Inhalt des SIGN_BIT wird am Ausgang SIGN angezeigt. Wird ein ERROR_BIT spezifiziert, wird der Inhalt des Error Bits am Ausgang ERROR angezeigt. Manche A/D Wandler liefern anstatt eines Error Bits einen festgelegten Ausgangswert der außerhalb des spezifizierten Messbereichs liegt und Signalisieren dadurch einen Fehler. Mit der Setup Variablen ERROR_CODE wird der entsprechende Error Code spezifiziert und mit ERROR_CODE_EN wird die Auswertung des ERROR_CODE Festgelegt. Wenn ERROR = TRUE wird am Ausgang OUT der Wert  ERROR_OUTPUT ausgegeben. Mithilfe des OVERFLOW_BITS wird eine Bereichsüberschreitung des D/A Wandlers signalisiert und am Ausgang OVERFLOW ausgegeben. Mithilfe der Setup Variablen OVERFLOW_CODE_EN und OVERFLOW_CODE kann ein bestimmter Code am Eingang IN abgefragt werden und bei Auftreten dieses Codes das Overflow Bit gesetzt werden. Zusätzlich zum OVERFLOW_BIT kann mittels CODE_MIN und CODE_MAX ein zulässiger Bereich für die Eingangsdaten spezifiziert werden. Wird dieser Bereich über- beziehungsweise unter-schritten wird ebenfalls der OVERFLOW Ausgang gesetzt. Bei einem Überlauf wird am Ausgang OUT der Wert OVERFLOW_OUTPUT ausgegeben. Die Setup Variablen BIT_0 und BIT_N legen fest wie der D/A Wandler den Messwert  Bereitstellt. Mit Bit_0 wird festgelegt bei welchem Bit das Datenwort beginnt und mit BIT_N an welchem Bit das Datenwort endet. Im obigen Beispiel wird das Datenwort von Bit 3 bis Bit 14 übertragen (Bit 3 = Bit 0 des Datenwortes und Bit 14 = Bit 12 des Datenwortes). Das empfangene Datenwort wird entsprechend den Setup Variablen CODE_MIN, CODE_MAX und OUT_MIN, OUT_MAX umgerechnet und falls ein Vorzeichen vorhanden ist wird wenn SIGN = TRUE der Ausgangswert an OUT invertiert. |

![ain1](ain1.gif)

![ain1_config](ain1_config.gif)
