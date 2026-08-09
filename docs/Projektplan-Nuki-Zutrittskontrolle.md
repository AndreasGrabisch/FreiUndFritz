# Projektplan: Elektronische Zutrittskontrolle mit Nuki

**Version:** 1.0  
**Datum:** August 2026  
**Zur Entscheidung:** Bewohnerverein / Trägergemeinschaft  
**Standort:** München, Bayern  

---

## 1. Zusammenfassung für die Entscheidung

Wir schlagen vor, die Zutritte zu buchbaren Kellerräumen und zur Haustür schrittweise mit **Nuki Smart Lock Pro** und **Nuki Keypad** zu automatisieren. Die Anbindung an unser Buchungssystem **Anny** ermöglicht es externen und internen Nutzern, nach einer Buchung automatisch Zugang zu erhalten — ohne manuelle Schlüsselübergabe.

| | |
|---|---|
| **Einmalige Investition (Vollausbau)** | ca. **2.000–2.500 €** (5 Türen, siehe Kap. 5) |
| **Laufende Kosten** | ca. **0 €** für Nuki (kein Nutzer-Abo); Anny Professional separat |
| **Zeitraum** | ca. **3–6 Monate** inkl. Klärung mit Eigentümer/Verwaltung |
| **Empfohlener Start** | Phase 1: Haustür + 2 Kellerräume; Veranstaltungsraum nach Freigabe |

**Beschluss wird erbeten zu:** Grundsatzentscheidung, Budgetrahmen, Beauftragung Klärung Fluchtweg, Start Phase 1.

---

## 2. Ausgangslage und Ziele

### 2.1 Ist-Zustand

- **Ca. 200 Bewohner** im Haus; zusätzlich **öffentliche Buchungen** über Anny für Kellerräume und ggf. Apartment.
- **Fünf relevante Türen:**

| Tür | Lage | Nutzung |
|-----|------|---------|
| Haustür | Eingang | Zugang zu Kellern und Haus |
| Veranstaltungsraum | Keller | Öffentliche/interne Veranstaltungen (max. ca. 50 Pers.) |
| Musikraum | Keller | Buchbar |
| Kreativraum | Keller | Buchbar |
| Apartment | Dach | Buchbar |

- Buchungen laufen über **Anny**; Zutritt heute manuell (Schlüssel, Aufschließen durch Anwesende).
- Veranstaltungsraum: **Glastüren zum Hof** sowie **Tür mit Klinke innen / Knauf außen** in den Kellergang.

### 2.2 Ziele

1. **Automatischer Zutritt** bei bestätigter Anny-Buchung (PIN oder App).
2. **Mechanische Hausschlüssel** für Bewohner bleiben erhalten.
3. **Keine laufenden Nutzergebühren** pro Bewohner (im Gegensatz zu z. B. KleverKey).
4. **Selbstmontage** wo möglich; keine aufwendige Verkabelung.
5. **Fluchtwege und baurechtliche Vorgaben** werden vor Inbetriebnahme geklärt und eingehalten.

### 2.3 Bewusst nicht gewählt

| Alternative | Grund der Ablehnung |
|-------------|---------------------|
| KleverKey (alle Türen) | Hohe laufende Kosten bei vielen Berechtigungen; Zylinderersatz |
| dormakaba Exivo | Keine transparenten Preise; Fachbetrieb; monatliches Service-Modell |
| UniFi Door Access | Hohe Hardware- und Installationskosten; Verkabelung; Overkill für Wohnhaus |
| EVVA AirKey (Haustür) | Fachbetrieb; zweites System neben Kellerräumen |

---

## 3. Lösungskonzept

### 3.1 Technik

- **Nuki Smart Lock Pro (5. Gen):** Montage **innen** am bestehenden Europrofil-Zylinder; dreht den eingesteckten Schlüssel per Motor.
- **Nuki Keypad 2:** Montage **außen** am Türrahmen; Zugang per **6-stelliger PIN** (für Gäste ohne App).
- **WLAN 2,4 GHz** an jeder Tür mit Anny-Anbindung (für Fernfreigabe und Buchungssync).
- **Anny Professional** mit Nuki-Integration: Bei Buchung werden zeitlich begrenzte Zugänge erzeugt; **Remote Open** in der Anny-App möglich.

### 3.2 Zugangslogik

