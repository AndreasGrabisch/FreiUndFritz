# Projektplan: Elektronische Zutrittskontrolle mit Nuki

**Version:** 1.1 · **August 2026** · Zur Entscheidung: Bewohnerverein · München, Bayern

---

## 1. Zusammenfassung

Buchbare Zugänge (v. a. **Apartment**) und weitere Türen schrittweise mit **Nuki Smart Lock Pro + Keypad** automatisieren, angebunden an **Anny** — ohne manuelle Schlüsselübergabe.

| | |
|---|---|
| **Vollausbau (5 Türen)** | ca. **2.000–2.500 €** einmalig |
| **Laufende Kosten Nuki** | **0 €** (kein Nutzer-Abo) |
| **Umsetzung gesamt** | **max. 2 Monate** ab Beschluss (parallel Klärung + Pilot) |
| **Pilot (Phase 1)** | **Apartment** + Haustür — wichtigste Buchung zuerst |

**Offen vor Kauf:** Zylinder-Kompatibilität an Kellertüren (siehe Kap. 3). **Beschluss:** Grundsatz, Budget Pilot, Mandat technische Klärung.

---

## 2. Ausgangslage

- **~200 Bewohner**, öffentliche **Anny-Buchungen** für Kellerräume und Apartment.
- **Fünf Türen:** Haustür · Veranstaltungsraum (Keller) · Musikraum · Kreativraum · Apartment (Dach).
- Zutritt heute manuell. Veranstaltungsraum: Glastüren zum Hof (vermutl. Rettungsweg) + Tür Kellergang (Klinke innen / Knauf außen).

**Ziele:** Automatischer Zutritt bei Buchung · mechanische Schlüssel bleiben · keine Nutzer-Abo-Kosten · DIY · Fluchtwege einhalten.

---

## 3. Technische Voraussetzungen und offene Punkte

Nuki sitzt **innen** am Zylinder und **dreht den eingesteckten Schlüssel** per Motor. Dafür muss an jeder Tür gelten:

| Voraussetzung | Status |
|---------------|--------|
| Schlüssel **innen stecken** und vom Nuki drehbar | **Apartment:** sehr wahrscheinlich ja (normale Wohnungstür, Referenz: funktioniert in einer vergleichbaren Wohnung im Haus) · **Kellertüren:** **noch nicht getestet** (nur je ein Schlüssel vorhanden — Test mit zweitem Schlüssel bzw. Montageprobe nötig) |
| Not- und Gefahrenzylinder, Maße Nuki-kompatibel | Vor Bestellung je Tür prüfen |
| WLAN 2,4 GHz | Messung an geplanten Türen |
| Keine Fluchttür ohne Freigabe | VR-Glastüren: voraussichtlich **kein** Nuki |

### Kellertür Veranstaltungsraum → Kellergang (nach außen)

**Ist-Zustand:** Tür lässt sich derzeit **nur von außen abschließen**. Innen ist eine **Klinke** (Flucht öffnen), aber der **Schlüssel lässt sich innen nicht drehen**.

- **Für Nuki:** **nicht nutzbar** im Ist-Zustand — Nuki braucht innen einen drehbaren, steckenden Schlüssel.
- **Baurecht / Mangel?** Nicht pauschal als „Mangel“ zu bewerten: Bei Rettungswegen sind **rein außen verriegelbare** Zylinder mit **innen nur Klinke** gezielt vorgesehen. Ob das hier so gewollt ist oder ein defekter/falscher Zylinder, muss **Eigentümer / Verwaltung / ggf. Schließer** klären.
- **Folge:** VR-Kellergang-Tür erst nach **Zylinderanpassung** und **schriftlicher Freigabe** (Fluchtweg); bis dahin manueller Zutritt.

### Apartment (Pilot)

Höchste Priorität — wichtigste Anny-Ressource. Wahrscheinlichkeit hoher Nuki-Tauglichkeit; Pilot bestätigt Anny-Integration und Gästeablauf.

---

## 4. Lösung: Nuki + Anny

- **Nuki Smart Lock Pro** innen am Zylinder · **Keypad 2** außen (Gast-PIN).
- **Anny Professional:** zeitlich begrenzte Zugänge und Remote Open pro Buchung.
- **Bewohner:** weiterhin mechanische Schlüssel; optional ein gemeinsamer Haustür-PIN.
- **Anny-Regeln (Beispiel):** Apartment → Haustür + Apartment; Kellerräume analog · Zeitfenster z. B. 15 Min. vor/nach Buchung.

**Veranstaltungsraum:** Glastüren **ohne** Nuki. Kellergang-Tür nur nach Klärung (Kap. 3).

---

## 5. Warum nicht die Alternativen?

