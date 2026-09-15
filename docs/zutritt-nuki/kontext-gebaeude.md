# Kontext: Gebäude, Türen, Nutzung

Kanonische Fakten für alle Unterlagen. **Stand:** Planung 2026.

---

## Haus und Bewohner

| Merkmal | Wert |
|---------|------|
| **Standort** | München, Bayern |
| **Träger** | Postbaugenossenschaft (über Hausverwaltung) |
| **Entscheidung Zutritt** | **Bewohnerverein** (nicht WEG-Eigentümerbeschluss) |
| **Parteien** | ca. **50** (Wohnungen/Haushalte) |
| **Buchungssystem** | **Anny** (bereits gekauft/im Einsatz) |
| **Geplante Technik** | **Nuki Smart Lock Pro** + **Keypad**, Anny-Integration |
| **Software im Repo** | [`freiundfritz`](../../freiundfritz/) — Anny + Door Lock (Nuki Web API) |

Öffentliche oder halböffentliche **Anny-Buchungen** für: Apartment (Dach), Musikraum, Kreativraum, Veranstaltungsraum (max. ca. 50 Personen).

---

## Fünf relevante Türen

| Tür | Lage | Rolle | Nuki-Planung |
|-----|------|-------|--------------|
| **Haustür** | Hauseingang | Bewohner, derzeit auch Gäste | Phase 2 |
| **VR — Glastüren** | Keller → Hof | Rettungsweg / Notausgang | **Kein Nuki — ausgeschlossen** |
| **VR — Kellergang** | Keller → Kellergang/Außen | **Künftiger Hauptgästezugang** | Phase 3, nur nach Klärung |
| **Musikraum** | Keller | Buchbar | Phase 2, Zylinder-Test offen |
| **Kreativraum** | Keller | Buchbar | Phase 2, Zylinder-Test offen |
| **Apartment** | Dach | Wichtigste Buchung | **Phase 1 Pilot** |

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