| Nutzergruppe | Haustür | Kellerräume (gebucht) |
|--------------|---------|----------------------|
| **Bewohner (Dauer)** | Mechanischer Schlüssel; optional **ein gemeinsamer Keypad-PIN** | Mechanischer Schlüssel oder Buchung über Anny |
| **Anny-Gast (öffentlich)** | PIN oder Anny Remote Open (wenn in Regel enthalten) | PIN / App / Remote Open für Buchungszeitraum |
| **Notfall / Flucht** | Klinke bzw. manueller Nuki-Drehknauf **innen**; mechanischer Schlüssel **außen** | Unverändert, soweit nicht elektrifiziert |

### 3.3 Anny-Regeln (Beispiel)

| Ressource Anny | Zugeordnete Nuki-Schlösser |
|----------------|----------------------------|
| Musikraum | Haustür + Musikraum |
| Kreativraum | Haustür + Kreativraum |
| Veranstaltungsraum | Haustür + Veranstaltungsraum *(nur nach Freigabe)* |
| Apartment | Haustür + Apartment *(optional Phase 3)* |

Zeitfenster: z. B. **15 Min. vor** bis **15 Min. nach** Buchungsende (in Anny konfigurierbar).

### 3.4 Veranstaltungsraum — Sonderfall

- **Glastüren zum Hof:** Voraussichtlich **Rettungsweg / Notausgang** → **keine** Smart-Lock-Nachrüstung.
- **Tür Kellergang:** Derzeit **Klinke innen, Knauf außen** (baurechtlich abgenommen). Nuki ist hier **technisch verträglich** (Klinke bleibt nutzbar), aber **nur nach schriftlicher Freigabe** durch Eigentümer/Brandschutz.
- **Öffentliche Buchungen** (max. 50 Pers.): Anzeige nach **Art. 19 LStVG** beim KVR München erforderlich (kein §47-VStättV-Antrag bei unter 200 Personen).

---

## 4. Phasenplan

### Phase 0 — Klärung und Freigaben (ca. 4–8 Wochen)

**Verantwortlich:** Projektgruppe + Eigentümer/Verwaltung  

| Nr. | Aufgabe | Ergebnis |
|-----|---------|----------|
| 0.1 | Flucht- und Rettungswegplan einsehen | Liste: welche Türen sind Rettungsweg |
| 0.2 | Schriftliche Anfrage Eigentümer (Fluchtweg, Smart Lock, Haustür) | Go/No-Go pro Tür |
| 0.3 | Bauantrag-Nutzung Veranstaltungsraum klären | Gemeinschaftsraum vs. Versammlungsstätte |
| 0.4 | LStVG-Anzeige öffentliche Vergnügung (KVR) vorbereiten/einreichen | Bestätigung oder Auflagen |
| 0.5 | Versicherung informieren | Schriftliche Stellungnahme |
| 0.6 | WLAN-Empfang an allen geplanten Türen testen | Protokoll; ggf. Repeater einplanen |
| 0.7 | Zylinder prüfen (Not- und Gefahrenfunktion, Maße) | Kompatibilität Nuki bestätigt |
| 0.8 | Beschluss Bewohnerverein: Budget + Phase 1 | Protokoll |

**Meilenstein:** Schriftliche Freigabe mindestens für **Haustür + 2 Kellerräume**.

---

### Phase 1 — Pilot (ca. 2–4 Wochen nach Freigabe)

**Umfang:** Haustür + **Musikraum** + **Kreativraum**

| Nr. | Aufgabe |
|-----|---------|
| 1.1 | Hardware beschaffen (3× Lock Pro, 3× Keypad, Reserve-Akkus) |
| 1.2 | Montage und Einrichtung in Nuki-App |
| 1.3 | WLAN-Anbindung; Test Remote Open |
| 1.4 | Anny-Integration autorisieren; Regeln anlegen |
| 1.5 | Testbuchungen (intern + extern); PIN-Zustellung prüfen |
| 1.6 | Bewohner-PIN Haustür (optional); Hausmitteilung |
| 1.7 | Kurzanleitung für Gäste (Anny-Mail, Fluchtweg-Hinweis) |

**Meilenstein:** 30 Tage Probebetrieb ohne kritische Störungen.

---

### Phase 2 — Veranstaltungsraum (nur bei Freigabe)

| Nr. | Aufgabe |
|-----|---------|
| 2.1 | Nur **Kellergang-Tür** elektrifizieren (nicht Glastüren) |
| 2.2 | Anny-Regel Haustür + Veranstaltungsraum |
| 2.3 | Fluchtweg-Beschilderung in Buchungsbestätigung |

**Meilenstein:** Erste öffentliche Veranstaltung mit automatischem Zutritt.

---

