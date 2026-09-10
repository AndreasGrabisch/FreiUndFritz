# Nuki vs. UniFi Access — Entscheidungsgrundlage

Stand: September 2026. Vergleich für fünf Gemeinschaftstüren (vier Keller, eine im 5. Stock), Anny-Buchungen, vorhandene Ethernet- und Summer-Infrastruktur.

Keine Empfehlung für ein System. Ziel ist, die offenen Punkte (Kosten, DIY, Versicherung, WLAN, Akku, Anny, 200er-Limit, PoE, Keypad) an einem Ort zu haben.

---

## Ausgangslage

| Gegeben | Bedeutung |
|---|---|
| 5 Türen | 4 Keller nah beieinander, 1 Tür 5. Stock |
| Ethernet und Türsummer liegen an den Türen | UniFi kann den bestehenden Öffner nutzen; kein Kabelzug bis zur Tür nötig |
| Montagepunkte für Leser/Keypads vorhanden | beide Systeme montierbar |
| Anny für Raumbuchung | beide nativ anbindbar |
| Bewohnerschaft | 56 Wohnungen × ~2,5 ≈ 140 Personen plus Dauergäste |
| Anforderung | Klinke innen und mechanischer Schlüssel bleiben |
| Keypad/PIN | für den Alltag und Anny-Buchungsgäste praktisch nötig |
| Einbau | Nuki DIY; UniFi nicht DIY (NAV + Versicherung) |

Zwei verschiedene Funktionsprinzipien, kein Markenvergleich 1:1:

| | **Nuki Pro** | **UniFi Access + bestehender Summer** |
|---|---|---|
| Mechanik | Motor dreht den Schließzylinder | Relais gibt denselben Impuls wie der Summer |
| Türzustand | kann den **Riegel** vor- und zurückschließen | löst nur die **Falle** |
| Schlüssel außen | bleibt (Pro, ohne Zylindertausch) | bleibt |
| Klinke innen | bleibt | bleibt |
| Abgeschlossen mit Schlüssel | Nuki öffnet trotzdem | Summer/UniFi öffnet **nicht** |

Solange die Räume wie heute mit Summer genutzt werden (Riegel nicht vorgeschlossen), ändert UniFi am Alltag wenig. Soll nachts wirklich abgeschlossen werden, kann das Nuki, UniFi am Summer nicht.

Nuki **Ultra** tauscht den Zylinder — für eine Schließanlage unpassend. Vergleichsmodell ist **Nuki Pro**.

---

## Antworten auf die Diskussionspunkte

### WLAN / Access Point

Nuki braucht an jeder Tür **innenseitig** stabiles 2,4-GHz-WLAN (Fernzugriff und Anny). Bluetooth reicht nur direkt an der Tür.

Ob ohne AP im Gang der Veranstaltungsraum reicht, sieht man nur per Messung **am Schloss**. Repeater sind bei Nuki unsicher (oft falscher AP, höherer Akkuverbrauch). Ein **kabelgebundener AP** (Küche → Gang) ist die seriöse Nuki-Variante.

UniFi braucht dieses WLAN an der Tür nicht. Ethernet liegt. Das Küchen-Gang-Kabel wäre ein **Nuki-Extra**.

### Akku

Hersteller: bei WLAN-Anbindung etwa 4–6 Monate. Bei 5 Türen im Schnitt etwa **ein Schloss-Akku pro Monat**, plus Keypad-Batterien (~jährlich). Das wäre DIY-Routine.

UniFi über PoE: keine Tür-Akkus.

### „Nuki ist Nachrüstung — bei uns liegt die Infrastruktur“

Stimmt. Ethernet, Summer und Montagepunkte sind da. Nuki nutzt davon fast nichts (Funk + Zylinder-Aufsatz). UniFi ist für Summer + Ethernet + Leser gebaut.

Haken: Relais an den vorhandenen Summer ist Hauselektrik. Nuki könnt ihr selbst. UniFi trotz liegender Kabel **nicht** selbst. Der Fachbetrieb wird dadurch **billiger** (kein Kabelzug), aber nicht überflüssig.

### Klinke und Schlüssel / Summer

Die frühere Formulierung zu Magneten war missverständlich. **Am bestehenden Summer bleibt alles mechanisch:** Zylinder, Schlüssel, Klinke innen. Es kommt ein Leser dazu, der denselben Impuls auslöst wie der Summer. Einziger Zusatz: Summer = Falle, nicht Riegel.

### Anny

Beide nativ:

- [UniFi Door Access](https://anny.co/integrations/unifi-door-access)
- [Nuki](https://docs.anny.co/de/articles/30440-nuki-integration)

Kein UniFi-Alleinstellungsmerkmal. Unterschied: Anny nennt bei Nuki ein Limit von **200 künftigen Zugängen pro Schloss**. UniFi hat dieses Schloss-Limit nicht.

Anny-Zugang an der Tür:

| Methode | Keypad nötig? |
|---|---|
| Remote Open (Button in Anny) | Nein — braucht Smartphone und Netz an der Tür |
| PIN aus der Buchungsmail | **Ja** — Leser mit PIN-Pad |

Ohne Keypad bleibt Remote Open. Im Keller (Empfang, leeres Handy, Gast ohne App) ist das unsicher. Access Ultra hat **kein PIN**. Für denselben Ablauf wie Nuki (Code in der Mail, eintippen) braucht UniFi z. B. **Reader Flex**.

Softwareseitig also nicht zwingend ein Keypad — für unbeaufsichtigte Gemeinschaftsräume plus Buchungsgäste praktisch ja.

### Limit 200 Personen (Nuki)

Quelle: [Nuki Support — Zutrittsberechtigungen](https://help.nuki.io/hc/de/articles/4407512064785). **Hardware-Limit pro Schloss**, nicht pro Account. Nuki Web hebt es nicht auf. App-Nutzer und Keypad-Codes sind getrennte Kontingente (je 200 bei aktuellen Modellen).

140 Bewohner plus Dauergäste sind für **persönliche** Accounts knapp.

Workaround: **ein monatlich wechselnder Hauscode** = ein Keypad-Slot; Schlüssel bleibt. Dann ist 200 für Bewohner kein Problem. Nachteile: kein Wer-war’s-Log, Code sickert, Wechsel muss alle erreichen. **Anny-Buchungsgäste** zählen extra gegen dieselben 200 künftigen Zugänge.

UniFi Access: bis 3000 Nutzer am Ultra/Hub; PIN nur an geeigneten Lesern.

---

## DIY, Elektrik, Versicherung

| | Nuki Pro + Akku-Keypad | UniFi am Summer |
|---|---|---|
| Fachbetrieb | nicht nötig | ja, für Anschluss und Inbetriebnahme |
| § 13 NAV | kein Eingriff in die elektrische Anlage | Relais an Summer und PoE = Änderung der Anlage |
| Versicherung vorher | üblicherweise keine Abnahme nötig; Keypad der Gebäudeversicherung kurz schriftlich nennen | Versicherungen nehmen DIY-Elektrik **nicht** ab |
| Im Schadenfall | kleiner Eingriff | ohne Fachbetrieb und Prüfprotokoll: Kürzung oder Ablehnung möglich |

Nuki Ultra (Zylindertausch) wäre Schlosserei und oft ein WEG-Thema, weiterhin keine Elektrik.

Brand-/Rauchschutztüren: nicht einfach bohren; E-Öffner nur bei passender Zulassung.

**Folgerung:** Nuki DIY. UniFi nicht DIY — auch wenn Kabel und Summer schon an den Türen liegen. Stromlose Vorarbeiten (Dosen, Leerrohre) können Laien in Absprache mit dem Elektriker machen; Anschließen bleibt Fachbetrieb.

---

## PoE — brauchen wir das?

**PoE (Power over Ethernet):** Strom und Daten über dasselbe Netzwerkkabel. Leser/Hub brauchen dann keine Steckdose an der Tür.

| | Nuki | UniFi |
|---|---|---|
| PoE nötig? | Nein (Akku/Batterie) | **Ja** — irgendeine Speisung auf dem Kabel |
| Extra PoE-Switch zwingend? | — | Nein, wenn der vorhandene Switch schon PoE++ hat **oder** ein Injektor pro Hub reicht |

Door Hub Mini verlangt **PoE++** (stärker als normales PoE+). Ein schwacher PoE-Port kann zu wenig sein.

---

## Hardware-Architektur UniFi mit Keypad

Access Ultra (~90–110 €, Leser+Hub+Relais) hat **kein PIN** — für Anny-PIN und Hauscode ungeeignet.

Door Hub Mini und Door Hub steuern je **eine** Tür. Zwei Standard-Hubs decken fünf Türen nicht.

Keller vs. 5. Stock: Hub nah an der Tür (Strecke Hub→Leser max. ca. 100 m). Praktisch:

- **5× Door Hub Mini** (vier Keller, einer 5. Stock), oder
- **1× Enterprise Access Hub** (bis 8 Türen) im Keller **plus** 1× Mini im 5. Stock — teurer als fünf Minis.

---

## Kostentabelle (5 Türen, Keypad überall)

Preise gerundet, EU-Store / Straßenpreis 2026, ohne Versand. Ethernet und Summer liegen.

| Position | Nuki (DIY) | UniFi, 5× Hub Mini + Reader Flex | UniFi „2 Hubs“ (Enterprise + Mini) |
|---|---|---|---|
| Schloss / Leser | 5 × Pro ~260 € = **1.300 €** | 5 × Reader Flex ~160 € = **800 €** | 5 × Reader Flex = **800 €** |
| Keypad | 5 × Keypad (Code) ~90 € = **450 €** | im Reader Flex | im Reader Flex |
| Hub | — | 5 × Mini ~99 € = **495 €** | Enterprise ~998 € + Mini ~99 € = **1.097 €** |
| Zentrale | — | Cloud Gateway Max * ~180–250 € | ~180–250 € |
| PoE | — | Switch/Injektor PoE++ ~200–350 € | ~250–400 € |
| WLAN extra | AP + Kabel Küche→Gang ~150–250 € | nicht nötig | nicht nötig |
| **Hardware** | **~1.900–2.000 €** | **~1.700–1.900 €** | **~2.300–2.550 €** |
| Einbau | selbst **0 €** | Fachbetrieb ~150–300 €/Tür → **750–1.500 €** | **750–1.500 €** |
| **Gesamt grob** | **~1.900–2.000 €** | **~2.500–3.400 €** | **~3.100–4.000 €** |

\* Nicht Cloud Gateway Ultra — das kann UniFi Access nicht.

Keypad 2 (Fingerprint) statt Basis-Keypad: Nuki etwa **+275 €**.

Die **Geräte** liegen mit Pflicht-Keypad nah beieinander. Der Abstand entsteht durch den Elektriker bei UniFi und durch die Hub-Stückzahl.

---

## Notausgang / Stromausfall

Fluchtwege müssen von innen ohne Schlüssel zu öffnen sein. Ob die Raumtüren ausgewiesene Fluchtwege sind, steht im Brandschutznachweis.

- **UniFi + Summer + Klinke:** Klinke öffnet mechanisch, auch ohne Strom (fail-secure-Öffner von außen zu, von innen die Klinke).
- **Nuki, Riegel vorgeschlossen:** von innen das Drehrad, auch bei leerem Akku (laut Nuki-Support). Ob das für einen amtlichen Notausgang reicht, ist eine Frage an Brandschutz/Schlosser.
- Von außen bei Totalschaden: bei beiden der mechanische Schlüssel, sofern der Zylinder bleibt.

---

## Gegenüberstellung

| Kriterium | Vorteil Nuki | Vorteil UniFi | Kommt drauf an |
|---|---|---|---|
| Hardware DIY | | Mini-Stückliste oft etwas günstiger | PIN-Vergleich ähnlich |
| Gesamtkosten | DIY, oft niedriger | | Fachbetrieb trotz liegender Leitungen |
| Selbsteinbau | klar | | |
| NAV / Versicherung DIY | klar | UniFi mit Fachbetrieb und Doku tragbar | |
| Akku-Routine | | klar (PoE) | |
| Defekt tauschen | Aufsatz tauschen | | |
| Schlüssel + Klinke | ja (Pro) | ja | |
| Tür wirklich abschließen | klar | | |
| Notausgang über Klinke | | typisches Summer-Muster | Brandschutztür extra prüfen |
| 140 Bewohner | Hauscode oder Limit | 3000 User | Ultra ohne PIN |
| Anny-Buchungen in der Fläche | | 200er-Limit entfällt | beide nativ |
| WLAN Keller | | kabelgebunden | Messung; Repeater unsicher |
| Vorhandene Infrastruktur | ungenutzt | genau der Anschlussweg, nur vom Elektriker | |

---

## Offene Prüfungen vor einer Entscheidung

1. An jeder Tür: Brand-/Rauchschutz? Wird der Riegel im Alltag vorgeschlossen?
2. WLAN-Messung innen am Schloss (Nuki), nicht vom Gang.
3. Gebäudeversicherung schriftlich: Nuki-Aufsatz + Keypad vs. PoE-Leser an bestehendem Türöffner, Fachbetrieb.
4. Vorhandener Switch: PoE++ ja/nein?
5. Anny: wie viele gleichzeitige künftige Buchungszugänge über 5 Räume?

Ohne 1–2 bleiben WLAN- und Brandschutzkosten Spekulation. Der Fachbetrieb hat bei UniFi recht mit Kosten **pro Tür**; das ist der Preis für den Eingriff ins elektrische System, kein Argument gegen oder für eine Marke.
