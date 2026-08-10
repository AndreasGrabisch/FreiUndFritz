# Projektplan: Elektronische Zutrittskontrolle mit Nuki

**Version:** 1.3 · **August 2026** · Zur Entscheidung: Bewohnerverein · München, Bayern

---

## 1. Zusammenfassung für die Entscheidung

Wir schlagen vor, buchbare Zugänge im Haus schrittweise mit **Nuki Smart Lock Pro** und **Nuki Keypad** zu automatisieren und an unser bestehendes Buchungssystem **Anny** anzubinden. Gäste erhalten nach einer bestätigten Buchung automatisch einen **zeitlich begrenzten Zugang** (PIN oder App) — ohne dass jemand physisch einen Schlüssel übergeben muss.

Der **Bewohnerverein** trifft die Grundsatz- und Budgetentscheidung. Die **Postbaugenossenschaft** als Träger des Gebäudes muss für Montagen an gemeinschaftlichen Türen fachlich zustimmen bzw. Fluchtweg- und Zylinderfragen klären (siehe Checkliste im Anhang). Eine Zustimmung durch den Eigentümer im WEG-Sinne ist **nicht** vorgesehen — der Verein handelt im Rahmen seiner Satzung und der mit der Genossenschaft vereinbarten Nutzung.

| | |
|---|---|
| **Vollausbau (5 Türen)** | ca. **2.000–2.500 €** einmalig (Referenz, spätere Phasen) |
| **Pilot (nur Apartment)** | ca. **470–570 €** (Kap. 7) — **Anny ist bereits gekauft** und nicht Bestandteil des Pilot-Budgets |
| **Laufende Kosten Nuki** | **0 €** Nutzer-Abo; Wartung im Ehrenamt |
| **Umsetzung gesamt** | **max. 2 Monate** ab Vereinsbeschluss (Klärung und Pilot teilweise parallel) |

**Pilot Phase 1** beschränkt sich bewusst auf die **Apartment-Tür im Dachgeschoss** — unsere wichtigste und umsatzstärkste Anny-Ressource. **Haustür** und **Kellergang-Haupteingang** sind **nicht** Teil des Pilots: Der Kellergang soll langfristig der **Hauptzugang für Gäste** werden (direkter Weg zu Kellerräumen und später zum Apartment), ist aber derzeit wegen einer **Nachbarbaustelle** ohnehin nicht nutzbar. Der Pilot kann unabhängig davon starten; Gäste erreichen das Apartment bis zur Freigabe des Kellergangs wie bisher über den manuellen Zugang (z. B. Haustür, Schlüsselübergabe).

**Offene technische Punkte** betreffen vor allem **Kellertüren** (Schlüssel innen drehbar?) und die **Kellertür nach draußen** am Veranstaltungsraum (Sicherheit, Fluchtweg, Nuki-Unverträglichkeit). Diese dürfen den Apartment-Pilot **nicht blockieren**, müssen aber vor jedem weiteren Ausbau geklärt sein.

**Beschluss wird erbeten zu:** Grundsatz (Antrag A), Budget Pilot (Antrag B), optional Vollausbau-Obergrenze (Antrag C), Mandat Checkliste/Klärung (Antrag D).

---

## 2. Ausgangslage und Ziele

### 2.1 Haus und Nutzer

Das Haus umfasst **ca. 50 Parteien** (Wohnungen bzw. Haushalte). Zusätzlich werden über **Anny** öffentlich oder halböffentlich buchbar:

- das **Apartment** im Dachgeschoss,
- der **Musikraum** und **Kreativraum** im Keller,
- der **Veranstaltungsraum** im Keller (Veranstaltungen mit bis zu ca. 50 Personen).

Der Bewohnerverein betreibt die Buchungsinfrastruktur und soll die Zutrittsautomatisierung **in Eigenregie** (DIY-Montage, Anny-Administration) umsetzen, soweit die Postbaugenossenschaft mitspielt.

### 2.2 Fünf relevante Türen

