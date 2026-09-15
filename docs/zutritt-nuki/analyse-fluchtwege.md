# Analyse: Brandschutz-Ausschnitte + Zugangsschema

Stand: September 2026. Quellen: Ausschnitt DG und UG aus dem Brandschutznachweis (Postbau/Gröpke) sowie [Zugangsschema_WUP.pdf](anlagen/Zugangsschema_WUP.pdf) (Elektro Lindenmiller, WUP_S031, 12.09.2025).

Gebäude: **Postgenossenschaft München**, Arnulfstr. 55, Neubau **Kreativquartier / Haus Neuhausen**, Projekt **WUP München**, **56 WE**.

Die Zeichnungen ersetzen keine Prüfung durch Brandschutzplaner oder Schließer. Sie klären aber, **welche Tür welcher Raum ist** und **welche Tür Rettungsweg ist**.

---

## 1. Was das Zugangsschema verdrahtet (genau fünf Türen)

Jede Tür: **Edelstahlkasten 200 × 200 × 80 mm**, **CAT 7**, **NYM 3×1,5** (230 V), **Y-ST-Y 2×2×0,8**, **Türöffner über SPA** (Sprechanlage / Öffnerkreis).

| Schema | Geschoss | Bau-ID | Raum | UV / Speisung |
|--------|----------|--------|------|----------------|
| Tür Wohnen/Schlafen/Küche | **5. OG** | **NH_5_02** | Apartment (Wohnen+Kochen+Schlafen + interne „Gemeinschaft“) | UV **NH 5-03** |
| TUG-11-L | UG | **SB_-1_01_G** | **Musikraum** | Gemeinschafts-UV **SB −1-03 Gem.** |
| TUG-12-L | UG | **SB_-1_02_G** | **Kreativraum / Werkraum** | SB −1-03 Gem. |
| Tür (Außen) | UG | **SB_-1_07** | **Flur außen** (Kellergang → Hof/Lichthof) | SB −1-03 Gem. |
| TUG-16-L | UG | **SB_-1_03_G** | **Veranstaltung** | SB −1-03 Gem. |

Das sind dieselben fünf Türen wie in der UniFi-Diskussion (vier Keller + eine im 5. Stock). **Haustür des Hauses** und **Glastüren VR → Hof** sind **nicht** vorverdrahtet.

Kastenmaß **80 mm tief / 200 mm** ist für einen UniFi Door Hub Mini knapp, aber geometrisch denkbar; Leser sitzt außen. Nuki nutzt den Kasten nicht.

---

## 2. Dachgeschoss — Apartment NH_5_02 (85,34 m²)

Ausschnitt: [brandschutz-dg-nh-5-02.jpg](anlagen/brandschutz-dg-nh-5-02.jpg)

Nutzungseinheit **NH_5_02**: Küche+Wohnen+Schlafen, intern „Gemeinschaft“, zwei Bäder. Das ist das **buchbare Apartment**, nicht ein zweiter Vereinssaal.

| Weg | Verlauf | Bedeutung fürs Schloss |
|-----|---------|------------------------|
| **1. RW** | Wohnungstür → Flur (Türen „D“) → Treppenhaus (grün) | Die **Wohnungseingangstür** liegt **auf dem ersten Rettungsweg**. Rettungslänge 15,21 m bzw. 17,29 m, jeweils &lt; 35 m. |
| **2. RW** | Fenster auf die **Anleiterstelle Hubrettung DG Haus Neuhausen** (1,00 m-Markierungen) | Zweiter Weg ist **kein zweites Türblatt**, sondern Fenster/Leiter. |

Innenliegende Türen (Apartment-„Gemeinschaft“, Bad) sind keine Gebäuderettungswege nach draußen.

**Zutritt:** Schema verdrahtet genau diese Wohnungstür. Nuki-Pilot passt zum Nutzungsprofil (Wohnung, Referenz-Nuki im Haus). Die Tür bleibt der 1. RW der Einheit: Klinke von innen ohne App/Akku muss gehen. UniFi am vorhandenen Öffner ist hier ebenfalls vorbereitet (eigenes UV-Stockwerk).

---

## 3. Untergeschoss — Gemeinschaft / Hobby / Lichthof

