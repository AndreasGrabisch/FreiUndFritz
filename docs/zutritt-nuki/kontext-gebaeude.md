# Kontext: Gebäude, Türen, Nutzung

Kanonische Fakten für alle Unterlagen. **Stand:** Planung 2026.

---

## Haus und Bewohner

| Merkmal | Wert |
|---------|------|
| **Standort** | München, Bayern — **Arnulfstr. 55**, Haus **Neuhausen**, Kreativquartier (Projekt WUP, 56 WE) |
| **Träger** | Postbaugenossenschaft (über Hausverwaltung) |
| **Entscheidung Zutritt** | **Bewohnerverein** (nicht WEG-Eigentümerbeschluss) |
| **Parteien** | **56 WE** laut Zugangsschema / Bauschriftfeld (Planungstexte nannten zuvor ca. 50) |
| **Buchungssystem** | **Anny** (bereits gekauft/im Einsatz) |
| **Geplante Technik** | **Nuki Smart Lock Pro** + **Keypad**, Anny-Integration |
| **Software im Repo** | [`freiundfritz`](../../freiundfritz/) — Anny + Door Lock (Nuki Web API) |

Öffentliche oder halböffentliche **Anny-Buchungen** für: Apartment (Dach), Musikraum, Kreativraum, Veranstaltungsraum (max. ca. 50 Personen).

---

## Fünf verdrahtete Türen (Zugangsschema + Brandschutz)

Quellen: [analyse-fluchtwege.md](analyse-fluchtwege.md), [anlagen/Zugangsschema_WUP.pdf](anlagen/Zugangsschema_WUP.pdf).

| Tür | Bau-ID | Lage | Rettungsweg | Nuki-Planung |
|-----|--------|------|-------------|--------------|
| **Apartment** | NH_5_02 | 5. OG, 85,34 m² | **1. RW** der Wohnung zur Treppe; **2. RW** Fenster/Hubrettung | **Phase 1 Pilot** |
| **Musikraum** | SB_-1_01_G | UG, Hobby, T30-RS | **1. RW** in den Kellerflur | Phase 2, Zylinder + T30-RS offen |
| **Kreativraum/Werkraum** | SB_-1_02_G | UG, Hobby, T30-RS | **1. RW** in den Kellerflur | Phase 2, wie Musik |
| **Veranstaltung** | SB_-1_03_G | UG, NE_1_04 122,74 m², max. 100 Personen | **1. RW** T30-RS in den Flur; **2. RW** Glastür Lichthof | Innentür Phase 3 nur über Öffner/Klärung |
| **Flur außen (Kellergang)** | SB_-1_07 | UG → Hof | **kein** Fluchtweg (Gröpke + Plan: 2. RW des Saals ist die Lichthof-Tür) | Phase 3 Gästezugang, Zylinder/Einsperrung |
| **Glastüren VR → Lichthof** | — | „Tür erforderlich“, 2. RW | **Rettungsweg** | **Kein Nuki, kein UniFi** |
| **Haustür EG** | — | nicht im Zugangsschema | nicht auf diesen Ausschnitten | nicht vorverdrahtet |

---

## Kellergang als Gäste-Haupteingang

Langfristig sollen Gäste **primär über den Kellergang** ins Gebäude und zu den buchbaren Räumen — nicht zwingend über die Haustür.

**Aktuell:** Der Zugang über den Kellergang ist wegen einer **Nachbarbaustelle** **nicht nutzbar**. Der **Apartment-Pilot** (nur Dach-Tür) kann unabhängig starten; Gäste erreichen das Apartment bis dahin **manuell** (z. B. Haustür, Schlüsselübergabe).

**Anny Zielbild (später):** Buchung → Zugang **Kellergang-Haupteingang** + Zielraum (Apartment oder Kellerraum).

---

## Kellertür nach draußen (VR / Kellergang)

**Ist-Zustand (vor Ort):**

- Abschließen nur **von außen** mit Schlüssel.
- Innen: **Klinke**; Schlüssel **innen nicht drehbar**.
- Wenn **von außen zugesperrt**: Tür lässt sich **von innen nicht öffnen** (laut Beobachtung).

**Folgen:**

| Thema | Einschätzung |
|-------|----------------|
| **Nuki** | **Nicht möglich** ohne Zylinderumbau (kein drehbarer Schlüssel innen). |
| **Sicherheit / Fluchtweg** | **Dringend klären** mit Postbaugenossenschaft — Einsperrgefahr in Aufenthaltsräumen. |
| **Baurecht** | Nicht automatisch „Mangel“; kann defekter Zylinder oder Missverständnis sein — **fachlich prüfen**. |

---

## Veranstaltungsraum (VR)

- **Glastüren zum Hof:** Rettungsweg — **definitiv kein Nuki**, keine elektrische Verriegelung.
- **Rechtliches Risiko:** Raum kann als **Veranstaltungsort** gelten (LStVG, ggf. Nutzungsänderung) — siehe [rechtliches.md](rechtliches.md). Unabhängig von Smart Locks.
- **Kellergang-Tür am VR:** erst nach Zylinder-, Sicherheits- und Rechtsklärung.

---

## Offene technische Tests (Keller)

An **allen Kellertüren** unklar, ob Nuki funktioniert: **Schlüssel muss innen stecken und drehbar sein**. Bisher nur **ein Schlüssel** pro Raum — Test mit Zweitschlüssel oder Montageprobe **vor Bestellung** nötig.

**Apartment:** sehr wahrscheinlich kompatibel (normale Wohnungstür; Referenz: Nuki funktioniert in vergleichbarer Wohnung im Haus).

---

## Projektzeitrahmen

- **Gesamtumsetzung:** max. **2 Monate** ab Vereinsbeschluss
- **Pilot:** nur **Apartment** (Budget ca. **600 €** inkl. Internet/WLAN; Anny nicht im Budget)