| Tür | Lage | Nutzung heute | Nuki-Planung |
|-----|------|---------------|--------------|
| **Haustür** | Hauseingang | Zugang für Bewohner und derzeit auch Gäste | Phase 2, nach Pilot |
| **Veranstaltungsraum — Glastüren** | Keller → Hof | Rettungsweg / Notausgang | **Kein Nuki, ohne Ausnahme** |
| **Veranstaltungsraum — Kellergang** | Keller → Kellergang/Außen | Künftiger **Hauptgästezugang**; derzeit Baustelle | Phase 3, nur nach Klärung |
| **Musikraum** | Keller | Buchbar | Phase 2, nach Zylinder-Test |
| **Kreativraum** | Keller | Buchbar | Phase 2, nach Zylinder-Test |
| **Apartment** | Dach | Buchbar, wichtigste Ressource | **Phase 1 Pilot** |

**Ist-Zustand Zutritt:** Nach Bestätigung einer Anny-Buchung erfolgt die Schlüsselübergabe manuell (Vereinsmitglied, Schlüsseltresor o. Ä.). Das bindet Kapazität, verzögert spontane Buchungen und skaliert schlecht bei steigender Nachfrage — insbesondere beim Apartment.

### 2.3 Ziele des Projekts

1. **Automatischer Zutritt** im Buchungszeitraum (PIN per E-Mail, Anny-App oder Remote Open).
2. **Mechanische Schlüssel** für Bewohner und Notfälle bleiben erhalten — Nuki ergänzt, ersetzt nicht.
3. **Keine laufenden Nutzergebühren** pro Partei oder Gast (im Gegensatz zu KleverKey, Tapkey u. Ä.).
4. **Selbstmontage** wo möglich; keine aufwendige Verkabelung.
5. **Fluchtwege und baurechtliche Vorgaben** einhalten; **keine Smart Locks an Glastüren** des Veranstaltungsraums.
6. **Entscheidungen durch den Verein**; fachliche Abstimmung mit der **Postbaugenossenschaft** vor Montage.

---

## 3. Technische Voraussetzungen und offene Punkte

### 3.1 Funktionsweise Nuki (kurz)

Das **Nuki Smart Lock Pro** wird **innen** am vorhandenen **Europrofil-Zylinder** montiert. Ein kleiner Motor dreht den **von innen eingesteckten Schlüssel**. Von außen öffnet man per **Keypad-PIN**, per App (Bluetooth vor Ort) oder per **Fernfreigabe** (WLAN). Der **mechanische Schlüssel** funktioniert weiterhin — innen und außen — unabhängig vom Nuki.

**Konsequenz:** An jeder Tür, an der Nuki montiert werden soll, muss ein Schlüssel **dauerhaft innen stecken** und vom Nuki **frei drehbar** sein. Ist das nicht der Fall, ist Nuki **ohne Zylinderumbau** nicht einsetzbar.

| Voraussetzung | Status / nächster Schritt |
|---------------|---------------------------|
| Schlüssel innen steckend und drehbar | **Apartment:** sehr wahrscheinlich ja (normale Wohnungstür wie in anderen Wohnungen des Hauses; in einer Referenzwohnung funktioniert Nuki bereits) · **Kellertüren:** **ungetestet** — bisher nur je **ein** Schlüssel verfügbar; Test mit Zweitschlüssel, Leihschlüssel vom Hausmeister oder Nuki-Kompatibilitätscheck nötig |
| Not- und Gefahrenzylinder | Muss je Tür bestätigt werden (Öffnen von innen ohne Schlüssel im Notfall) |
| Nuki-Maße | Abstand Schlossmitte ↔ Klinke ≥ 30 mm; Schlüssel innen ≤ 37 mm Länge, ≤ 4 mm Breite |
| **Internet / WLAN 2,4 GHz** | Für Anny-Fernfreigabe und automatische PIN-Vergabe erforderlich; am Apartment messen, ggf. Repeater |
| Glastüren Veranstaltungsraum | **Kein Nuki** — Rettungsweg |

### 3.2 Kellertür nach draußen (Kellergang — künftiger Gäste-Haupteingang)

