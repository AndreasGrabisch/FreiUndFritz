# Technik: Nuki, Anny, Zylinder, Grenzen

---

## Nuki Smart Lock Pro — Prinzip

- Montage **innen** am **Europrofil-Zylinder**.
- Motor dreht den **von innen eingesteckten Schlüssel**.
- **Klinke innen** bleibt in der Regel nutzbar (Türöffnung von innen wie gewohnt, sofern Zylinder/Notfunktion es erlauben).
- **Mechanischer Schlüssel** innen und außen bleibt möglich.
- **Keypad außen:** 6-stelliger PIN für Gäste ohne App.
- **WLAN 2,4 GHz** für Fernfreigabe und Anny-Anbindung.

**Nuki Ultra** (Zylindertausch) ist für Schließanlagen oft unpassend — Vergleichsmodell: **Pro**.

---

## Voraussetzungen je Tür

| Prüfpunkt | Anforderung |
|-----------|-------------|
| Schlüssel innen | **Steckend** und **motorisch drehbar** |
| Zylinder | **Not- und Gefahrenfunktion** empfohlen |
| Maße | Abstand Schlossmitte ↔ Klinke ≥ **30 mm**; Schlüssel innen ≤ **37 × 4 mm** |
| WLAN | Stabil **2,4 GHz** am Schloss (nicht nur im Gang messen) |
| Hochzieh-Drücker | Verhalten dokumentieren |

**Keller:** Tests noch ausstehend (nur ein Schlüssel). **Apartment:** Referenz im Haus positiv.

---

## Anny-Integration

- **Anny Professional** mit nativer [Nuki-Integration](https://docs.anny.co/de/articles/30440-nuki-integration).
- Bei Buchung: **zeitlich begrenzte Zugänge**; optional **Remote Open** in der Anny-App.
- Zeitfenster typisch: **15 Min. vor** bis **15 Min. nach** Buchungsende (konfigurierbar).

### Regeln (Beispiel Zielbild)

| Ressource | Nuki-Schlösser |
|-----------|----------------|
| Apartment | Kellergang-Haupteingang + Apartment *(wenn freigegeben)* |
| Musikraum | Kellergang + Musikraum |
| Kreativraum | Kellergang + Kreativraum |
| Veranstaltungsraum | Kellergang + VR *(nur Phase 3, nicht Glastüren)* |

### Pilot

Nur **Apartment-Schloss** — kein Kellergang, keine Haustür. Hauszugang in Gäste-Mail **manuell** erklären.

---

## Limit: 200 künftige Zugänge pro Schloss

- **Hardware-Limit pro Nuki-Schloss** (relevant für Anny-Buchungsgäste).
- Quelle: [Nuki Support — Zutrittsberechtigungen](https://help.nuki.io/hc/de/articles/4407512064785).
- **Gegenmaßnahme:** abgelaufene Zugänge löschen; **nicht** alle Parteien digital am Schloss hinterlegen.
- **Bewohner Haustür (optional später):** ein **gemeinsamer Keypad-PIN** (1 Slot) statt 50 einzelne Accounts.

---

## WLAN und Akku

- **WLAN:** Repeater bei Nuki oft problematisch; kabelgebundener AP im Keller ggf. nötig (siehe [vergleich-nuki-unifi.md](vergleich-nuki-unifi.md)).
- **Akku Nuki:** ca. **4–6 Monate** bei WLAN; App-Warnung; Fallback: Drehknauf + Schlüssel.
- **Keypad:** Batterien ca. jährlich.

---

## Software im Repository

[`freiundfritz`](../../freiundfritz/): `AccessService` prüft Anny-Buchung und löst `DoorLockController` (Nuki Web API) aus — parallel zur Anny-native Integration für eigene App/Flows.

| Umgebungsvariable | Bedeutung |
|-------------------|-----------|
| `ANNY_BASE_URL`, `ANNY_API_KEY` | Anny API |
| `LOCK_BASE_URL`, `LOCK_API_KEY` | Lock-Gateway (z. B. Nuki) |

---

## Was Nuki nicht kann

- **Fluchttür-Hardware** ersetzen (Panikstange, Glastüren-VR).
- Tür nutzen, wenn **innen kein drehbarer Schlüssel** steckt (Kellergang-Tür Ist-Zustand).
- **Mehrere PINs pro Buchung** über eine Tür hinaus: bei mehreren Türen ggf. **mehrere PINs** (eine pro Schloss).
