# Versicherungsfragen Nuki vs. UniFi

Stand: September 2026. Quellen im Repo: Gröpke-Mail (Postbau), `nuki-vs-unifi.md`, Gesprächsprotokoll, Projektkontext Postbaugenossenschaft / Bewohnerverein (`docs/zutritt-nuki/`), FreiUndFritz/Anny.

Versicherer **genehmigen die Montage in der Regel nicht im Voraus**. Gefragt wird nach **Anzeige**, **Deckung im Schadenfall** und **Obliegenheiten**. Schriftlich, **pro Tür**, **getrennt nach Police**.

---

## 1. Wer fragt wen?

| Police | Wer hat sie? | Kanal | Wofür |
|---|---|---|---|
| Wohngebäude | **Postbaugenossenschaft** | Hausverwaltung / Gröpke | Schloss, Keypad, Leser, Einbruch, bauliche Änderung an Gemeinschaftstüren |
| Haus- und Grundbesitzer-Haftpflicht | **Postbaugenossenschaft** | derselbe | Personenschaden am Gebäude (Einsperrung, Fluchtweg, Sturz, unbefugter Zutritt über Gebäudezugang) |
| Vereins-Haftpflicht | **Bewohnerverein** | Vorstand direkt an Vereinsversicherer | Anny-Gäste, PIN/App, Veranstaltungen, Apartment-Vermietung, Fehlöffnung |
| Vermieter / Mietausfall (falls vorhanden) | Verein oder Genossenschaft | nur wenn Apartment vermietet | eher Schadenfall als Freigabe |

Gröpkes Satz „Was sollten wir mit unserer Versicherung abklären?“ meint die **Genossenschaftspolicen**, nicht die Vereins-Haftpflicht. Die Vereins-Haftpflicht klärt der Verein selbst.

Keine WEG-Eigentümerversicherung: Träger ist die Genossenschaft, Entscheidung Zutritt der Bewohnerverein.

Private Haftpflicht der Montierenden ersetzt das nicht. Cyber ist für diese Größe im Repo als selten eingestuft; DSGVO (Anny/Logs) bleibt separat.

---

## 2. Ausgangslage, die der Versicherer kennen muss

Kurzbeschreibung, nicht Marken-Pitch:

- München, Postbaugenossenschaft, Bewohnerverein betreibt **Anny**.
- Ca. **50–56 Wohnungen**, rund **140 Personen** plus Dauergäste und **Buchungsgäste**.
- Großer Gemeinschafts-/Veranstaltungsraum laut Postbau **bis 100 Personen** ausgelegt; Verein plant eher kleinere öffentliche Buchungen (Anzeige LStVG/KVR ist **keine** Versicherungsfrage).
- Vorhaltung an mehreren Türen: **230 V, CAT 7, Y-ST-Y, elektrischer Türöffner (Summer)** im Edelstahlkasten; **Panikschlösser müssen bleiben**; Zylindertausch grundsätzlich möglich.
- Nutzung heute: Summer löst die **Falle**, nicht den Riegel. Mechanischer Schlüssel und Klinke innen sollen bleiben.
- Software: Anny prüft die Buchung, dann kurzer Unlock (PIN, App oder Remote Open). Tokens sind zeitlich begrenzt.
- Zwei Bauarten:
  - **A UniFi:** Relais am vorhandenen Summer, PoE, Leser/Keypad außen, **Fachbetrieb** (§ 13 NAV, Änderung der elektrischen Anlage).
  - **B Nuki Pro + Keypad:** Aufsatz innen am Zylinder, Akku, **kein** Eingriff in die Hauselektrik, DIY vorgesehen; Keypad sichtbar außen.

---

## 3. Türen — nicht eine Frage fürs ganze Haus

| Tür | Lage / Rolle | Brandschutz / Beobachtung im Repo | Versicherung |
|---|---|---|---|
| **Glastüren VR → Lichthof** | 2. RW des 122-m²-Raums | nicht im Schema; **kein** Smart Lock | nur bestätigen: keine elektrische Verriegelung |
| **Kellergang Flur außen SB_-1_07** | Gäste-Haupteingang, Vorhaltung | **kein** Fluchtweg | Einsperrung im Flur / Klinke von innen |
| **Musik / Kreativ / VR-Innentür** | T30-RS, **1. RW** in den Kellerflur | Vorhaltung am Öffner | Feuerschutztür-Zulassung, Panik, Fachbetrieb bei UniFi |
| **Apartment NH_5_02** | 1. RW Wohnung; 2. RW Hubrettung | Vorhaltung + Pilot | Keypad/Öffner anzeigen |
| **Haustür EG** | nicht im Schema | Rettungswegstatus offen | erst wenn überhaupt geplant |

