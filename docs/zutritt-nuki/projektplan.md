# Projektplan: Elektronische Zutrittskontrolle mit UniFi Access

**Version:** 2.0 · **September 2026** · Zur Entscheidung: Bewohnerverein · München, Bayern (Arnulfstr. 55)

→ [Übersicht aller Unterlagen](README.md) · Checkliste: [checkliste.md](checkliste.md) · Treffen PostBG: [gespraechsprotokoll-groepke-2026-09-22.md](../gespraechsprotokoll-groepke-2026-09-22.md)

---

## 1. Zusammenfassung für die Entscheidung

Wir schlagen vor, buchbare Zugänge schrittweise mit **UniFi Door Access** zu automatisieren und an **Anny** anzubinden. An den **fünf vom Postbau vorverdrahteten Türen** (CAT7, elektrischer Türöffner, Kasten) steuert UniFi den **bestehenden Summer** — Zylinder, Schlüssel und **Klinke innen** bleiben mechanisch erhalten.

| | |
|---|---|
| **System** | **UniFi Access** (Leser mit PIN, Door Hub, Konsole/Gateway) |
| **Pilot** | **Eine Testtür** — vorgesehen: **Apartment** (5. OG, vorverdrahtet) |
| **Einbau Pilot** | **Tobias Schüle** (Verein); PostBG hat Einbau **ohne Fachbetrieb** mit abgesegnet |
| **Postbaugenossenschaft** | Plan am **22.09.2026** von **Herrn Gröpke** (Vorstand) **freigegeben** (inkl. versicherungstechnischer Folgen) |
| **Verein** | **Beschluss ausstehend** — Grundsatz, Budget Pilot, Mandat Klärung |
| **Vollausbau (5 Türen)** | Hardware grob **~1.700–1.900 €** + Konsole/PoE; Details Kap. 7 · [nuki-vs-unifi.md](../nuki-vs-unifi.md) |
| **Pilot-Budget (Richtwert)** | **~800–1.200 €** (1× Tür + Gateway/Konsole, PoE, Reserve; Internet-Lösung extra) |
| **Laufende Kosten UniFi** | Kein Nutzer-Abo; Anny Professional separat (bereits im Einsatz) |

**Elektrik (Kurz):** Kein **neuer 230-V-Zuleitungsbau** bis zur Tür; Hub/Leser über **bestehendes CAT7 + PoE(PoE++)**. Der **Anschluss Hub ↔ Türöffner** ist ein elektrischer Eingriff am Öffner — vor Inbetriebnahme Öffner-Typ, Fail-Verhalten und Fluchtweg **pro Tür** prüfen (Checkliste).

**Offene Punkte vor Pilot:** **Internet im Apartment** für Konsole/Anny **ohne zweiten Vertrag**; Hardware-Stückliste für die Testtür finalisieren und bestellen.

**Beschluss wird erbeten zu:** Grundsatz UniFi + Anny (Antrag A), Budget Pilot (Antrag B), optional Vollausbau-Obergrenze (Antrag C), Mandat Klärung (Antrag D).

---

## 2. Ausgangslage und Ziele

### 2.1 Haus und Nutzer

- **56 Wohneinheiten**, Bewohnerverein betreibt **Anny** (Apartment, Musik-, Kreativ-, Veranstaltungsraum).
- **Träger Gebäude:** Postbaugenossenschaft (Fluchtweg, Vorhaltung, Versicherung Gebäude).
- Zutritt heute **manuell** (Schlüssel, Aufschließen).

Details Türen: [kontext-gebaeude.md](kontext-gebaeude.md), Fluchtwege: [analyse-fluchtwege.md](analyse-fluchtwege.md).

### 2.2 Fünf vorverdrahtete Türen (UniFi-Zielbild)

| Tür | Lage | Rettungsweg | Planung |
|-----|------|-------------|---------|
| **Apartment** | 5. OG | 1. RW Wohnung | **Phase 1 — Testtür** |
| **Musikraum** | UG | 1. RW | Phase 2 nach Pilot |
| **Kreativraum** | UG | 1. RW | Phase 2 nach Pilot |
| **Veranstaltungsraum** (Innentür Flur) | UG | T30-RS, bis 100 Pers. | Phase 3 nach Freigabe |
| **Kellergang → Hof** | UG | kein RW laut PostBG | Phase 3; Zylinder/Einsperrung klären |
| **Glastüren VR → Hof** | — | **Rettungsweg** | **Keine** Elektronik |
| **Haustür EG** | — | — | **Nicht** vorverdrahtet — nicht im UniFi-Pilot |