**Beschreibung Ist-Zustand:** Die Tür vom Veranstaltungsraum bzw. Kellergang **nach draußen** (Richtung Außenbereich / später Hauptweg für Gäste) lässt sich derzeit **nur von außen mit Schlüssel abschließen**. Innen ist eine **Türklinke** montiert; der **Schlüssel lässt sich von innen nicht drehen**. Nach Beobachtung vor Ort gilt zusätzlich: **Wenn von außen zugesperrt wurde, lässt sich die Tür von innen nicht öffnen** — die Klinke öffnet in diesem Zustand offenbar nicht.

| Frage | Ausführliche Einschätzung |
|-------|---------------------------|
| **Ist Nuki möglich?** | **Nein** im Ist-Zustand. Nuki benötigt innen einen steckenden, motorisch drehbaren Schlüssel. Ohne innen drehbaren Zylinder ist keine Montage möglich — außer nach **fachgerechtem Zylinderumbau** durch Schließer/Genossenschaft. |
| **Ist das ein Sicherheitsmangel?** | **Dringend mit der Postbaugenossenschaft klären.** Für Türen entlang von **Fluchtwegen** oder zu **Aufenthaltsräumen** gilt: Personen im Inneren müssen die Tür **jederzeit von innen ohne Schlüssel** verlassen können. Eine Tür, die nach Abschließen von außen **von innen nicht zu öffnen** ist, birgt im Ernstfall **Einsperrgefahr** (Feuer, Notfall, medizinischer Vorfall). Das ist **nicht** mit üblichen Anforderungen an Rettungswege vereinbar — unabhängig von Nuki. Mögliche Erklärungen, die geklärt werden müssen: (a) **defekter oder falscher Zylinder**, (b) **fehlende Gefahrenfunktion**, (c) **Missverständnis** über die Bedienung (Fallenbolt vs. Klinke), (d) historisch so eingebaut und nie beanstandet. Bis zur schriftlichen Klärung: **keine Nachrüstung**, **kein Nuki**, ggf. **sofortige Prüfung** ob der Veranstaltungsraum so überhaupt sicher nutzbar ist. |
| **Gästezugang** | Langfristig ist diese Tür der **bevorzugte Haupteingang für Gäste** (kürzerer Weg zu Kellerräumen, später Anny-Regel „Kellergang + Zielraum“). Durch die **Nachbarbaustelle** ist dieser Weg **derzeit gesperrt**; Gäste nutzen andere Zugänge. Der **Apartment-Pilot** hängt nicht davon ab. |

### 3.3 Veranstaltungsraum — rechtliches und organisatorisches Risiko

Der Veranstaltungsraum ist das **komplexeste Teilprojekt** — nicht wegen der Technik allein, sondern wegen der **rechtlichen Einordnung** als möglicher **Veranstaltungsort**.

**Art. 19 Bayerisches Landesstraf- und Verordnungsgesetz (LStVG):** Wer **öffentliche Vergnügungen** veranstaltet (z. B. Konzerte, Lesungen, Feiern mit externen Gästen gegen Entgelt oder mit Eintritt), muss dies **beim Kommunalreferat (KVR) in München anzeigen**. Öffentliche **Anny-Buchungen** für den VR fallen hierunter, sobald externe Nutzer zugelassen werden — **unabhängig davon**, ob Nuki installiert ist.

**Nutzungsänderung / Versammlungsstätte:** Wird der Raum **regelmäßig** und **gewerbsmäßig** für Veranstaltungen genutzt (Orientierung in Bayern: u. a. mehr als **5 Veranstaltungen pro Jahr** mit Eintritt oder Eintrittsersatz), kann eine **genehmigungspflichtige Nutzungsänderung** oder die Einordnung als **Versammlungsstätte** relevant werden. Das löst zusätzliche Anforderungen an Fluchtwege, Beschilderung, Brandschutz aus — **weit über Nuki hinaus**.

**§ 47 Versammlungsstättenverordnung (VStättV):** Pflicht zur Erlaubnis als Versammlungsstätte bei **über 200 Besuchern**. Bei maximal ca. **50 Personen** im VR voraussichtlich **nicht** einschlägig. Dennoch: ab **100 m²** Nutzfläche können **zwei voneinander unabhängige Ausgänge** relevant werden — **Raumgröße** sollte ermittelt werden.