Pilot Apartment darf die Klärung Keller **nicht ersetzen**, sobald Gemeinschaftstüren dran sind.

---

## 4. Gemeinsame Fragen (beide Bauarten)

An **Gebäudeversicherung und Gebäude-Haftpflicht** (über HV/Gröpke):

1. Müssen Montage und sichtbares Keypad/Leser **vorher angezeigt** werden, oder reicht Information zur Akte?
2. Ändert elektronischer Zutritt die **Einbruchdeckung** (auch ohne Aufbruchspuren — Hausrat/Gebäude kann streitig sein)?
3. Bleibt die **Panik / Klinke von innen ohne Strom, Akku und App** uneingeschränkt — insbesondere an den **T30-RS-Türen** Musik, Kreativ, VR-Innentür (jeweils 1. RW) und an der Apartmenttür NH_5_02?
4. Ist der **Ist-Zustand Kellergang** (von außen zu, von innen ggf. nicht auf) mit der Police und dem Brandschutznachweis vereinbar — **vor** jeder Nachrüstung?
5. Gäste mit **zeitlich begrenzter PIN/App** (Anny): Obliegenheit „Schlüssel nur an bekannte Personen“ verletzt?
6. Fernöffnen (Remote Open) und wechselnder **Hauscode** (~140 Bewohner, Nuki-Limit 200 Zugänge/Schloss): reicht das als Schließmittel-Sorgfalt, oder sind personenbezogene Codes nötig (Protokoll „wer war drin“)?
7. Darf nachts mit Schlüssel **vorgeschlossen** werden? (UniFi/Summer öffnet dann **nicht**; Nuki kann den Riegel drehen — anderes Einbruch- und Einsperrszenario.)
8. Brand-/Rauchschutztür: Bohren für Leser, E-Öffner-Zulassung?

An die **Vereins-Haftpflicht** (Verein selbst):

1. Deckt die Police **automatischen Gästezutritt** (PIN/App/Remote Open) über Anny?
2. Apartment-Vermietung/Buchung und spätere Kellerräume/VR — eine Deckung oder nachmelden?
3. Öffentliche Buchungen / Veranstaltungen im großen Raum (Auslegung **100 Personen**): reicht die Vereins-Haftpflicht, oder Veranstalter-Zusatz?
4. Haftung bei **falsch erteiltem Zutritt** (Buchung, gehacktes Konto, Code weitergegeben, Tür bleibt offen) und bei **Aussperrung** (leerer Akku, Netz tot, Summer tot)?
5. Muss die Police vor Start **angepasst** werden oder nur informiert?

---

## 5. Nur UniFi (Summer + PoE + Leser)

Für den Versicherer: *Fachbetrieb schaltet den vorhandenen Türöffner. Panik/Klinke mechanisch. Von außen Berechtigung, von innen Klinke. Kein DIY am Stromkreis.*

1. Ist die Nutzung der **Vorhaltung** (230 V, CAT 7, Öffner) mit Nachweis und Gebäudepolice vereinbar?
2. **Fail-secure** (stromlos von außen zu) zulässig, oder stromlos auf / BMA-Zwangsoffnung an Rettungswegtüren?
3. DIY am Summer/PoE: Repo-Stand — **nicht** versicherbar im Schadenfall (§ 13 NAV). Reicht **eingetragener Elektrobetrieb plus Prüfprotokoll**?
4. Muss das System **VdS-gelistet** sein? (UniFi typischerweise nicht.)
5. Leser außen an Feuerschutztür: Zulassung der Tür?
6. Netzausfall: Falle wie bisher, Klinke innen — für Haftpflicht ausreichend?
7. Summer öffnet nur die Falle: wenn jemand den **Riegel** vorschließt, kommen Buchungsgäste nicht rein — organisatorisches Risiko, kein Öffnen abgeschlossener Türen.

Erwartung laut Repo: tragbar **nur mit Fachbetrieb und Dokumentation**. Keine vorherige „Abnahme“ durch den Versicherer.

---

## 6. Nur Nuki Pro + Keypad (Zylinder-Aufsatz)

Für den Versicherer: *Batterie-Aufsatz innen dreht den Zylinder. Türöffner ungenutzt. Keypad außen. DIY. Keine Zulassung als Fluchttürverschluss. Nuki Ultra (Zylindertausch) ist nicht die Vergleichsvariante.*