**Kellergang als Gäste-Hauptweg** ist wegen **Nachbarbaustelle** derzeit gesperrt; Apartment-Pilot unabhängig möglich.

### 2.3 Ziele

1. **Automatischer Zutritt** bei Anny-Buchung (PIN in Mail, App, ggf. Remote Open).
2. **Mechanische Schlüssel** und **Klinke innen** bleiben.
3. **Vorhandene Postbau-Vorhaltung** nutzen (Ethernet + Türöffner).
4. **Kein Nuki-200er-Limit** pro Schloss; skaliert besser für viele Buchungsgäste.
5. **Fluchtwege** einhalten; **keine** Smart Locks an VR-Glastüren.
6. **Entscheidung Verein**; fachliche Abstimmung PostBG — für den beschriebenen Pilot **bereits erfolgt** (Gröpke).

### 2.4 Warum UniFi — und warum nicht Nuki / andere

Ausführlich: [vergleich-nuki-unifi.md](vergleich-nuki-unifi.md), [systemvergleich-alternativen.md](systemvergleich-alternativen.md), [nuki-vs-unifi.md](../nuki-vs-unifi.md).

| System | Kurzfassung |
|--------|-------------|
| **UniFi Access (gewählt)** | Passt zu **CAT7 + Summer**; **Anny nativ**; PIN am Leser (z. B. Reader Flex); **PoE**, kein Tür-Akku; Klinke/Schlüssel unverändert. PostBG-Freigabe für Pilot. |
| **Nuki Pro + Keypad** | Gute **DIY-Zylinder**-Lösung, Anny nativ — nutzt unsere **Vorhaltung nicht**; **200 künftige Zugänge/Schloss**; Kellertüren oft **Zylinder-Problem** (Schlüssel innen nicht drehbar); WLAN an jeder Tür nötig. Nicht mehr Projektlinie nach PostBG-Termin. |
| **KleverKey / Tapkey** | Laufende **Nutzerkosten** bei vielen Berechtigungen. |
| **Salto / Exivo / AirKey** | Fachbetrieb, Abos/Credits, falsche Kategorie oder Anny-Gäste ungünstig. |

**Entscheidungsgrundlage:** Vor-Ort-Termin und Mail PostBG (Vorhaltung, Panik, Kellergang kein Fluchtweg) plus interner Vergleich — siehe [plan-zutritt-nuki-unifi.md](../plan-zutritt-nuki-unifi.md).

---

## 3. Technisches Konzept

### 3.1 Komponenten (Pilot und Ausbau)