**Glastüren zum Hof:** Diese Türen sind **Rettungsweg** und werden **definitiv nicht** mit Nuki nachgerüstet. Eine elektrische Verriegelung würde den Fluchtweg gefährden und ist ohne behördliche Sonderlösung ausgeschlossen.

**Kellergang-Tür:** Selbst wenn Zylinder und Fluchtweg geklärt sind, sollte der **öffentliche VR-Betrieb** rechtlich **abgesichert** sein, bevor Phase 3 startet. Nuki **verschärft** die rechtliche Lage nicht, **löst** sie aber auch **nicht**.

**Fazit VR:** Höchstes **Risiko** im Gesamtprojekt. Empfehlung: VR-Ausbau (Phase 3) erst nach **abgeschlossener Checkliste** inkl. LStVG, Nutzungsart, Postbaugenossenschaft und Fluchtweg.

### 3.4 Apartment als Pilot

Das Apartment ist die **wichtigste Anny-Ressource** und vermutlich technisch am unkompliziertesten (normale Wohnungstür, Referenzerfahrung im Haus). Der Pilot dient dazu:

- Anny-Nuki-Integration **in der Praxis** zu testen (PIN-Versand, Zeitfenster, Remote Open),
- den **Gästeablauf** zu erproben und Dokumentation/Hausregeln anzupassen,
- **WLAN/Internet** am Montageort zu validieren,
- dem Verein **Erfahrungswerte** für Phase 2+ zu liefern.

Im Pilot wird **nur die Apartment-Tür** elektrifiziert — **nicht** Haustür oder Kellergang.

---

## 4. Lösungskonzept: Nuki + Anny

### 4.1 Komponenten

- **Nuki Smart Lock Pro (5. Gen):** Montage innen am Zylinder; Motor dreht den Schlüssel; manueller Drehknauf am Nuki bleibt als Fallback.
- **Nuki Keypad 2:** Montage außen am Türrahmen; **6-stellige PIN** für Gäste ohne Smartphone.
- **WLAN 2,4 GHz:** Verbindung zur Nuki-Cloud für Fernsteuerung und Anny-Anbindung.
- **Anny** (bereits im Einsatz, Kosten nicht Teil des Pilot-Budgets): Bei Buchung werden **zeitlich begrenzte Zugänge** erzeugt; Gäste können in der Anny-App **Remote Open** nutzen, sofern konfiguriert.

### 4.2 Zugangslogik nach Ausbaustufe

| Nutzergruppe | Pilot (nur Apartment) | Später (Zielbild) |
|--------------|----------------------|-------------------|
| **Bewohner** | Unverändert mechanische Schlüssel | Wie bisher; optional später gemeinsamer Keypad-PIN an Haustür |
| **Anny-Gast Apartment** | PIN / App nur **Apartment-Tür**; Weg ins Haus **manuell** (Schlüsselübergabe, Begleitung o. Ä.) | Kellergang-Haupteingang + Apartment (wenn freigegeben) |
| **Anny-Gast Kellerraum** | Noch manuell | Kellergang + Zielraum (wenn freigegeben) |
| **Notfall** | Klinke / Nuki-Drehknauf innen; mechanischer Schlüssel | Wie bisher an allen Türen |

**Anny-Regeln (Beispiel Zielbild):** Apartment-Buchung → Schlösser „Kellergang-Haupteingang“ + „Apartment“ · Musikraum → Kellergang + Musikraum · Zeitfenster z. B. **15 Minuten vor** bis **15 Minuten nach** Buchungsende (in Anny einstellbar).

### 4.3 Was bewusst ausgeschlossen ist

- **Glastüren Veranstaltungsraum:** kein Nuki, keine elektrische Verriegelung.
- **Kellergang-Tür:** kein Nuki bis Zylinder-, Sicherheits- und Fluchtwegklärung.
- **Haustür im Pilot:** bewusst zurückgestellt — geringerer Testnutzen, höhere organisatorische Tragweite (50 Parteien).

---

## 5. Warum nicht die Alternativen?

Es wurden mehrere Systeme geprüft. Für unser Haus mit **ca. 50 Parteien**, **Anny-Buchungen**, **DIY-Ansatz** und **Zylinder-Türen** scheitern die Alternativen vor allem an **Kosten**, **Integration** oder **falscher Produktkategorie**.