Ausschnitt: [brandschutz-ug-gemeinschaft.jpg](anlagen/brandschutz-ug-gemeinschaft.jpg)

Geschützter Fluchtflur oben (hellgrün, **UG OKFF −3,85**), Türen dorthin durchweg **T30-RS**. Treppenhaus oben rechts dunkelgrün.

### 3.1 Veranstaltungs- / Gemeinschaftsraum NE_1_04

- **122,74 m² BGF**, Beschriftung **„Aufenthaltsraum für max. 100 Personen“** — das ist Gröpkes 100-Personen-Raum.
- Über **100 m²**: zwei unabhängige Ausgänge sind auf dem Plan **eingezeichnet**, nicht nur Theorie.

| Weg | Verlauf | Tür für Smart Lock? |
|-----|---------|---------------------|
| **1. RW** | durch **T30-RS** in den grünen Kellerflur → Treppe. Rettungslänge u. a. 16,83 m / 22,35 m, &lt; 35 m | Die **Innentür Veranstaltung** (Schema TUG-16-L / SB_-1_03_G) ist dieser 1. RW. |
| **2. RW** | Pfeil zur Wand **Lichthof**, Text **„Tür erforderlich“** | Das sind die **Hof-/Glastüren**. **Kein** Eintrag im Zugangsschema. **Kein** Nuki, **kein** UniFi, keine elektrische Verriegelung. |

Garderobe und WC liegen **im** Raum; Flucht geht an ihnen vorbei in den Flur, nicht durch Abstellräume als einzigen Weg.

### 3.2 Hobbyräume = Musik + Kreativ

Zwei beige Räume, einer **NE_1_05 35,67 m²**, einer westlich daneben. Schema: **Musikraum** SB_-1_01_G und **Kreativraum/Werkraum** SB_-1_02_G.

- **1. RW:** jeweils **T30-RS** nach oben in den grünen Flur.
- **2. RW:** in den Nachbar-Hobbyraum bzw. in den Flur (kurze Pfeile), **nicht** der Hof.

Diese Innentüren sind **Rettungswegtüren und Feuerschutz (T30-RS)**. Nachrüstung (Bohren, Zylinder-Aufsatz, Leser) kann die **Zulassung der Tür** treffen. Der elektrische Türöffner in der Vorhaltung ist der vorgesehene Weg, die Panik/Klinke von innen muss bleiben.

### 3.3 Kellergangtür außen — SB_-1_07

Schema: **Tür (Außen), 4_Flur / SB_-1_07**. Das ist der **Gäste-Haupteingang Kellergang**, den Gröpke meint.

Auf dem UG-Ausschnitt ist der **2. RW des Veranstaltungsraums nicht diese Flurtür**, sondern die **Lichthof-Öffnung** („Tür erforderlich“). Das stützt Gröpke: **Kellergangtür in den Hof ist kein Fluchtweg**.

Trotzdem:

- Personen im VR sollen über **Glastür/Lichthof** und über **T30-RS + Treppe** raus, nicht über SB_-1_07.
- Ist SB_-1_07 von außen zugesperrt und von innen tot, ist das trotzdem **Einsperrgefahr im Flur**, nicht der amtliche 2. RW des Saals. Klären, nicht ignorieren.
- **Hofzugang über Treppen** (Nachbarbaustelle): der **2. RW endet im Lichthof**. Wenn die Treppen aus dem Hof gesperrt sind, bleibt der **1. RW über das Treppenhaus** der sichere Weg ins Freie. Der 2. RW ist dann nur ein Ausweichen in den Hof, kein Straßenanschluss — vorübergehend mit der Genossenschaft/Feuerwehrlage abgleichen, unabhängig von Nuki.

Lichthof-Koten **NE_1_06 23,67 m²** und **NE_1_07 226,86 m²**, Φ −3,85.

### 3.4 Was nicht zu den fünf Türen gehört

- **Kellerabteile** rechts: eigener 1. RW entlang der Ostseite.
- **Fahrradkeller** NH_-1_02, **ELT-Raum**, **5 Einzelparker**: andere Nutzungseinheiten.
- **Haustür Erdgeschoss:** nicht auf diesen Ausschnitten, nicht im Zugangsschema.