### Phase 3 — Apartment Dach (optional)

| Nr. | Aufgabe |
|-----|---------|
| 3.1 | WLAN-Reichweite Dach prüfen |
| 3.2 | Montage + Anny-Regel |
| 3.3 | Abstimmung mit Apartment-Nutzern (Schlüssel parallel?) |

---

### Phase 4 — Betrieb und Pflege (dauerhaft)

| Intervall | Aufgabe |
|-----------|---------|
| Monatlich | Abgelaufene Nuki-Zugänge prüfen (200er-Limit); Anny-Buchungen stichprobenartig |
| Alle 4–6 Monate | Akku Nuki laden |
| Jährlich | Jahres-PIN Bewohner rotieren (optional); Funktionstest Fluchtweg-Türen |
| Bei Störung | Fallback: mechanische Schlüssel; Ansprechpartner benennen |

**Ansprechpartner:** [Name, Rolle, Telefon, E-Mail eintragen]

---

## 5. Kostenübersicht

### 5.1 Einmalkosten Hardware (Richtwerte, Stand 2026)

| Position | Stück | Einzelpreis | Summe |
|----------|-------|-------------|-------|
| Nuki Smart Lock Pro 5. Gen | 5 | 269 € | 1.345 € |
| Nuki Keypad 2 | 5 | 150 € | 750 € |
| Reserve / Kleinteile (Batterien, Montage) | 1 | 100 € | 100 € |
| **Gesamt Vollausbau (5 Türen)** | | | **ca. 2.195 €** |

**Phase 1 (3 Türen):** ca. **1.320 €**

Optional: WLAN-Repeater für Keller/Dach ca. **50–120 €** pro Gerät.

### 5.2 Laufende Kosten

| Position | Kosten/Jahr | Anmerkung |
|----------|-------------|-----------|
| Nuki Cloud / Nutzer-Abo | **0 €** | Kein Abo für Anny-Betrieb nötig |
| Anny Professional | [bestehende Kosten eintragen] | Bereits für Smart-Lock-Integration erforderlich |
| Strom / WLAN | Vernachlässigbar | Bestehende Haus-Infrastruktur |
| Wartung Ehrenamt | 0 € | Zeitaufwand Projektgruppe |

### 5.3 Nicht enthalten

- Elektriker / Schließer (nur bei Sonderfällen)
- Baurechtliche Gutachten
- Identity-/UniFi-Infrastruktur
- Smartphone für alle Bewohner

---

## 6. Rechtliches und Genehmigungen (München / Bayern)

| Thema | Pflicht? | Zuständig | Status |
|-------|----------|-----------|--------|
| §47 VStättV (>200 Besucher) | Nein bei max. 50 | — | — |
| Art. 19 LStVG (öffentliche Vergnügung) | **Ja** bei öffentl. Anny-Buchungen | KVR München | ☐ offen |
| Fluchtweg / Smart Lock | Klärung **vor** Montage | Eigentümer / Brandschutz | ☐ offen |
| WEG / Hausordnung | Zustimmung Träger | Eigentümergemeinschaft | ☐ offen |
| Versicherung | Information empfohlen | Versicherer | ☐ offen |
| Datenschutz (Gäste-E-Mail in Anny/Nuki) | DSGVO-konforme AV | Verein | ☐ offen |

---

## 7. Risiken und Gegenmaßnahmen

| Risiko | Auswirkung | Gegenmaßnahme |
|--------|------------|---------------|
| Fluchtweg: keine Smart Locks am VR | VR nur manuell | Phase 2 nur nach Freigabe; Glastüren unberührt |
| 200-Zugangs-Limit pro Nuki | Neue Buchung schlägt fehl | Abgelaufene Zugänge löschen; nur Gäste digital, nicht alle 200 Bewohner |
| WLAN-Ausfall an Tür | Kein Remote Open / Anny-Sync | Öffnen per Bluetooth/PIN vor Ort; mechanischer Schlüssel |
| Leerer Akku | Kein Motorverschluss | Manuell am Nuki-Knauf; rechtzeitig laden (App-Warnung) |
| Öffentliche Buchung ohne LStVG-Anzeige | Ordnungswidrigkeit | Anzeige vor Start öffentlichen Betriebs |
| Gäste finden Fluchtweg nicht | Sicherheitsrisiko | Hinweis in Anny-Mail; Beschilderung im Raum |

---

## 8. Technische Grenzen (transparent kommunizieren)

