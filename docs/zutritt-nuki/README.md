# Elektronische Zutrittskontrolle (Nuki + Anny)

**Stand:** September 2026 · **Ort:** München, Bayern · **Entscheidung:** Bewohnerverein

Dieser Ordner bündelt alle Unterlagen aus Planung, Chat und technischer Recherche. Die **maßgebliche Entscheidungsvorlage** für die Mitgliederversammlung ist der [Projektplan](projektplan.md).

---

## Lesepfade

### Für den Bewohnerverein (Beschluss)

1. [Kontext Gebäude & Türen](kontext-gebaeude.md)
2. [Projektplan](projektplan.md) (Phasen, Kosten, Beschlussanträge)
3. [Checkliste](checkliste.md) (Antrag D / Phase 0)

### Für die Hausverwaltung / Postbaugenossenschaft

1. [E-Mail-Entwurf](mail-hausverwaltung.md)
2. [Kontext Gebäude & Türen](kontext-gebaeude.md) — Kellergang-Tür, Fluchtweg
3. [Rechtliches](rechtliches.md) — Veranstaltungsraum, LStVG

### Für Technik & Betrieb

1. [Technik Nuki & Anny](technik-nuki-anny.md)
2. [Checkliste](checkliste.md) — Türtest, WLAN, Zylinder
3. Software: [`freiundfritz`](../../freiundfritz/) (Anny + Door Lock Controller)

### Systemwahl & Hintergrund

1. [Systemvergleich Alternativen](systemvergleich-alternativen.md) — KleverKey, Tapkey, Salto, Exivo, AirKey, …
2. [Vergleich Nuki vs. UniFi Access](vergleich-nuki-unifi.md) — detaillierte Gegenüberstellung (Ethernet/Summer vorhanden)
3. [Gesprächsprotokoll Nuki/UniFi](gespraechsprotokoll-nuki-unifi.md)

### Versicherung

- Kurz: [Versicherungen — wen fragen?](versicherung.md)
- Ausführlich (Genossenschaft vs. Verein, UniFi/NAV, je Tür): [../versicherung-nuki-unifi.md](../versicherung-nuki-unifi.md)

### Postbau / Gröpke / Brandschutz

- [Treffen Gröpke 22.09.2026](../gespraechsprotokoll-groepke-2026-09-22.md) — UniFi-Pilot, Freigabe PostBG
- [Analyse Fluchtwege + Schema](analyse-fluchtwege.md)
- [Prüfplan Vorhaltung](../plan-zutritt-nuki-unifi.md)
- [Antwortentwurf Gröpke](../antwort-groepke.md)
- [Nuki vs. UniFi, aktuelle Fassung](../nuki-vs-unifi.md)

---

## Dokumente (Übersicht)

| Datei | Zweck |
|-------|--------|
| [analyse-fluchtwege.md](analyse-fluchtwege.md) | Brandschutz UG/DG + Zugangsschema, Tür-IDs |
| [kontext-gebaeude.md](kontext-gebaeude.md) | 56 WE, fünf verdrahtete Türen, Kellergang, VR |
| [projektplan.md](projektplan.md) | Gesamtplan, Phasen, Kosten, Risiken, Beschlussvorlagen |
| [checkliste.md](checkliste.md) | Abhakliste vor Montage / Ausbau |
| [mail-hausverwaltung.md](mail-hausverwaltung.md) | Anfrage Fluchtweg, Zylinder, Zustimmung |
| [rechtliches.md](rechtliches.md) | LStVG, VR als Veranstaltungsort, Zuständigkeiten |
| [versicherung.md](versicherung.md) | Welche Policen, welche Fragen |
| [technik-nuki-anny.md](technik-nuki-anny.md) | Zylinder, Klinke, 200er-Limit, Anny-Regeln |
| [systemvergleich-alternativen.md](systemvergleich-alternativen.md) | Warum nicht KleverKey, UniFi, … |
| [vergleich-nuki-unifi.md](vergleich-nuki-unifi.md) | Tiefer Vergleich bei vorhandener Türtechnik |
| [gespraechsprotokoll-nuki-unifi.md](gespraechsprotokoll-nuki-unifi.md) | Verlauf der UniFi-Diskussion |
| [gespraechsprotokoll-groepke-2026-09-22.md](gespraechsprotokoll-groepke-2026-09-22.md) | Verweis auf Treffen PostBG |

---

## Aktuelle Projektentscheidung (Kurz)

**Nach Treffen mit Herrn Gröpke am 22.09.2026** ([Protokoll](../gespraechsprotokoll-groepke-2026-09-22.md)):

- **Geplanter Rollout:** **UniFi Access** für alle Türen, Start mit **einer Testtür**; Einbau **Tobias Schüle** (PoE, kein Eingriff ins Haus-Stromnetz; Fluchttüren unverändert nutzbar)
- **Postbaugenossenschaft:** Plan von **Herrn Gröpke** abgesegnet (inkl. Einbau ohne Fachbetrieb / versicherungstechnische Folgen)
- **Offen:** Internet im Apartment ohne zweiten Vertrag; **Zustimmung Vorstand Bewohnerverein** ausstehend; Hardware für erste Testtür bestellen

Ältere Vereinsvorlage (Nuki-Pilot Apartment) siehe [projektplan.md](projektplan.md) — vor Beschluss des Vereins anpassen.