---

## 4. Nuki vs. UniFi je Tür (nach Plan, nicht nach Bauchgefühl)

| Tür | Rettungsweg? | T30-RS? | Vorhaltung | Nuki | UniFi am Öffner |
|-----|--------------|---------|------------|------|-----------------|
| Apartment NH_5_02 | **1. RW der Wohnung** zur Treppe; 2. RW = Fenster/Hubrettung | Wohnungstür, nicht die UG-T30-RS-Serie | ja, UV im 5. OG | **Pilot geeignet**, Klinke innen immer | möglich, eigener Stromkreis |
| Musik SB_-1_01_G | **1. RW** in den Kellerflur | **ja** | ja, UV im großen Raum | riskant (T30-RS + 1. RW, Zylinder ungetestet) | passt zur Vorhaltung, Fachbetrieb, Klinke/Panik unangetastet |
| Kreativ SB_-1_02_G | **1. RW** in den Kellerflur | **ja** | ja | wie Musik | wie Musik |
| Veranstaltung SB_-1_03_G | **1. RW** in den Kellerflur | **ja** | ja | wie Musik; 100 Personen / 122 m² verschärft | wie Musik |
| Glastüren / „Tür erforderlich“ Lichthof | **2. RW** des 100-Personen-Raums | — | **nein** | **ausgeschlossen** | **ausgeschlossen** |
| Flur außen SB_-1_07 | **kein** RW laut Gröpke + Planlogik | prüfen vor Ort | ja | nur nach Zylinder/Klinke-von-innen; technisch oft unmöglich im Ist | sinnvoller Gästezugang am Summer; Einsperrung im Flur trotzdem klären |

**Folgerung aus den Plänen:** Die Vorhaltung ist für **Öffner + SPA** an fünf Türen gebaut, davon **vier T30-RS- bzw. 1.-RW-Türen** im Keller plus die Apartmenttür. UniFi (oder jede Zutrittssteuerung am Öffner) trifft die gezeichnete Infrastruktur. Nuki trifft den **Apartment-Pilot**. An den UG-Innentüren von Musik/Kreativ/VR spricht der Brandschutzplan **gegen** einen Zylinder-Aufsatz, solange T30-RS und 1. RW gelten.

---

## 5. Was das für Versicherung und Gröpke heißt

Nicht mehr offen „welche Tür ist Rettungsweg?“, sondern:

1. **SB_-1_03_G, SB_-1_01_G, SB_-1_02_G:** 1. RW, T30-RS — elektronisch nur über den **vorhandenen Türöffner**, Panik von innen, Zulassung der Feuerschutztür nicht zerstören.
2. **Lichthof-Türen des VR:** 2. RW, 122 m² / 100 Personen — **keine** Zutrittskontrolle.
3. **SB_-1_07:** kein RW, aber Gästezugang und mögliche Einsperrung; Hof-Treppen temporär zu.
4. **NH_5_02:** 1. RW der Nutzungseinheit, 2. RW Hubrettung — Apartment-Pilot; Keypad/Öffner der Gebäudeversicherung nennen.
5. Kasten **200×200×80** und Speisung aus **UV SB −1-03 Gem.** bzw. **UV NH 5-03** — UniFi = Änderung der elektrischen Anlage, Fachbetrieb.

---

## 6. Abgleich mit früheren Annahmen

| Früher im Repo | Plan |
|----------------|------|
| Großer Raum max. 100 Personen | bestätigt, NE_1_04 122,74 m² |
| Zwei Ausgänge ab 100 m² | **eingezeichnet** (Flur + Lichthof) |
| Glastüren VR = Rettungsweg, kein Nuki | bestätigt als **2. RW** |
| Kellergangtür kein Fluchtweg (Gröpke) | bestätigt: 2. RW ≠ SB_-1_07 |
| Fünf Türen, 4 Keller + 5. Stock | bestätigt durch Schema |
| 56 Wohnungen | bestätigt Schriftfeld |
| Apartment = Dach-Pilot | = NH_5_02, nicht der UG-Saal |
| Haustür verdrahtet | **nein**, nicht im Schema |