| System | Ausführliche Begründung der Ablehnung |
|--------|--------------------------------------|
| **KleverKey** | Elektronische Zylinder mit App-Zugang; Anny-Integration vorhanden. **Aber:** Abo-Modell pro Nutzer/Berechtigung. An der **Haustür** mit **50 Parteien** und vielen Gästen laufen die **Jahreskosten** deutlich höher als bei Nuki (0 €). Zudem **kompletter Zylinderersatz** — kein Nachrüsten am bestehenden Schlüssel. Für einzelne Kellerräume mit wenigen Nutzern denkbar; als **Einheitssystem für das ganze Haus** wirtschaftlich unattraktiv. |
| **UniFi Door Access** | Professionelles Zutrittssystem von Ubiquiti für **Gewerbe** und große Anlagen. Erfordert **Verkabelung (PoE)**, Türleser, Controller — **kein** Euro-Zylinder-Nachrüstsatz. **Hohe Einmalkosten**, **keine native Anny-Integration**, typischerweise **Türöffner/Magnete** statt Klinke — **unpassend für Fluchtwege** mit bestehender Klinke. Sinnvoll nur bei bestehender UniFi-Infrastruktur und Facility-Team — **Overkill** für unseren Verein. |
| **Tapkey** | Cloud-Zylinder mit **Nutzerpaketen**; Kosten skalieren mit Anzahl Berechtigungen — **ähnliches Problem wie KleverKey** bei vielen Parteien und Gästen. |
| **EVVA AirKey** | Hybridsystem mit elektronischen Schlüsseln (KeyCredits), Fachbetrieb-Montage. Gut für **verwaltete MFH** mit **dauerhaften** Schließrechten; **schlecht** für **kurzzeitige Gast-PINs** über Anny. Würde ein **Zweitsystem** neben Anny-Nuki bedeuten oder hohe Credit-Kosten. |
| **dormakaba Exivo** | Premium-Smart-Lock-Linie; **keine transparenten Preise**, nur autorisierte Partner, **monatliches Service-Abo** — für einen kostenbewussten Verein ohne Schließer-Vertrag ungeeignet. |
| **Salto KS / Salto Space** | Hotel- und Bürostandard; teure Infrastruktur, professionelle Administration, **keine praktikable Anny-Anbindung** — falsche Produktkategorie. |

**Nuki** ist das einzige geprüfte System, das **Anny-native Buchungs-PINs**, **kein Nutzer-Abo**, **Nachrüstung am vorhandenen Zylinder**, **DIY** und **parallele mechanische Schlüssel** vereint — **sofern** der Zylinder es technisch zulässt.

---

## 6. Phasenplan (max. 2 Monate)

| Phase | Dauer | Inhalt im Detail |
|-------|-------|------------------|
| **0 — Klärung** | Woche 1–3 (parallel zum Pilot-Start möglich) | Checkliste Anhang abarbeiten: Postbaugenossenschaft ansprechen, Fluchtwegplan, Versicherung, VR-Rechtliches, Zylinder-Tests Keller, WLAN-Messungen, Projektgruppe benennen |
| **1 — Pilot** | Woche 2–6 | **Nur Apartment:** Nuki + Keypad kaufen und montieren, Internet/WLAN sicherstellen, Anny-Regel anlegen, interne und externe Testbuchungen, Gästeanleitung (Hinweis: Hauszugang weiterhin manuell), 2 Wochen Probebetrieb |
| **2 — Ausbau** | Woche 5–8 | Nach positivem Pilot und **erneutem Vereinsbeschluss:** Haustür, Musikraum, Kreativraum — jeweils nur nach bestandenem Türtest |
| **3 — VR + Kellergang** | nach Freigabe | Nur **Kellergang-Tür** (nicht Glastüren); nur wenn Zylinder, Fluchtweg, Sicherheit und **VR-Rechtliches** geklärt; Baustelle am Kellergang frei |
| **4 — Betrieb** | dauerhaft | Akku alle 4–6 Monate laden (App-Warnung), abgelaufene Nuki-Zugänge prüfen (Limit 200 pro Schloss), Ansprechpartner für Störungen: [Name, Kontakt] |

