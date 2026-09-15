# Gesprächsprotokoll: Nuki vs. UniFi Access

Vollständige Zusammenfassung der Diskussion (Cloud-Agent / Verwaltung), ergänzend zu [vergleich-nuki-unifi.md](vergleich-nuki-unifi.md). Stand: September 2026.

Aktualisierte Kopie im Docs-Root: [../gespraechsprotokoll-zutritt-nuki-unifi.md](../gespraechsprotokoll-zutritt-nuki-unifi.md)

→ [Übersicht Zutritt-Nuki](README.md) · [Projektplan](projektplan.md)

---

## Verlauf in Kurzform

1. Rückfragen und Korrekturen zu einer ersten Vergleichsnotiz (Tobias).
2. Bias-freie Analyse mit Kosten (DIY vs. Fachbetrieb), Versicherung, Wartung, Notausgang, 200er-Limit, WLAN.
3. Klärung: Nuki DIY möglich; UniFi am Summer nicht DIY (NAV + Versicherung), auch wenn Kabel und Summer an den Türen liegen.
4. Antworten auf Tobias’ Punkte mit diesem Wissen.
5. Kostentabelle mit **Keypad für beide** Systeme; UniFi: nicht zwei normale Hubs für 5 Türen, sondern 5× Mini oder Enterprise + Mini.
6. Anny: Keypad praktisch nötig für PIN; Remote Open ohne Keypad möglich.
7. PoE: Erklärung und ob zwingend nötig.
8. Dokumentation ins Repo; Merge in `main`.

---

## Tobias — erste Rückfragen und Antworten

### WLAN / Access Point (Kreativ-, Musik-, Veranstaltungsraum)

**Anmerkung:** Nuki braucht WLAN oder Thread; ohne AP im Gang vermutlich keine Verbindung zum Veranstaltungsraum; Kabel von der Küche in den Gang nötig.

**Antwort:** Plausibel. Nuki braucht stabiles 2,4-GHz-WLAN **innenseitig an jeder Tür**. Repeater oft problematisch (falscher AP, Akku). Kabelgebundener AP (Küche → Gang) ist die seriöse Nuki-Lösung. UniFi nutzt vorhandenes Ethernet — kein WLAN-Problem an der Tür. Messung am Schloss, nicht vom Gang.

### Akku 4–6 Monate, 5 Türen ≈ 1× pro Monat laden

**Antwort:** Korrekt (Herstellerangabe bei WLAN). Organisatorischer Aufwand bei DIY-Nuki. UniFi: PoE, keine Tür-Akkus.

### Nuki = Nachrüstung ohne Infrastruktur; bei uns Ethernet, Summer, Montage für Leser

**Antwort:** Zutreffend. UniFi passt zur vorhandenen Infrastruktur. Nuki nutzt sie kaum (Funk + Aufsatz). **Neu:** Kabel und Summer liegen an den Türen — UniFi-Einbau wird günstiger (kein Kabelzug), Fachbetrieb für Anschluss bleibt Pflicht.

### Kosten Ultra ~100 € vs. Nuki ~269 €, Gateway ~250 €, Summe ~2000 €; Nuki + AP/Verkabelung

**Antwort:** Größenordnung ähnlich, Details:

- Access Ultra günstig, aber **kein PIN** (für Anny/Hauscode ungeeignet).
- Cloud Gateway **Ultra** (~120 €) kann **kein** UniFi Access — braucht z. B. Cloud Gateway Max (~180–250 €).
- Mit **Keypad überall**: Nuki Pro + Keypad ~350 €/Tür; UniFi Reader Flex + Hub Mini eher ~260–320 €/Tür Hardware.
- Gesamt: Nuki DIY oft ~1.900–2.000 €; UniFi mit Fachbetrieb ~2.500–3.400 € (5× Mini).

### „Magnet/Türöffner vs. Klinke und Schlüssel“

**Anmerkung:** Alles bleibt mit Summer wie gehabt.