1. Gemeinschafts-/Rettungswegtüren: Consumer-Aufsatz **ausgeschlossen**?
2. **Apartment-Tür** getrennt: zulässig (Pilot)?
3. **Kellergang:** im beobachteten Ist-Zustand (innen nicht drehbar) oft **nicht montierbar** — erst nach Zylinder mit Not- und Gefahrenfunktion; dann neu anfragen.
4. **Glastüren VR:** nicht anfragen als Option.
5. Keypad **sichtbar außen**: Einfluss auf Einbruch/Vandalismus-Tarif?
6. Bestimmungsgemäße Verwendung (Wohnungsabschluss) vs. Gemeinschaftsraum / bis 100 Personen / Gästebetrieb — Deckung ja oder nein?
7. Leerer Akku: Nuki nennt Drehrad innen; reicht das an amtlichem Notausgang? Wer haftet bei Aussperrung von fünf Türen (ca. ein Ladevorgang pro Monat)?
8. Mechanischer Schlüssel parallel: Anzahl, Verwahrung, Schlüsselverlust analog Schließanlage?
9. Cloud-Account, geteilte Admins, Hauscode ohne Wer-war’s-Log: Sorgfalt Schließmittel?
10. Ungenutzter geplanter Türöffner: Verstoß gegen Abnahme/Nachweis?

Erwartung laut Repo: elektrisch der **einfachere** Weg (kein NAV). Gebäudeversicherung trotzdem **kurz schriftlich** (Aufsatz + Keypad). An Rettungsweg und an der Kellergangtür mit Einsperrverdacht oft **nein**, bis Zylinder/Brandschutz klar sind.

---

## 7. Was Gröpke konkret vorlegen soll (Genossenschaft)

Nicht: „Ist Nuki versichert?“ Sondern:

> Wir prüfen zwei Bauarten an den Gemeinschaftstüren mit vorhandener Vorhaltung (drei Veranstaltungsräume bzw. Kellertüren plus Kellergangtür; Glastüren Hof bleiben ohne Elektronik). Variante A: Fachbetrieb steuert den vorhandenen elektrischen Türöffner (netzwerkgestützt). Variante B: batteriebetriebenes Smart Lock am Profilzylinder plus Keypad außen, ohne Eingriff in die Hauselektrik. Panikbeschläge bleiben. Der große Raum ist bis 100 Personen ausgelegt; Gäste sollen über das Buchungssystem zeitlich begrenzten PIN-/App-Zugang erhalten. Bitte klären Sie mit Wohngebäudeversicherung und Gebäude-Haftpflicht schriftlich: Anzeigepflicht; Einbruchdeckung bei digitalem Zutritt ohne Aufbruchspuren; Rettungsweg je Tür laut Nachweis; ob die Kellergangtür bei Abschluss von außen von innen jederzeit ohne Schlüssel öffenbar sein muss; Zulässigkeit A vs. B an Rettungsweg- vs. Nicht-Rettungswegtüren; bei A Stromlos-Verhalten des Öffners und Montage nur durch Elektrofachbetrieb; bei B Keypad außen und Consumer-Aufsatz an Gemeinschaftstüren. Eine produktbezogene Freigabe „Nuki“ oder „UniFi“ ist nicht nötig.

Zusätzlich **technisch** (nicht Police, aber Haftpflicht-relevant) von Postbau/Brandschutz:

- Welche Türen im Ausschnitt UG/DG sind Rettungsweg?
- Kellergang: Widerspruch „kein Fluchtweg / richtig ausgeführt“ vs. Beobachtung Einsperrung — bitte am Schloss vorführen.
- Glastüren Hof: Bestätigung keine elektrische Verriegelung.

---

## 8. Was der Verein selbst an die Vereins-Haftpflicht schreibt

> Der Bewohnerverein betreibt Anny-Buchungen (Apartment, später Musik-/Kreativ-/Veranstaltungsraum, max. Auslegung Gemeinschaftsraum 100 Personen). Geplant ist automatischer, zeitlich begrenzter Gästezutritt per PIN/App. Pilot nur Apartment-Tür; Gemeinschaftstüren erst nach Abstimmung mit der Postbaugenossenschaft. Bitte mitteilen, ob die Vereins-Haftpflicht diesen Gästezutritt deckt, ob Nachmeldung nötig ist und welche Auflagen für Veranstaltungen gelten. Gebäudeversicherung läuft über die Genossenschaft.

---

## 9. Reihenfolge

1. Kellergang **Einsperrung** und Rettungswegplan — Haftpflicht/Brandschutz, ohne Produktwahl.
2. Vereins-Haftpflicht: Anny-Gäste Apartment (Pilot).
3. Gebäudeversicherung: Anzeige Keypad/Leser; UniFi nur mit Fachbetrieb-Zusage.
4. Erst dann Montage Gemeinschaftstüren; Glastüren Hof nie.

Nuki vs. UniFi entscheidet die Versicherung nicht als Marke. Sie entscheidet **Elektrik-Eingriff**, **Flucht/Panik**, **Gäste-Schließmittel** und **welche Tür**.