**Meilenstein Pilot:** Mindestens zwei Wochen stabiler Betrieb mit echten Apartment-Buchungen; dokumentierter Bericht an den Verein.

---

## 7. Kosten

### 7.1 Pilot (nur Apartment)

| Position | Richtwert | Anmerkung |
|----------|-----------|-----------|
| Nuki Smart Lock Pro 5. Gen | ca. 269 € | Einmalig; kein Abo nötig für Anny-Betrieb |
| Nuki Keypad 2 | ca. 150 € | Gast-PIN von außen |
| **Internet / WLAN** | ca. 50–120 € | z. B. WLAN-Repeater, falls Signal am Apartment schwach; oder Nutzung bestehendes Wohnungs-WLAN |
| Reserve (Batterien, Kleinteile) | ca. 30 € | Keypad batteriebetrieben; Nuki Akku |
| **Summe Pilot** | **ca. 470–570 €** | Budget-Vorschlag **max. 600 €** inkl. Puffer |
| **Anny** | **0 € im Pilot-Budget** | Bereits gekauft und im laufenden Betrieb eingeplant |

### 7.2 Vollausbau (Referenz, spätere Phasen)

| Position | Summe |
|----------|-------|
| 5× Lock Pro + 5× Keypad + Reserve | ca. 2.195 € |
| WLAN-Repeater Keller/Dach (falls nötig) | 50–120 € pro Gerät |
| Nuki Nutzer-Abo | **0 €** |

**Nicht enthalten:** Schließer oder Elektriker (Zylinderumbau Kellergang, Sonderfälle), baurechtliche Gutachten, Anny-Lizenz (bereits vorhanden).

---

## 8. Rechtliches und Zuständigkeiten

| Thema | Ausführung |
|-------|------------|
| **Beschluss / Freigabe** | Der **Bewohnerverein** beschließt Grundsatz, Budget und Phasen. Das ist die maßgebliche Vereinsentscheidung — **nicht** eine separate Eigentümer-Freigabe im WEG-Sinne. |
| **Postbaugenossenschaft** | Als **Träger des Gebäudes** muss sie Fluchtweg-, Zylinder- und Nutzungsfragen **mittragen**; schriftliche Zustimmung vor Montage an gemeinschaftlichen Türen einholen (Checkliste). |
| **Art. 19 LStVG** | Bei **öffentlichen** Anny-Buchungen (VR, ggf. andere Räume): **Anzeige beim KVR München** — unabhängig von Nuki. |
| **VR als Veranstaltungsort** | Prüfen, ob Nutzungsänderung oder Versammlungsstättenrecht greift; **vor** intensivem öffentlichen VR-Betrieb und **vor** Phase 3 klären. |
| **Fluchtweg / Smart Lock** | Keine Montage ohne erfüllte Checkliste; Glastüren ausgenommen. |
| **Versicherung** | Haftpflicht / Gebäudeversicherung informieren (Smart Lock, Vermietung Apartment). |
| **DSGVO** | Gästedaten in Anny/Nuki; Auftragsverarbeitung und Datenschutzhinweise in Buchungsablauf. |

---

## 9. Risiken und Gegenmaßnahmen

| Risiko | Auswirkung | Gegenmaßnahme |
|--------|------------|---------------|
| **VR rechtlich** als Veranstaltungsort | Bußgelder, Nutzungsuntersagung, Auflagen | LStVG-Anzeige, Nutzungsklärung mit Postbaugenossenschaft **vor** öffentlichem VR-Ausbau |
| **Kellergang-Tür:** Einsperrung von innen | Gefahr für Personen im VR / Keller | **Sofort** mit Postbaugenossenschaft und Fluchtwegplan klären; kein Nuki; ggf. Zylinder tauschen |
| **Kellertüren:** Schlüssel innen nicht drehbar | Nuki nicht montierbar | Türtest **vor** Bestellung; Tür aus Plan streichen oder Zylinder anpassen |
| **Kellergang gesperrt** (Baustelle) | Gäste können Hauptweg nicht nutzen | Pilot Apartment trotzdem; Anny-Regeln erst erweitern wenn Weg frei |
| **200-Zugangs-Limit** pro Nuki | Neue Buchung schlägt fehl | Abgelaufene Zugänge löschen; nicht alle 50 Parteien digital am Schloss hinterlegen |
| **WLAN-Ausfall** | Kein Remote Open / Anny-Sync | PIN/Bluetooth vor Ort; mechanischer Schlüssel |
| **Leerer Nuki-Akku** | Motor öffnet nicht | Manuell am Nuki-Knauf; App warnt rechtzeitig |
| **Gäste verstehen Zugang nicht** | Supportaufwand, schlechte Bewertungen | Klare Anny-Mail; Hinweis auf manuellen Hauszugang im Pilot |

