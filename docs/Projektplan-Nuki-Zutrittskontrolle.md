# Projektplan: Elektronische Zutrittskontrolle mit Nuki

**Version:** 1.2 · **August 2026** · Zur Entscheidung: Bewohnerverein · München, Bayern

---

## 1. Zusammenfassung

Buchbare Zugänge (v. a. **Apartment**) schrittweise mit **Nuki Smart Lock Pro + Keypad** automatisieren, angebunden an **Anny** — ohne manuelle Schlüsselübergabe.

| | |
|---|---|
| **Vollausbau (5 Türen)** | ca. **2.000–2.500 €** einmalig |
| **Pilot (nur Apartment)** | ca. **470–550 €** (siehe Kap. 7) — **Anny bereits vorhanden** |
| **Laufende Kosten Nuki** | **0 €** (kein Nutzer-Abo) |
| **Umsetzung gesamt** | **max. 2 Monate** ab Beschluss des Vereins |

**Pilot Phase 1:** ausschließlich **Apartment** (wichtigste Buchung). **Haustür** und **Kellergang-Haupteingang** bewusst **nicht** im Pilot — Kellergang ist langfristig der geplante Gästezugang, derzeit durch **Nachbarbaustelle** ohnehin nicht nutzbar.

**Beschluss durch:** **Bewohnerverein** (nicht Eigentümer). Abnahme und fachliche Klärung mit **Postbaugenossenschaft** als Voraussetzung vor Montage (Checkliste Anhang).

---

## 2. Ausgangslage

- **Ca. 50 Parteien** im Haus; öffentliche **Anny-Buchungen** für Kellerräume und Apartment.
- **Fünf Türen:** Haustür · Veranstaltungsraum (Keller) · Musikraum · Kreativraum · Apartment (Dach).
- Zutritt heute manuell.
- **Veranstaltungsraum:** **Glastüren zum Hof** (Rettungsweg) — **kein Nuki, ohne Ausnahme** · Tür **Kellergang** (Klinke innen / Knauf außen) — geplanter **Hauptzugang für Gäste** ins Gebäude (derzeit gesperrt durch Baustelle).

**Ziele:** Automatischer Zutritt bei Buchung · mechanische Schlüssel bleiben · keine Nutzer-Abo-Kosten · DIY · Fluchtwege einhalten · **Freigabe durch den Verein**.

---

## 3. Technische Voraussetzungen und offene Punkte

Nuki sitzt **innen** am Zylinder und **dreht den eingesteckten Schlüssel** per Motor.

| Voraussetzung | Status |
|---------------|--------|
| Schlüssel **innen stecken** und vom Nuki drehbar | **Apartment:** sehr wahrscheinlich ja (normale Wohnungstür; Referenz: funktioniert in vergleichbarer Wohnung im Haus) · **Kellertüren:** **ungetestet** (nur je ein Schlüssel — Test vor Bestellung nötig) |
| Not- und Gefahrenzylinder, Nuki-Maße | Je Tür prüfen |
| **Internet / WLAN 2,4 GHz** am Montageort | Apartment: messen; ggf. Repeater |
| Glastüren VR | **Kein Nuki** |

### Kellertür nach draußen (Kellergang — künftiger Gäste-Haupteingang)

**Ist-Zustand:** Tür lässt sich **nur von außen abschließen**. Innen: **Klinke** vorhanden, Schlüssel **innen nicht drehbar**. Nach Aussage vor Ort: **Wenn von außen zugesperrt, lässt sich die Tür von innen nicht öffnen.**

| Frage | Einschätzung |
|-------|--------------|
| **Nuki möglich?** | **Nein** im Ist-Zustand (kein drehbarer Schlüssel innen). |
| **Sicherheitsmangel?** | **Muss dringend geklärt werden.** Eine Tür, die von innen **nicht** zu öffnen ist, sobald sie von außen abgeschlossen wurde, ist für **Aufenthaltsräume und Fluchtwege** höchst problematisch — im Ernstfall Gefahr der **Einsperrung**. Ob das so beabsichtigt (unüblich), ein **defekter Zylinder** oder ein **Missverständnis** (Klinke vs. Schloss), muss die **Postbaugenossenschaft** mit Fluchtwegplan klären. Bis zur Klärung: **keine Nachrüstung**, **kein Nuki**. |
| **Gästezugang** | Langfristig **Hauptweg** für Gäste — derzeit **nicht nutzbar** (Nachbarbaustelle). Pilot Apartment unabhängig davon. |

### Veranstaltungsraum — rechtliches Risiko

Der VR ist nicht nur eine „Kellerbuchung“, sondern kann rechtlich zum **Veranstaltungsort** werden:

