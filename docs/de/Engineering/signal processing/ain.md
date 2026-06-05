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
| **Input	IN** | DWORD (Eingang vom A/D Wandler) |
| **Output** | REAL (Ausgangswert) |
| **Setup	BITS** | Byte (Anzahl der Bits, 16 für ein komplettes Wort) |
| **SIGN** | Byte (Sign Bit, 15 für Bit 15) |
| **LOW** | REAL (kleinster Wert des Ausgangs) |
| **HIGH** | REAL (größter Wert des Ausgangs) |
| | Analoge Eingänge von A/D Wandlern liefern in der Regel ein WORD (16 Bit) oder DWORD (32 Bit), wobei sie selbst meist nicht 16 Bit oder 32 Bit Auflösung besitzen. Weiterhin digitalisieren A/D Wandler einen festen Eingangsbereich (z B. -10 .. + 10 V), was zum Beispiel mit den digitalen Werten 0 .. 65535 (Bei 16 Bit) repräsentiert wird. Die Funktion AIN wird durch Setup-Parameter Konfiguriert und rechnet die Ausgangswerte des A/D Wandlers entsprechend um, sodass nach dem Modul AIN ein REAL-Wert zur Verfügung steht, der mit dem echten gemessenen Wert übereinstimmt. Weiterhin kann das Modul ein Sign-Bit an beliebiger Stelle extrahieren und umrechnen. Durch einen Doppelklick auf den Baustein können mehrere Setup-Variablen gesetzt werden. Bits definiert wie viele Bits des Eingangs-DWORD verarbeitet werden sollen. Für einen 12 Bit Wandler ist dieser Wert 12. Es werden dann nur die Bits 0 – 11 ausgewertet. Sign definiert, ob ein Vorzeichenbit vorhanden ist und wo im Eingangswort es zu finden ist. Sign=255 bedeutet, dass kein Vorzeichenbit vorhanden ist und 15 bedeutet, dass Bit 15 im DWORD das Vorzeichen enthält. Der Vorgabewert für SIGN ist 255. LOW und HIGH definieren den kleinsten und höchsten Ausgangswert. Ist ein Sign-Bit definiert (SIGN < 255), dann müssen LOW und HIGH positiv sein. Ohne Sign-Bit können Sie sowohl positiv als auch negativ sein. |

![ain](ain.gif)

**Beispiel:**

Beispiel: Ein 12 Bit A/D Wandler ohne Vorzeichen und Eingangsbereich 0 – 10 wird wie folgt definiert: Bits=12, Sign=255, LOW=0, HIGH=10. Ein 14 Bit A/D Wandler mit Vorzeichen in Bit 14 und Eingangsbereich -10 - +10 wird folgendermaßen definiert: Bits=14, Sign=14, LOW=0, HIGH=+10. Ein 24 Bit A/D Wandler ohne Vorzeichen und Eingangsbereich -10 - +10 wird folgendermaßen definiert: Bits=24, Sign=255, LOW=-10, HIGH=+10.