- **UniFi-Konsole** mit UniFi-Access-Fähigkeit (z. B. **Cloud Gateway Max** — nicht Ultra).
- **Door Hub Mini** (1 Tür pro Hub) im Türkasten, **PoE++** über **CAT7**.
- **Leser mit PIN** (z. B. **UA-G2-Pro** / Reader Flex) — für Anny-Gäste praktisch **Pflicht**.
- **Anbindung** an **bestehenden elektrischen Türöffner** (gleicher Impuls wie Summer/Klingel).
- **Anny** — [UniFi-Integration](https://anny.co/integrations/unifi-door-access); zeitlich begrenzte Zugänge.

Software im Repo: [`freiundfritz`](../../freiundfritz/) (Anny + Zutritt, Erweiterung UniFi/API).

### 3.2 Zugangslogik

| Nutzergruppe | Pilot (nur Apartment-Tür) | Später (Zielbild) |
|--------------|---------------------------|-------------------|
| **Bewohner** | Mechanischer Schlüssel | Wie bisher |
| **Anny-Gast** | PIN/App **Apartment-Tür**; Weg ins Haus **manuell** bis Kellergang frei | Kellergang + Zielraum |
| **Notfall / Flucht** | **Klinke innen** mechanisch; Schlüssel | Unverändert; Öffner fail-secure prüfen |

**Anny-Regeln (Zielbild):** Apartment → später Kellergang + Apartment · Kellerräume → Kellergang + Raum · Zeitfenster z. B. 15 Min. vor/nach Buchung.

### 3.3 Elektrik und PoE (transparent)

| Aussage | Bedeutung |
|---------|-----------|
| Kein neuer **Haus-Stromnetz**-Ausbau | Keine **neue** 230-V-Leitung bis zur Tür; Nutzung **bestehender** Kasten/Verteiler (230 V ggf. nur für PoE-Switch/Injektor im Schrank — bereits von PostBG vorgesehen). |
| **PoE** | Niederspannung + Daten auf **CAT7**; Hub Mini braucht **PoE++**. |
| **Türöffner** | Hub schaltet den **vorhandenen Öffner** — das ist **Anlagenänderung** (§ 13 NAV); PostBG hat **Eigenmontage** dennoch abgesegnet; **Vereins-Haftpflicht** und Schadenfall-Risiko bleiben eigenes Thema ([versicherung-nuki-unifi.md](../versicherung-nuki-unifi.md)). |

### 3.4 Offene technische Klärung (Pilot)

- [ ] **Internet/Konsole** im Apartment ohne zweiten Vertrag (LAN, VLAN, Gast-WLAN, Hausanschluss — Optionen prüfen).
- [ ] Am Apartment-Kasten: CAT7 patchbar, Platz Hub, **PoE++-Quelle**, Öffner-Spannung/Typ, **Klinke bei Stromausfall**.
- [ ] Apartment ist **1. Rettungsweg** der Wohnung — Verhalten dokumentieren (Gröpke: Fluchttüren unbeeinträchtigt).

### 3.5 Bewusst ausgeschlossen

- **Glastüren Veranstaltungsraum** — kein UniFi, kein Magnet.
- **Haustür** — nicht vorverdrahtet; nicht Teil Phase 1.
- **Kellergang-Tür** — erst nach **Einsperr-/Zylinder-Klärung** (siehe [kontext-gebaeude.md](kontext-gebaeude.md)).

### 3.6 Veranstaltungsraum — Rechtliches (unverändert relevant)

Öffentliche Anny-Buchungen: **Art. 19 LStVG** (KVR München). VR-Nutzung, Fluchtwege, max. Auslegung 100 Personen — Details wie in Version 1.x; Smart Lock **verschärft** Recht nicht, **ersetzt** Anzeigen nicht. Phase 3 VR erst nach Checkliste.

---

## 4. Phasenplan

| Phase | Inhalt |
|-------|--------|
| **0 — Beschluss & Klärung** | Vereinsbeschluss; Internet Apartment; Hardware-Recherche/Bestellung Testtür; [checkliste.md](checkliste.md); Vereins-Haftpflicht Anny-Gäste |
| **1 — Pilot (1 Tür)** | Montage **Tobias Schüle**: Hub + Leser + Konsole; Anny-UniFi koppeln; Testbuchungen; 2–4 Wochen Probebetrieb |
| **2 — Kellerräume** | Musik + Kreativ (+ ggf. weitere) nach erneutem Beschluss; je Tür Checkliste |
| **3 — VR + Kellergang** | Nur Innentür Kellergang (nicht Glastüren); Baustelle frei; Rechtliches abgeschlossen |
| **4 — Betrieb** | Firmware/Konsole; kein Akku an Tür; Ansprechpartner Störungen: _[eintragen]_ |

**Meilenstein Pilot:** Stabile Apartment-Buchungen mit PIN; Bericht an Verein; Go/No-Go Ausbau.

---

## 5. Kosten (Richtwerte 2026)

### 5.1 Pilot — eine Testtür (Apartment)

| Position | Grob |
|----------|------|
| Cloud Gateway Max (o. ä.) | ~180–250 € |
| 1× Door Hub Mini | ~99 € |
| 1× Leser mit PIN (z. B. Reader Flex / UA-G2-Pro) | ~160–200 € |
| PoE++ (Injektor oder Switch-Anteil) | ~50–150 € |
| Reserve, Kleinteile | ~50 € |
| **Summe Hardware Pilot** | **~550–750 €** |
| Internet/LAN-Lösung Apartment | **offen** (0–150 € je nach Variante) |
| **Budget-Vorschlag Verein** | **max. 1.200 €** inkl. Puffer (Antrag B) |

**Einbau:** Ehrenamt (Tobias Schüle) — kein Fachbetrieb-Budget eingeplant (PostBG-Freigabe).

### 5.2 Vollausbau — fünf Türen (Referenz)

Siehe [nuki-vs-unifi.md](../nuki-vs-unifi.md) (5× Mini + Reader Flex + Gateway + PoE): Hardware **~1.700–1.900 €**; frühere Elektriker-Pauschalen entfallen bei Eigenmontage, **Risiko** bleibt dokumentiert.

**Anny:** nicht im Hardware-Budget (bereits beschafft).

---

## 6. Rechtliches und Zuständigkeiten

| Thema | Stand / Pflicht |
|-------|-----------------|
| **Verein** | Beschluss Grundsatz + Budget **ausstehend** |
| **Postbaugenossenschaft** | Plan **abgesegnet** (22.09.2026, Gröpke) — schriftlich im Protokoll festhalten |
| **Fluchtweg** | Pro Tür vor Montage; Glastüren ausgenommen |
| **LStVG / VR** | Bei öffentlichen Buchungen KVR; vor VR-Phase 3 klären |
| **Versicherung** | Gebäude: PostBG; **Vereins-Haftpflicht**: Anny-Gäste selbst ([versicherung.md](versicherung.md)) |
| **DSGVO** | Gästedaten Anny/UniFi |

---

## 7. Risiken und Gegenmaßnahmen

| Risiko | Gegenmaßnahme |
|--------|----------------|
| **Kein Internet** am Pilotstandort | Phase 0 klären; Pilot startet erst mit Konnektivität |
| **Öffner/Fail-Secure** falsch | Messung/Protokoll vor Go-Live; Brandschutz bei RW-Türen |
| **DIY am Öffner** — Versicherung Schadenfall | PostBG-Zusage dokumentiert; Verein informiert Versicherer |
| **Kellergang Einsperrung** | Kein Ausbau bis Klärung; siehe Kontext Gebäude |
| **VR rechtlich** | LStVG/Nutzung vor öffentlichem Betrieb |
| **Gast versteht Zugang nicht** | Anny-Mail, Fluchtweg-Hinweis |

---

## 8. Beschlussvorlagen (Mitgliederversammlung)

### Antrag A — Grundsatz

> Der Bewohnerverein befürwortet die schrittweise Einführung elektronischer Zutrittskontrolle auf Basis **UniFi Door Access** in Verbindung mit **Anny**, beginnend mit **einer Testtür (Apartment)**, vorbehaltlich der Checkliste und eines **gesonderten Beschlusses** für jede weitere Tür. Zur Kenntnis: Die Postbaugenossenschaft hat den Plan am 22.09.2026 durch Herrn Gröpke abgesegnet.

☐ Ja · ☐ Nein · ☐ Vertagung

### Antrag B — Budget Pilot

> Für **Phase 1 (Testtür Apartment)** wird ein Budget von **max. 1.200 €** (UniFi-Hardware, PoE, Konnektivität/LAN am Pilotstandort, Reserve) freigegeben. Anny ist bereits beschaffen.

☐ Ja · ☐ Nein · ☐ Abweichender Betrag: _______ €

### Antrag C — Budget Vollausbau (optional)

> Für den **Vollausbau** aller nach Checkliste freigegebenen vorverdrahteten Türen (bis zu 5) wird eine **Obergrenze von max. 2.500 €** Hardware bestätigt. Weitere Beschlüsse je Phase bleiben vorbehalten.

☐ Ja · ☐ Nein · ☐ Nur Pilot

### Antrag D — Mandat Klärung & Umsetzung

> Die Projektgruppe wird beauftragt, **Internet im Apartment ohne zweiten Vertrag** zu klären, die **Hardware für die Testtür** zu beschaffen (Einbau: Tobias Schüle), die **Checkliste** abzuarbeiten und dem Verein zu berichten — insbesondere Fluchtwege, Kellergang, VR-Rechtliches, Versicherung Vereins-Haftpflicht.

☐ Ja · ☐ Nein

---

## 9. Nächste Schritte nach positivem Beschluss

1. Hardware bestellen (Stückliste aus Recherche / [nuki-vs-unifi.md](../nuki-vs-unifi.md)).
2. Internet/LAN Apartment lösen.
3. Montage Testtür, Anny koppeln, Testbuchungen.
4. Bericht an Verein → Beschluss Phase 2.

---

## Anhang — Checkliste

Vollständig: **[checkliste.md](checkliste.md)** (Vor Montage je Tür: Öffner, PoE, Fluchtweg, PostBG schriftlich pro Tür bei Ausbau).

---

*Dieses Dokument dient der Entscheidungsfindung im Bewohnerverein. Es ersetzt keine rechtsverbindliche Prüfung durch Postbaugenossenschaft, Elektrofachkraft, Bauaufsicht oder Versicherer.*
