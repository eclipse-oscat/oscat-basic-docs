<!--
  Copyright (c) 2026 Hans Mühlbauer, Franz Höpfinger and others.

  This program and the accompanying materials are made available under the
  terms of the Eclipse Public License 2.0 which is available at
  https://www.eclipse.org/legal/epl-2.0

  SPDX-License-Identifier: EPL-2.0
-->

## Im Bereich der Regelungstechnik werden Bausteine zum Aufbau von Reglern und Regelstrecken zur Verfügung gestellt. Soweit möglich messen die Bausteine selbst die Zykluszeit und errechnen mit der jeweils aktuellen Zykluszeit die Ausgangsveränderung. Dieses Verfahren hat gegenüber einer fest eingestellten Zykluszeit den Vorteil das Regelstrecken verschiedenster Geschwindigkeit innerhalb derselben Task verarbeitet werden können. Ein weiterer Vorteil ist die Tatsache das bei niedrig priorisierten Tasks die Zykluszeit schwanken kann und ein Regler mit fixer Zykluszeit ungenaue Ausgangswerte erzeugt. Der Anwender hat beim Einsatz sicherzustellen das die Zykluszeit der Task entsprechend den Anforderungen der Regelstrecke eingestellt ist.

Übersicht über die Regelkreiselemente: Wind-Up: Der Wind-Up Effekt betrifft alle Regler mit I-Anteil. Da reale Regler einen eingeschränkten Stellbereich haben würde der Integrator bei großen  Regelabweichungen und erreichen eines Ausgangslimits stets weiter anwachsen. Würde nach einiger Zeit der Prozesswert den Sollwert übersteigen so müsste abgewartet werden bis der Integrator seinen hohen Wert wieder abgebaut hat. Dies führt zu einem unerwünschten und ungünstigen Verhalten des Reglers. Der Regler würde für die Zeit aussetzen die der Integrator benötigt seinen hohen Wert wieder abzubauen, was um so länger wäre je länger der Regler in der Begrenzung war. Deshalb sind bei Reglern mit I-Anteil Anti Wind-Up Maßnahmen notwendig. Die einfachste Maßnahme zur Verhinderung des Wind-Up ist den Integrator bei erreichen eines Limits anzuhalten und erst bei Rückkehr in den Arbeitsbereich mit dem letzten Wert des Integrators weiterzuarbeiten. Dieses Verfahren hat allerdings den Nachteil das Veränderungen der Regelabweichung während der Ausgang an einem Limit ansteht weiterhin zu unnötig erhöhten Werten des Integrators führen können. Bausteine der Bibliothek die mit diesem Verfahren arbeiten sind mit einen W am Ende gekennzeichnet. Eine verfeinerte Anti Wind-Up Maßnahme ist ein Verfahren das den Ausgangswert des Integrators auf einen Wert begrenzt der zusammen mit den anderen Regelanteilen exakt zu dem Ausgangslimit führt. Dieses Verfahren hat den Vorteil das bei eintritt in den Arbeitsbereich der Regler ohne Zeitverzug sofort Einsatzfähig ist und reagieren kann. Bausteine der Bibliothek die mit diesem verbesserten Verfahren arbeiten sind mit einen WL am Ende gekennzeichnet.

| TYP | Name | Parameter | Übertragungsfunktion | Berechnung |
| --- | --- | --- | --- | --- |
| P | Proportionalglied | KP | KP | Y = X * KP |
| I | Integrator | KI |  | Y = Ya + X * KI *  ΔT |
| D | Differentiator | KD |  | Y = KD * ΔX / ΔT |
| PT1 | Tiefpaß 1.Ordnung | T1 | KP / ( 1 + T1s) |  |
| PT2 | Tiefpaß 2.Ordnung | T1, T2 |  |  |
| PI | PI-Glied | KP, KI | KP (1 + 1/TNs) | Y = Ya + KP ((1 + ΔT/TN)X - Xa) |
| PD | PD-Glied | KP, KD | KP (1 + TDs) |  |
| PDT1 | PD-Glied, Verzögert | KP, TV, T1 | KP (1 + TVs/(1+T1s)) |  |
| PID | PID-Glied | KP, TN, TV | KP (1 + 1/TNs + TVs |  |
| PIDT1 | PID-Glied, Verzögert | KP, TN, TV, T1 | KP (1 + 1/TNs + TVs/(1+T1s)) |  |