| System | Hauptgrund Ablehnung |
|--------|---------------------|
| **KleverKey** | **Laufende Kosten pro Nutzer** — an der Haustür mit ~200 Bewohnern unverhältnismäßig; Zylinderersatz; Mischsystem mit Nuki = zwei Welten für Gäste |
| **UniFi Door Access** | **Gewerbe/Verkabelung**, hohe Einmalkosten, **kein Zylinder-Nachrüstsatz**, **keine Anny-Integration**, ungeeignet für Klinke/Fluchtweg — Overkill |
| **Tapkey** | Nutzerpakete — gleiche Kostenskala wie KleverKey bei vielen Berechtigungen |
| **EVVA AirKey** | Fachbetrieb, KeyCredits, auf Dauerberechtigungen — schlecht für Anny-Gast-PINs |
| **dormakaba Exivo** | Intransparente Preise, nur Fachbetrieb, monatliches Service-Abo |
| **Salto KS/Space** | Hotel/Gewerbe, teure Infrastruktur, keine Anny-Anbindung |

**Nuki** vereint als einziges geprüftes System: **Anny-native PINs**, **0 € Nutzer-Abo**, **Nachrüstung am bestehenden Zylinder**, **DIY**, **mechanische Schlüssel parallel** (wo Zylinder es zulässt).

---

## 6. Phasenplan (max. 2 Monate)

| Phase | Dauer | Inhalt |
|-------|-------|--------|
| **0 — Klärung** | Woche 1–3 (parallel) | Eigentümer/Fluchtweg · Zylinder-Tests Keller (Schlüssel innen drehbar?) · VR-Tür Kellergang klären · WLAN · Versicherung · LStVG (KVR) bei öffentl. Buchungen |
| **1 — Pilot** | Woche 2–6 | **Apartment + Haustür:** Hardware, Montage, Anny, Testbuchungen, Gästeanleitung |
| **2 — Ausbau** | Woche 5–8 | Musikraum, Kreativraum — **nur wenn** Zylinder-Test positiv |
| **3 — VR** | nach Freigabe | Nur Kellergang-Tür, nicht Glastüren — nur nach Zylinderlösung + Freigabe |
| **4 — Betrieb** | dauerhaft | Akku laden (4–6 Mon.), abgelaufene Nuki-Zugänge prüfen, Ansprechpartner: [ ] |

**Meilenstein Pilot:** Apartment-Buchungen mit automatischem Zutritt stabil (ca. 2 Wochen Probebetrieb).

---

## 7. Kosten

| Position | Summe |
|----------|-------|
| 5× Lock Pro + 5× Keypad + Reserve | **ca. 2.195 €** |
| **Pilot (Apartment + Haustür, 2 Türen)** | **ca. 880 €** (+ Puffer → Budget **max. 1.000 €**) |
| WLAN-Repeater (falls nötig) | 50–120 €/Stück |
| Nuki Nutzer-Abo | **0 €** |

Nicht enthalten: Schließer/Elektriker (Sonderfälle), Gutachten, Anny Professional ([bestehende Kosten]).

---

## 8. Rechtliches (Kurz)

| Thema | Hinweis |
|-------|---------|
| §47 VStättV | Nein (max. ~50 Pers.) |
| Art. 19 LStVG | **Ja** bei öffentlichen Anny-Buchungen → KVR |
| Fluchtweg / Smart Lock | Freigabe Eigentümer **vor** Montage |
| WEG / Versicherung / DSGVO | Klären / informieren |

---

## 9. Risiken

| Risiko | Gegenmaßnahme |
|--------|---------------|
| Kellertüren: Schlüssel innen nicht drehbar | **Vor Bestellung testen**; ggf. Zylinder tauschen oder Tür aus Plan streichen |
| VR Kellergang: nur außen verriegelbar | Eigentümer klären; **kein Nuki** ohne Anpassung |
| 200-Zugangs-Limit pro Nuki | Abgelaufene Zugänge löschen; Bewohner nicht alle digital |
| WLAN / Akku | PIN/Bluetooth vor Ort; mechanischer Schlüssel |
| VR Glastüren Rettungsweg | Keine Nachrüstung |

---

## 10. Beschlussvorlagen

**A — Grundsatz:** Nuki + Anny, vorbehaltlich Eigentümer-Freigabe und positiver Zylinder-Tests je Tür. ☐ Ja ☐ Nein

**B — Budget Pilot:** max. **1.000 €** für **Apartment + Haustür**. ☐ Ja ☐ Nein ☐ Abweichend: ___ €

**C — Budget Vollausbau (optional):** max. **2.500 €** für bis zu 5 freigegebene Türen. ☐ Ja ☐ Nein ☐ Nur Pilot

**D — Mandat Klärung:** Projektgruppe führt Zylinder-Tests, Eigentümer-Anfrage und VR-Tür-Klärung bis **[Datum]** durch. ☐ Ja ☐ Nein

---

## Anhang — Checkliste je Tür (vor Bestellung)

- [ ] Schlüssel innen steckend **drehbar** (Nuki-Test oder Probe)
- [ ] Not- und Gefahrenzylinder, Abstand Klinke ≥ 30 mm
- [ ] WLAN 2,4 GHz ausreichend
- [ ] Keine Fluchttür / schriftliche Freigabe
- [ ] VR Kellergang: Klärung Zylinder (innen drehbar nötig für Nuki)

---

*Entscheidungsunterlage für den Bewohnerverein — ersetzt keine Prüfung durch Eigentümer, Schließer oder Behörden.*