---

## 10. Beschlussvorlagen für die Mitgliederversammlung

### Antrag A — Grundsatz

> Der Bewohnerverein befürwortet die schrittweise Einführung elektronischer Zutrittskontrolle auf Basis **Nuki Smart Lock Pro** und **Nuki Keypad** in Verbindung mit **Anny**, vorbehaltlich der Checkliste (Anhang) und eines **gesonderten Vereinsbeschlusses** für jede Ausbaustufe nach dem Pilot.

☐ Ja · ☐ Nein

### Antrag B — Budget Pilot

> Für **Phase 1 (Pilot)** wird ein Budget von **max. 600 €** für die **Apartment-Tür** (Nuki Smart Lock Pro, Keypad, Internet/WLAN-Anschluss) freigegeben. **Anny** ist bereits beschafft und nicht Teil dieses Budgets.

☐ Ja · ☐ Nein · ☐ Abweichender Betrag: _______ €

### Antrag C — Budget Vollausbau (optional)

> Für den **Vollausbau** aller nach Checkliste freigegebenen Türen (bis zu 5) wird eine **Obergrenze von max. 2.500 €** (inkl. WLAN-Nachrüstung) bestätigt. Einzelentscheidungen je Phase bleiben dem Verein vorbehalten.

☐ Ja · ☐ Nein · ☐ Nur Pilot, weitere Entscheidung später

### Antrag D — Mandat Klärung

> Die Projektgruppe wird beauftragt, die **Checkliste (Anhang)** bis **[Datum]** abzuarbeiten und dem Verein schriftlich zu berichten — insbesondere Fluchtwege, Kellertür nach draußen, Veranstaltungsraum-Rechtliches, Zylinder-Tests Keller und Abstimmung mit der **Postbaugenossenschaft**.

☐ Ja · ☐ Nein

---

## Anhang — Checkliste vor Montage / Ausbau

Die Checkliste wird vom **Verein** beauftragt. Fachliche Stellungnahmen (Fluchtweg, Zylinder) liegen bei der **Postbaugenossenschaft** bzw. ggf. Schließer/Brandschutz.

### Organisation & Freigaben

- [ ] **Beschluss Bewohnerverein** zu Grundsatz, Budget und Phase (Protokoll)
- [ ] **Abnahme / Zustimmung Postbaugenossenschaft** schriftlich — pro Tür oder als Gesamtkonzept für Zutrittsautomatisierung
- [ ] **Versicherung** (Haftpflicht, ggf. Gebäude) informiert; Stellungnahme zu Smart Locks und **Vermietung Apartment** eingeholt
- [ ] **Projektgruppe** benannt: Projektleitung, Technik, Anny-Admin, Stellvertretung — Namen und Kontakt dokumentiert
- [ ] **Hausordnung / Nutzungsregeln** geprüft, ob Anpassung für elektronischen Zutritt nötig

### Fluchtweg & Sicherheit

- [ ] **Flucht- und Rettungswegplan** bei Postbaugenossenschaft eingesehen; alle betroffenen Türen aufgelistet
- [ ] **Glastüren Veranstaltungsraum** (Hof): schriftlich bestätigt — **kein Nuki**, keine elektrische Verriegelung
- [ ] **Kellertür nach draußen** (Kellergang, künftiger Gäste-Hauptweg):
  - [ ] Zylinder-Typ und Funktion dokumentiert (innen/außen drehbar?)
  - [ ] **Öffnung von innen** bei Abschluss von außen **getestet** und bewertet
  - [ ] Stellungnahme Postbaugenossenschaft: Fluchtweg, Einsperrgefahr, Handlungsbedarf
  - [ ] **Baustellensituation** Nachbargrundstück: wann ist Kellergang wieder als Gästezugang nutzbar?