- **Max. 200 gleichzeitige zukünftige Zugänge** pro Nuki-Schloss (Anny-Limit).
- **Pro Buchung mit mehreren Türen:** ggf. **mehrere PINs** (eine pro Tür).
- **Zwei Systeme** (falls später doch KleverKey o. Ä.): schlechtere Gäste-UX — aktuell **nicht** geplant.
- **Nuki ersetzt keine Fluchttür-Hardware** (Panikstange etc.).

---

## 9. Organisationsstruktur

| Rolle | Aufgabe | Person |
|-------|---------|--------|
| Projektleitung | Koordination, Beschaffung, Anny-Admin | [ ] |
| Technik | Montage, Nuki-App, WLAN | [ ] |
| Recht / Verwaltung | Anschreiben Eigentümer, KVR, Versicherung | [ ] |
| Anny-Admin | Regeln, Buchungsseite, Gäste-Mail | [ ] |
| Stellvertretung | Bei Ausfall Projektleitung | [ ] |

---

## 10. Beschlussvorlagen für die Mitgliederversammlung

### Beschlussantrag A — Grundsatz

> Der Bewohnerverein befürwortet die Einführung einer elektronischen Zutrittskontrolle auf Basis **Nuki Smart Lock Pro** in Verbindung mit **Anny**, vorbehaltlich der schriftlichen Freigabe durch den Eigentümer/Träger für jede einzelne Tür und unter Einhaltung der Fluchtweg-Vorgaben.

- ☐ Ja  
- ☐ Nein  
- ☐ Vertagung bis Klärung Fluchtweg (Phase 0)

### Beschlussantrag B — Budget Phase 1

> Für **Phase 1** (Haustür, Musikraum, Kreativraum) wird ein Budget von **max. 1.400 €** (inkl. Puffer) freigegeben.

- ☐ Ja  
- ☐ Nein  
- ☐ Abweichender Betrag: _______ €

### Beschlussantrag C — Budget Vollausbau (optional)

> Für den **Vollausbau** aller freigegebenen Türen (bis 5) wird ein Gesamtbudget von **max. 2.500 €** (inkl. WLAN-Nachrüstung) als Obergrenze bestätigt.

- ☐ Ja  
- ☐ Nein  
- ☐ Nur Phase 1, weitere Entscheidung später

### Beschlussantrag D — Mandat Klärung

> Die Projektgruppe wird beauftragt, **Phase 0** (Fluchtweg, Eigentümer, KVR, Versicherung) durchzuführen und der Mitgliederversammlung bis **[Datum]** zu berichten.

- ☐ Ja  
- ☐ Nein  

---

## 11. Nächste Schritte nach positivem Beschluss

1. Projektgruppe benennen (innerhalb 2 Wochen).
2. Anschreiben Eigentümer/Verwaltung (Vorlage: siehe Gesprächsdokumentation / separate Mail).
3. WLAN-Messung an Kellertüren und Dach.
4. Anny Nuki-Integration in Testumgebung prüfen.
5. Termin Folgeversammlung für Go Phase 1 festlegen.

---

## Anhang A — Checkliste Kompatibilität pro Tür

Vor Bestellung je Tür ausfüllen:

- [ ] Europrofil-Zylinder mit **Not- und Gefahrenfunktion**
- [ ] Abstand Schlossmitte ↔ Klinke ≥ 30 mm
- [ ] Schlüssel innen: Länge ≤ 37 mm, Breite ≤ 4 mm
- [ ] WLAN 2,4 GHz am Montageort (min. −70 dBm empfohlen)
- [ ] Keine Fluchttür / Freigabe liegt vor
- [ ] Bei Hochzieh-Drücker: Verhalten dokumentiert

---

## Anhang B — Kurzinfo für Bewohner (Entwurf Hausmitteilung)

**Neue Schlüssellösung für buchbare Räume**

Ab [Datum] erhalten Nutzer mit Anny-Buchung automatisch einen **Zugangscode** per E-Mail oder können die Tür über die Anny-App öffnen. Die **Haustür** kann zusätzlich mit einem **gemeinsamen Bewohner-PIN** am Keypad genutzt werden (falls beschlossen).

**Wichtig:** Eure **normalen Hausschlüssel** funktionieren weiter. Im Notfall öffnet ihr Türen wie bisher von innen mit der **Klinke** bzw. dem Drehknauf am Nuki.

Bei Fragen: [Kontakt Projektgruppe]

---

*Dieses Dokument dient der Entscheidungsfindung im Bewohnerverein und ersetzt keine rechtsverbindliche Prüfung durch Eigentümer, Bauaufsicht oder Versicherer.*