- **Öffentliche Anny-Buchungen** → Anzeige **Art. 19 LStVG** (KVR München) für öffentliche Vergnügung.
- **Häufige / größere Veranstaltungen** (z. B. >5 Veranstaltungen/Jahr mit Eintritt o. Ä.) können **Nutzungsänderung** oder Prüfung als **Versammlungsstätte** auslösen — unabhängig von Nuki.
- **§47 VStättV** (>200 Besucher): bei max. ~50 Personen voraussichtlich **nicht** relevant; **Raumgröße / zweiter Ausgang** (ab 100 m²) dennoch prüfen.
- **Smart Lock am VR** verschärft die Sichtbarkeit des Themas nicht, löst aber **keines** der rechtlichen Fragen — **Klärung vor Ausbau Phase VR**.

**Fazit VR:** Höchstes **organisatorisches und rechtliches Risiko** im Gesamtprojekt. Glastüren: **definitiv kein Nuki.** Kellergang-Tür: erst nach Zylinder-, Fluchtweg- und **Vereinsbeschluss** + **Postbaugenossenschaft**.

---

## 4. Lösung: Nuki + Anny

- **Nuki Smart Lock Pro** innen · **Keypad 2** außen (Gast-PIN).
- **Anny** (bereits im Einsatz): zeitlich begrenzte Zugänge, Remote Open.
- **Bewohner:** mechanische Schlüssel bleiben.
- **Pilot:** nur **Apartment-Tür**; Gäste erreichen das Apartment bis auf Weiteres wie bisher (manuell / über Haustür — nicht Teil des Pilots).
- **Später:** Anny-Regeln z. B. Apartment → Kellergang-Haupteingang + Apartment; Kellerräume analog.

**Veranstaltungsraum:** Glastüren **ausgeschlossen**. Kellergang-Tür nur nach Checkliste (Anhang).

---

## 5. Warum nicht die Alternativen?

| System | Hauptgrund Ablehnung |
|--------|---------------------|
| **KleverKey** | Laufende Kosten pro Nutzer — bei **~50 Parteien** und vielen Gästen an der Haustür teuer; Zylinderersatz |
| **UniFi Door Access** | Gewerbe, Verkabelung, kein Zylinder-Nachrüstsatz, keine Anny-Integration — Overkill |
| **Tapkey** | Nutzerpakete — ähnliche Kostenskala wie KleverKey |
| **EVVA AirKey** | Fachbetrieb, KeyCredits, schlecht für Anny-Gast-PINs |
| **dormakaba Exivo** | Intransparent, Fachbetrieb, Service-Abo |
| **Salto** | Hotel/Gewerbe, keine Anny-Anbindung |

**Nuki:** Anny-native PINs, 0 € Nutzer-Abo, Zylinder-Nachrüstung, DIY — wo Zylinder es zulässt.

---

## 6. Phasenplan (max. 2 Monate)

| Phase | Dauer | Inhalt |
|-------|-------|--------|
| **0 — Klärung** | Wk. 1–3 | Checkliste Anhang (parallel) |
| **1 — Pilot** | Wk. 2–6 | **Nur Apartment:** Nuki + Keypad, WLAN/Internet, Anny-Anbindung, Testbuchungen |
| **2 — Ausbau** | Wk. 5–8 | Haustür, Musik-, Kreativraum — nach Checkliste + Vereinsbeschluss |
| **3 — VR + Kellergang** | nach Freigabe | Nur Kellergang-Tür; **keine** Glastüren; VR-Rechtliches geklärt |
| **4 — Betrieb** | dauerhaft | Akku, Nuki-Zugänge, Ansprechpartner: [ ] |

**Meilenstein Pilot:** Apartment-Buchungen mit automatischem Zutritt (ca. 2 Wochen Probebetrieb).

---

## 7. Kosten

### Pilot (nur Apartment)

| Position | Richtwert |
|----------|-----------|
| Nuki Smart Lock Pro 5. Gen | ca. 269 € |
| Nuki Keypad 2 | ca. 150 € |
| **Internet / WLAN** (Repeater o. ä., falls nötig) | ca. 50–120 € |
| Reserve (Batterien, Kleinteile) | ca. 30 € |
| **Summe Pilot** | **ca. 470–570 €** → Budget-Vorschlag **max. 600 €** |
| Anny | **bereits gekauft** — nicht im Pilot-Budget |

### Vollausbau (Referenz, später)

| Position | Summe |
|----------|-------|
| 5× Lock Pro + 5× Keypad + Reserve | ca. 2.195 € |
| WLAN-Repeater (Keller/Dach, falls nötig) | 50–120 €/Stück |
| Nuki Nutzer-Abo | **0 €** |

Nicht enthalten: Schließer/Elektriker, Gutachten, ggf. Zylinderumbau Kellergang-Tür.

---

## 8. Rechtliches (Kurz)

| Thema | Hinweis |
|-------|---------|
| **Beschluss / Freigabe** | **Bewohnerverein** — nicht Eigentümer |
| **Abnahme Träger** | **Postbaugenossenschaft** vor Montage (Checkliste) |
| Art. 19 LStVG | Bei öffentlichen Buchungen → KVR |
| VR als Veranstaltungsort | Nutzungsänderung / Versammlungsstätte möglich — **vor VR-Ausbau klären** |
| Fluchtweg / Smart Lock | Keine Montage ohne Checkliste |
| Versicherung / DSGVO | Informieren / AV-Verträge |