**Antwort:** Richtig. Gemeint war Magnet als Ersatzverriegelung, nicht Anbindung an **bestehenden Summer**. UniFi löst denselben Impuls wie der Klingeltaster. Zylinder, Schlüssel, Klinke bleiben. Summer = Falle, nicht Riegel; bei abgeschlossener Tür mit Schlüssel öffnet UniFi nicht, Nuki kann den Riegel drehen.

### Anny + UniFi nativ

**Antwort:** Korrektur der früheren „nur Umwege“-Aussage — [anny.co/integrations/unifi-door-access](https://anny.co/integrations/unifi-door-access). **Nuki ebenfalls nativ** ([Anny-Doku](https://docs.anny.co/de/articles/30440-nuki-integration)). Unterschied: Nuki-Limit 200 künftige Zugänge pro Schloss (Anny-Doku).

### Limit 200 Personen — woher?

**Antwort:** [Nuki Support — Zutrittsberechtigungen](https://help.nuki.io/hc/de/articles/4407512064785): Hardware-Limit **pro Schloss** (App-Nutzer und Keypad-Codes je bis 200 bei aktuellen Modellen). Nuki Web erhöht das nicht. Bei ~140 Bewohnern + Gäste knapp für individuelle Accounts. **Workaround:** monatlich wechselnder **Hauscode** (1 Keypad-Slot) + Schlüssel bleibt — löst Bewohner-Problem, nicht vollständig Anny-Buchungsgäste (zählen gegen 200 künftige Zugänge).

---

## Bias-freie Analyse — zusätzliche Themen

### Kosten Selbsteinbau vs. Fachbetrieb

| | Nuki | UniFi |
|---|---|---|
| DIY | üblich (Pro + Akku-Keypad) | nur stromlose Vorarbeiten; Anschluss Summer/PoE = Fachbetrieb |
| Fachbetrieb pro Tür | optional, gering | typisch **150–300 €** Arbeit, wenn Leitungen da (ohne Kabelzug) |
| Handwerker „pro Tür“ bei UniFi | — | normal (Leser, Relais, Prüfung), kein reines Aufschlag-Trick |

### Versicherung / Hauselektrik

- **Nuki Pro + Keypad:** kein NAV-Eingriff; Gebäudeversicherung vorher schriftlich klären (sichtbares Keypad außen kann bei einzelnen Tarifen relevant sein).
- **UniFi:** Änderung der elektrischen Anlage (§ 13 NAV). **Keine** vorherige „Abnahme“ durch Versicherer; im Schadenfall Prüfung. DIY-Elektrik: Risiko Leistungskürzung/Ablehnung (grobe Fahrlässigkeit). Fachbetrieb + Protokoll = üblicher Weg.
- Einbruch ohne mechanische Spuren bei Smart Locks: Hausrat kann streitig sein (Beweislast); unabhängig von Nuki vs. UniFi.

### Wartung

| | Nuki DIY | UniFi |
|---|---|---|
| Routine | Akku ~monatlich im Schnitt (5 Türen), Keypad-Batterien | Firmware/Konsole; kein Akku an Tür |
| Defekt | Schloss/Keypad selbst tauschen | Hardware an Tür oft Elektriker |
| Fachbetrieb | optional | bei Elektrik/Defekt sinnvoll |

### Notausgang

- UniFi + Summer: **Klinke innen** mechanisch, auch ohne Strom (typisch fail-secure).
- Nuki: **Drehrad innen** bei leerem Akku; Fluchtweg-Zulässigkeit bei ausgewiesenen Notausgängen mit Brandschutz klären.
- Brand-/Rauchschutztüren: E-Öffner nur nach Zulassung; Arbeitsstrom-Prinzip.

### WLAN Repeater „Kellerräume nah“

Kann funktionieren, ist **nicht** zuverlässig (Nuki verbindet oft falschen Mesh-AP). Eigenes SSID am nächsten AP oder kabelgebundener AP. Nur Messung an der Tür entscheidet.

### 200er-Limit + Hauscode

Hauscode für alle Bewohner: Limit für Dauerzugang entschärft. Schlüssel parallel. Trade-off: Sicherheit/Protokollierung. Anny-Buchungen bleiben separates Kontingent.

---

## Klärungsfragen (DIY / Versicherung)

**Frage:** Nuki problemlos DIY, UniFi nicht, vor allem Versicherung — UniFi nicht DIY, obwohl Kabel und Summer an den Türen?

**Antwort:** Ja.

| | Nuki | UniFi |
|---|---|---|
| DIY? | Ja (Pro + Akku-Keypad) | Nein für Summer/PoE-Anschluss |
| Versicherung | kein Elektriker-Thema | DIY-Elektrik nicht „abgenommen“; Fachbetrieb + Doku |
| Liegende Leitungen | sparen bei UniFi nur Kabelzug, nicht Elektriker |

**Frage:** UniFi selbst einbauen — Versicherung?

**Antwort:** Nein, auch nicht bei vorhandenen Leitungen. Relais an Summer = elektrische Anlage.

**Vorgehen wenn UniFi:** Vorarbeit selbst möglich; **Anschluss und Protokoll** Elektriker.

---

## Keypad und Anny

**Frage:** Mit Anny brauchen wir bei UniFi auf jeden Fall ein Keypad?

**Antwort:** Nicht softwareseitig zwingend. **Praktisch ja** für Buchungsgäste und Keller (PIN in Mail, kein Handy nötig). Alternative nur **Remote Open** in Anny (Smartphone + Netz). Access Ultra **ohne PIN** — für Parität zu Nuki-Keypad: z. B. **Reader Flex** + Hub.

Für **Kostenvergleich** wurde angenommen: **Keypad/PIN an allen 5 Türen** (Nuki Keypad + UniFi Reader Flex).

---

## PoE

**Was ist PoE?** Strom + Daten über ein Ethernet-Kabel; keine Steckdose am Leser.

**Brauchen wir das unbedingt?**

- **Nuki:** Nein.
- **UniFi:** Ja — Speisung auf dem Kabel (Switch mit PoE++ oder **Injektor** pro Hub). Extra PoE-Switch nur wenn der bestehende Switch nicht speist. Door Hub Mini: **PoE++** beachten.

---

## UniFi-Hubs: „zwei Hubs“ (Keller + 5. Stock)

- Door Hub Mini / Door Hub: **1 Tür pro Hub**.
- **Zwei** normale Hubs ≠ 5 Türen.
- Varianten:
  - **5× Door Hub Mini** (empfohlen in der Kostenschätzung), oder
  - **1× Enterprise Access Hub** (bis 8 Türen, ~998 €) im Keller + **1× Mini** im 5. Stock — teurer als 5 Minis.
- Hub soll **nah an der Tür** (Kabel Hub↔Leser, Richtwert max. ~100 m).

---

## Dokumentierte Team-Richtung (aus der Diskussion)

Ausdrücklich genannt, keine technische Pflicht:

- **Nuki:** DIY vorgesehen.
- **UniFi:** nicht DIY (NAV + Versicherung), auch mit liegenden Kabeln/Summern; Fachbetrieb für Anschluss.

---

## Quellen (Auswahl)

| Thema | Link |
|---|---|
| Nuki 200 Limit | https://help.nuki.io/hc/de/articles/4407512064785 |
| Nuki Akku leer | https://help.nuki.io/hc/de/articles/14838368305553 |
| Anny Smart Locks | https://docs.anny.co/de/articles/30481-smart-lock-integrationen |
| Anny Nuki | https://docs.anny.co/de/articles/30440-nuki-integration |
| Anny UniFi | https://anny.co/integrations/unifi-door-access |
| UniFi Unlock Methods (PIN pro Leser) | https://help.ui.com/hc/en-us/articles/17459303874327 |
| § 13 NAV | https://www.gesetze-im-internet.de/nav/ |

Hardware-Preise (Richtwerte): Ubiquiti EU Store (UA-Ultra, UA-Hub-Door-Mini, EAH-8, UCG-Max), Straßenpreise idealo/Geizhals für Nuki Pro 5 + Keypad.

---

## Verwandte Dateien im Repo

- `docs/nuki-vs-unifi.md` — kompakte Entscheidungsgrundlage und Kostentabellen
- `README.md` — FreiUndFritz / Anny + Türschloss (Software)