- [ ] Bei allen Rettungsweg-Türen: **Not- und Gefahrenfunktion** des Zylinders dokumentiert

### Technik je geplanter Tür

- [ ] **Türtest / Zylinder:** Mit **zweitem Schlüssel** oder Nuki-Kompatibilitätscheck prüfen, ob Schlüssel innen steckend **vom Motor drehbar** wäre
- [ ] **Nuki-Maße:** Abstand Klinke ≥ 30 mm; Schlüssel innen ≤ 37 × 4 mm; Hochzieh-Drücker-Verhalten notiert
- [ ] **Internet / WLAN 2,4 GHz** am Montageort gemessen (min. ca. −70 dBm empfohlen); Repeater oder Verstärkung eingeplant
- [ ] **WLAN-Zugang** für Nuki geklärt (Wohnungs-WLAN Apartment, Gast-Netz, Passwort-Verwaltung)
- [ ] **Fallback** dokumentiert: mechanischer Schlüssel, manueller Nuki-Knauf, Ansprechpartner bei Störung

### Veranstaltungsraum — Rechtliches

- [ ] **Art. 19 LStVG:** Anzeige beim **KVR München** für öffentliche Vergnügung vorbereitet oder eingereicht (Status: ☐ offen ☐ eingereicht ☐ nicht nötig nach Rücksprache)
- [ ] **Nutzungsart VR** geklärt: reiner Gemeinschaftsraum vs. **öffentlicher Veranstaltungsort** — Rücksprache Postbaugenossenschaft und ggf. Bauordnung
- [ ] **Häufigkeit und Art** geplanter Veranstaltungen dokumentiert (Anzahl/Jahr, Eintritt, externe Gäste, Öffnungszeiten)
- [ ] **Raumgröße** (m²) ermittelt; bei >100 m²: **zweiter Ausgang** / Fluchtwegbreite prüfen
- [ ] **Buchungsbedingungen und Hausordnung** um VR-Hinweise ergänzt (Fluchtweg, max. Personen, Verhalten bei Alarm)
- [ ] Entscheidung dokumentiert: **öffentlicher VR-Betrieb** erst nach rechtlicher Klärung

### Pilot Apartment (Phase 1)

- [ ] Technik-Checkliste **nur für Apartment-Tür** vollständig
- [ ] Hardware beschafft (Lock Pro, Keypad, ggf. Repeater) innerhalb Budget
- [ ] Montage und Einrichtung in Nuki-App; Test Remote Open und Keypad-PIN
- [ ] **Anny-Regel** angelegt: **nur Apartment-Schloss** (kein Kellergang, keine Haustür)
- [ ] **Gästeanleitung** in Anny-Bestätigungsmail: Zugang **nur Apartment-Tür**; **Hauszugang weiterhin manuell** bis Kellergang frei
- [ ] Mindestens **2 interne + 2 externe Testbuchungen**; PIN-Zustellung und Zeitfenster geprüft
- [ ] **2 Wochen Probebetrieb**; Störungen protokolliert

### Nach Pilot (vor Phase 2 und höher)

- [ ] **Schriftlicher Pilotbericht** an Verein (Technik, Gästefeedback, Kosten, Empfehlung)
- [ ] **Erneuter Vereinsbeschluss** für jede weitere Tür (Haustür, Musikraum, Kreativraum, Kellergang, VR)
- [ ] Checkliste **für jede neue Tür** von vorn durchgehen
- [ ] Anny-Regeln erweitern (z. B. Kellergang + Zielraum), sobald technisch und rechtlich möglich

---

*Dieses Dokument dient der Entscheidungsfindung im Bewohnerverein. Es ersetzt keine rechtsverbindliche Prüfung durch die Postbaugenossenschaft, einen Schließer, die Bauaufsicht oder Versicherer.*