---

## 9. Risiken

| Risiko | Gegenmaßnahme |
|--------|---------------|
| **VR rechtlich** Veranstaltungsort | Rechtslage klären **bevor** öffentlicher VR-Betrieb / Phase 3 |
| Kellergang-Tür: Einsperrung von innen | **Postbaugenossenschaft** + Fluchtwegplan; kein Nuki bis geklärt |
| Kellertüren: Schlüssel innen nicht drehbar | Türtest vor Bestellung |
| Kellergang als Gästeweg gesperrt (Baustelle) | Pilot Apartment trotzdem; Kellergang später |
| 200-Zugangs-Limit pro Nuki | Abgelaufene Zugänge löschen |
| WLAN / Akku | Repeater; mechanischer Schlüssel als Fallback |

---

## 10. Beschlussvorlagen (Verein)

**A — Grundsatz:** Nuki + Anny, vorbehaltlich Checkliste (Anhang) und **Beschluss des Vereins** je Ausbaustufe. ☐ Ja ☐ Nein

**B — Budget Pilot:** max. **600 €** für **Apartment** (Nuki + Keypad + Internet/WLAN). Anny außerhalb Budget (bereits vorhanden). ☐ Ja ☐ Nein ☐ Abweichend: ___ €

**C — Budget Vollausbau (optional):** max. **2.500 €** für bis zu 5 Türen nach Checkliste. ☐ Ja ☐ Nein ☐ Nur Pilot

**D — Mandat Klärung:** Projektgruppe arbeitet Checkliste bis **[Datum]** ab und berichtet dem Verein. ☐ Ja ☐ Nein

---

## Anhang — Checkliste vor Montage / Ausbau

Vom Verein beauftragt; fachliche Stellungnahmen wo angegeben.

### Organisation & Freigaben

- [ ] **Beschluss Bewohnerverein** (Grundsatz, Budget, Phase)
- [ ] **Abnahme / Zustimmung Postbaugenossenschaft** (schriftlich, pro Tür oder Gesamtkonzept)
- [ ] **Versicherung** informiert; Stellungnahme zu Smart Locks / Vermietung Apartment
- [ ] **Ansprechpartner** Projektgruppe benannt

### Fluchtweg & Sicherheit

- [ ] **Flucht- und Rettungswegplan** eingesehen; betroffene Türen dokumentiert
- [ ] **Glastüren Veranstaltungsraum:** bestätigt **kein Nuki**
- [ ] **Kellertür nach draußen (Kellergang / künftiger Gäste-Hauptweg):** Klärung mit Postbaugenossenschaft — Zylinder, **Öffnung von innen bei Abschluss von außen**, Fluchtweg; Baustellensituation
- [ ] Bei Rettungsweg-Türen: **Not- und Gefahrenfunktion** dokumentiert

### Technik je geplanter Tür

- [ ] **Türtest / Zylinder:** Schlüssel innen steckend **drehbar** (Nuki-Probekit oder Zweitschlüssel)
- [ ] Nuki-Maße (Abstand Klinke ≥ 30 mm, Schlüsselmaße)
- [ ] **Internet / WLAN 2,4 GHz** am Montageort gemessen; Repeater eingeplant falls nötig
- [ ] WLAN-Passwort / Gast-Netz für Nuki geklärt (Apartment-Pilot)

### Veranstaltungsraum — Rechtliches

- [ ] **Art. 19 LStVG:** Anzeige KVR bei öffentlichen Buchungen (Status: ☐ offen ☐ eingereicht)
- [ ] **Nutzung VR:** Gemeinschaftsraum vs. **Veranstaltungsort** — ggf. Nutzungsänderung / Genehmigung mit Postbaugenossenschaft und Bauordnung
- [ ] **Häufigkeit / Art** öffentlicher Veranstaltungen dokumentiert (>5/Jahr? Eintritt?)
- [ ] **Raumgröße** und zweiter Ausgang geprüft (relevant ab 100 m²)
- [ ] **Buchungs- und Hausordnung** angepasst (VR, Fluchtweg-Hinweise für Gäste)

### Pilot Apartment (Phase 1)

- [ ] Checkliste Technik für **nur Apartment-Tür** erfüllt
- [ ] Anny-Regel **nur Apartment** (ohne Kellergang/Haustür bis später)
- [ ] Gästeanleitung: Zugang zum Haus bis Kellergang frei **weiterhin manuell** erklärt
- [ ] Testbuchungen intern + extern; PIN-Zustellung geprüft

### Nach Pilot (vor Phase 2+)

- [ ] Ergebnis Pilot dokumentiert (Vereinsbericht)
- [ ] **Erneuter Vereinsbeschluss** für Haustür / Kellerräume / Kellergang
- [ ] Checkliste für jede weitere Tür wiederholt

---

*Entscheidungsunterlage für den Bewohnerverein — ersetzt keine rechtsverbindliche Prüfung durch Postbaugenossenschaft, Schließer oder Behörden.*
