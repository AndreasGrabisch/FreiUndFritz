# Plan: Zutritt Nuki vs. UniFi (Vorhaltung Postbau)

Auswertung der Mail von Jörg Gröpke und Vorgehen, um die Machbarkeit zu klären.

## 1. Was die Antwort bereits festlegt

| Punkt | Bedeutung für uns |
|---|---|
| Flucht-/Rettungswege UG + DG im Brandschutznachweis | Gemeinschaftsraumtüren können Rettungswegtüren sein. Elektronik darf die **Panik von innen** nicht einschränken. |
| Kellergangtür Hof **kein** Fluchtweg | Technisch der unkritischste Kandidat (auch für Nuki). Hofzugang über Treppen bis Ende Nachbar-Bau gesperrt. |
| Vorhaltung je Tür: 230 V + CAT 7 + Y-ST-Y im Edelstahlkasten, plus Ader zum **elektrischen Türöffner** | Das ist eine klassische Infrastruktur für Zutrittssteuerung am **Türöffner**, nicht für ein Zylinder-Smart-Lock. |
| Panikschlösser müssen bleiben, Zylindertausch möglich | UniFi: Schloss unangetastet, nur Öffner schalten. Nuki: greift am Zylinder, Konflikt mit Panik möglich. |
| Großer Raum max. 100 Personen | Eventuell Versammlungsstättenrecht; Türen/Flucht nicht „smart“ verbauen ohne Freigabe. |
| Nuki unbekannt; Frage Versicherung | Wir formulieren die Versicherungsfragen **bauartbezogen**, nicht produktbezogen. |
| Terminangebot Mo/Di/Do Nachmittag | Annehmen. Vor-Ort-Check ist der eigentliche Entscheidungspunkt. |

Schema-PDF (`Zugangsschema_WUP.pdf`) beim Termin mitführen und Adern/Klemmen gegen das Schema prüfen.

## 2. Zwei Systeme – was sie wirklich tun

### UniFi Access (bzw. vergleichbare Zutrittssteuerung)

Passt zur Vorhaltung.

- CAT 7: PoE++ vom Schrank im großen Gemeinschaftsraum zum **Access Hub** im Edelstahlkasten (oder PoE-Injektor an 230 V, falls noch kein PoE-Switch da ist).
- Vorhandener elektrischer Türöffner: Hub schaltet ihn (potentialfreier Kontakt oder 12 V, je nach Öffner).
- Y-ST-Y: Reserve für Türkontakt, Austrittstaster, Klingel, oder Öffnerleitung falls der Hub im Schrank sitzt.
- Panikbeschlag bleibt mechanisch. Von innen immer raus; von außen nur mit Berechtigung.
- App/API: UniFi Access hat eine API – anschließbar an FreiUndFritz/Anny, etwas mehr Integrationsaufwand als Nuki.
- Zusätzlich nötig: UniFi-Konsole (z. B. Cloud Gateway), PoE++-Switch, je Tür Hub + Leser, ggf. Türkontakt.

**Risiken:** Kasten zu klein für Hub; Öffner 6/24 V AC statt 12 V DC; CAT 7 endet nicht patchbar; Rettungsweg verlangt „stromlos auf“ oder BMA-Zwangsöffnung; kein UniFi-Netz vorhanden.

### Nuki Smart Lock (Zylinder)

Andere Architektur – nutzt die Vorhaltung **nicht**.

- Sitzt innen auf dem Profilzylinder, dreht elektrisch, Batterie, Bluetooth/WLAN, fertige Web-API (gut für FreiUndFritz).
- Elektrischer Türöffner, CAT 7 und Y-ST-Y bleiben ungenutzt.
- Nuki **Opener** ist für Gegensprechanlagen, nicht für diese Vorhaltung.
- Panikschlösser: oft kein geeigneter Innenzylinder, oder das Gerät stört die Notfunktion. Nuki verlangt Zylinder mit Not- und Gefahrenfunktion.
- An **Rettungswegtüren** in Gemeinschaftsräumen (bis 100 Personen) ist ein Consumer-Smart-Lock versicherungs- und brandschutzseitig meist ungeeignet.
- An der **Kellergangtür** (kein Fluchtweg) eher denkbar, aber uneinheitliches System.

**Zwischenstand:** Vorhaltung spricht klar für UniFi (oder Siedle/Gira/Salto o. ä.). Nuki nur prüfen als Plan B an Nicht-Rettungswegtüren oder wenn der Öffner unbrauchbar ist.

## 3. Entscheidungsablauf

```
Termin vor Ort (Gröpke)
        │
        ▼
Bestandsaufnahme 4 Türen + Schrank + Kästen
        │
        ├─ Rettungsweg? ── ja ──► Nuki am Zylinder voraussichtlich raus
        │                         UniFi nur mit Fail-Verhalten laut Brandschutz
        │
        ├─ Öffner-Typ / Spannung / Fail-Secure?
        ├─ Kastenmaß / Hutschiene / Klemmung CAT7?
        └─ Zylinder/Panik für Nuki überhaupt montierbar?
        │
        ▼
Kurzmemo + Foto-Protokoll
        │
        ├─ Versicherung/Brandschutz (Fragen siehe Mail)
        └─ Netz: UniFi-Konsole, PoE-Budget, VLAN
        │
        ▼
Empfehlung: UniFi auf Vorhaltung  |  Hybrid  |  andere Zutrittsmarke
        │
        ▼
Pilot 1 Tür (idealerweise Kellergang, weil kein Fluchtweg)
dann 3 Veranstaltungsräume
```

## 4. Checkliste Vor-Ort-Termin

Technik (Fotos + Notizen, nichts demontieren außer Kasten öffnen lassen):

1. **Edelstahlkasten:** Innenmaß, Hutschiene, Reihenklemmen, Beschriftung, Platz für Access Hub (~190×126×33 mm plus Reserve).
2. **CAT 7:** geschirmt? RJ45 bereits konfektioniert? Durchgang zum Verteilerschrank? Patchfeld vorhanden?
3. **230 V:** dauerhaft, abgesichert, FI, ob für PoE-Injektor nutzbar (kein 230 V an den UniFi-Hub!).
4. **Y-ST-Y:** Aderzahl (z. B. 2×2×0,8), Belegung laut Schema, ob Öffner darüber oder über separate Türader läuft.
5. **Türöffner:** Hersteller/Typ, AC oder DC, Spannung, Ruhestrom (stromlos auf) oder Arbeitsstrom (stromlos zu). Das ist die wichtigste Hardwarefrage.
6. **Schloss:** Panik nach EN 179 (Drücker) oder EN 1125 (Stange)? Hersteller? Zylinder von innen sichtbar (Nuki braucht Überstand)?
7. **Tür:** Feuer-/Rauchschutztür (T30/RS)? Obentürschließer? vorhandener Magnetkontakt?
8. **Verteilerschrank großer Raum:** Platz für Switch 8× PoE++, Strom, Lüftung, bestehendes LAN/Glasfaser ins Haus.
9. **WLAN/LTE** an den Türen (nur relevant falls Nuki).
10. **Welche vier Türen** genau (Bezeichnung im Schema vs. Brandschutzplan).

Mitbringen: Schema-PDF, Brandschutz-Ausschnitte, Maßband, Taschenlampe, Spannungstester nur durch Fachkraft, Handy für Fotos.

## 5. Klärung nach dem Termin (ohne Gröpke)

| Frage | Wer |
|---|---|
| Darf der Öffner fail-secure bleiben? BMA-Zwangsentriegelung? | Brandschutzplaner / Versicherung über Gröpke oder HV |
| UniFi-Netz im Haus vorhanden? VLAN, Internet, wer administriert? | Haus / IT / ggf. wir |
| Budget 4 Türen: Gateway + PoE-Switch + 4× Hub + 4× Leser + Montage | Angebot Elektriker/Systemintegrator |
| API: UniFi Access Unlock per REST für Anny-Buchung | wir (FreiUndFritz) |
| Nuki-Restfall Kellergang: Zylindermaß, Panik, Haftung Batterie leer | nur wenn UniFi am Öffner scheitert |

Grobe Orientierung Hardware UniFi (ohne Montage, Stand grob): 1 Konsole + 1 PoE++-Switch + 4 Door Hubs + 4 Reader = oft vierstelliger Betrag, plus Elektriker. Nuki 4× Smart Lock Pro ist billiger in der Anschaffung, aber brandschutzlich und betrieblich (Batterie, kein Türöffner, uneinheitlich) teurer im Risiko.

## 6. Pilotlogik

1. **Kellergangtür zuerst**, weil ausdrücklich kein Fluchtweg: Öffner ansteuern, Fail-Secure testen, App-Öffnen, Panik von innen unverändert.
2. Erst danach Gemeinschaftsräume, nachdem Brandschutz die Rettungswegtüren schriftlich einordnet.
3. Kein Zylindertausch an Rettungswegtüren, bevor Versicherung/Brandschutz Nuki-artig ausschließt oder zulässt.

## 7. Was genau mit Versicherungen (und Brandschutz) zu klären ist

Gröpkes Frage „Was sollten wir mit unserer Versicherung abklären?“ vermischt zwei Stellen. Beides schriftlich, **getrennt nach Tür** (drei Veranstaltungsräume vs. Kellergang, weil nur die Kellergangtür laut Postbau kein Fluchtweg ist).

| Stelle | Zuständig | Thema |
|---|---|---|
| Brandschutznachweis / Prüfingenieur | Postbau / Brandschutzplaner | Rettungsweg, Panik, stromlos auf/zu, BMA, 100 Personen |
| Gebäudeversicherung | Versicherungsnehmer Gebäude (oft WEG / Eigentümer) | Einbruch, Schlossänderung, Obliegenheiten |
| Haus- und Grundbesitzerhaftpflicht | derselbe oder HV | Personenschaden (eingesperrt) und unbefugter Zutritt |
| Betrieb / Veranstalter | wer Anny-Buchungen und Türen betreibt (FreiUndFritz) | Gäste, Remote-Öffnen, Schlüsselersatz |

Marke Nuki oder UniFi muss die Versicherung nicht „zertifizieren“. Sie muss die **Bauart** und den **Betrieb** (wer darf öffnen, was passiert bei Strom-/Batterieausfall) kennen.

### 7.1 Gemeinsam für beide Varianten

1. **Wer ist Versicherungsnehmer**, und welche Policen gelten für die Gemeinschaftsräume (Gebäude, Haftpflicht, ggf. Veranstaltungen)?
2. **Je Tür:** Rettungsweg ja/nein laut Brandschutznachweis (UG/DG-Ausschnitte). Kellergang Hof: Postbau sagt nein – das sollte die Versicherung/der Brandschutzplaner bestätigen.
3. Bleibt die **Panik von innen ohne Strom und ohne App** uneingeschränkt (EN 179 / EN 1125)?
4. Großer Raum **bis 100 Personen:** gilt etwas aus der Versammlungsstättenverordnung für die Türen (Zwangsentriegelung, Kennzeichnung)?
5. **Fernöffnen** über App/Cloud (Anny-Buchung → kurzer Unlock): ist das mitversichert, oder gilt das als unkontrollierte Schlüsselweitergabe?
6. **Gäste / Bewohner ohne physischen Schlüssel:** Obliegenheit „Schlüssel nur an bekannte Personen“?
7. Wer haftet bei **falsch erteiltem Zutritt** (Buchung falsch, Konto gehackt, Tür bleibt offen)?
8. Ist die Montage eine **anzeigepflichtige Änderung** am Schloss (Einbruchschutz, RC-Klasse, Feuer-/Rauchschutztür)?
9. Muss die Lösung **VdS-gelistet** sein, oder reicht CE/bestimmungsgemäße Verwendung?

### 7.2 Nur UniFi (Zutritt über vorhandenen Türöffner)

Kurzbeschreibung für den Versicherer: *Netzwerksteuergerät im Edelstahlkasten schaltet den bereits geplanten elektrischen Türöffner. Mechanisches Panikschloss bleibt. Von außen nur mit Berechtigung, von innen immer über den Beschlag.*

Klären:

1. Ist diese Nutzung der **Vorhaltung** mit dem Brandschutznachweis und der Police vereinbar?
2. **Fail-Secure (stromlos zu)** vs. **Fail-Safe (stromlos auf):** darf der Öffner bei Stromausfall von außen verriegelt bleiben? An Rettungswegtüren oft nur mit funktionierender Panik und ggf. BMA-Zwangsoffnung.
3. Ist eine **Aufschaltung auf die Brandmeldeanlage** (Entriegeln im Alarm) vorgeschrieben?
4. Darf ein **nicht VdS-gelistetes** System (UniFi Access ist typischerweise Gebäudetechnik, keine VdS-Einbruchmeldezentrale) an diesen Türen verwendet werden?
5. Zusatzteile außen (Leser, Verkabelung) an einer **T30/RS-Tür:** bleibt die Zulassung der Tür?
6. **Netz-/Cloud-Ausfall:** Tür bleibt mechanisch wie bisher (Panik innen, von außen zu). Reicht das der Haftpflicht?
7. Installation durch **Elektrofachkraft** vs. Laien: Obliegenheit?
8. Protokollierung von Öffnungen: Datenschutz ist keine Versicherungsfrage, aber „wer war drin“ kann bei Schäden relevant sein.

Erwartbares Ergebnis: UniFi an der Vorhaltung ist der Weg, den Brandschutz und Gebäudeversicherung am ehesten akzeptieren – **wenn** Panik unangetastet bleibt und das Stromlos-Verhalten je Rettungswegtür passt.

### 7.3 Nur Nuki (Smart Lock am Zylinder)

Kurzbeschreibung für den Versicherer: *Batteriebetriebenes Nachrüstgerät auf der Innenseite dreht den Profilzylinder. Der elektrische Türöffner wird nicht genutzt. Fernöffnen per App/Cloud. Keine bauaufsichtliche Zulassung als Fluchttürverschluss.*

Klären:

1. Ist ein **Consumer-Smart-Lock am Zylinder** an den Gemeinschaftsraumtüren (mögliche Rettungswege, Aufenthalt bis 100 Personen) ausgeschlossen?
2. An der **Kellergangtür** (kein Fluchtweg) gesondert: zulässig oder auch dort unerwünscht?
3. Bleibt die **Not- und Gefahrenfunktion** des Zylinders erhalten, und blockiert das Gerät den Panikbeschlag in keiner Stellung (auch bei leerer Batterie / festsitzendem Motor)?
4. **Bestimmungsgemäße Verwendung:** Nuki ist für Wohnungsabschlüsse ausgelegt. Gemeinschafts-/Veranstaltungsbetrieb – Deckungsschutz ja oder nein?
5. **Einbruch / RC:** Nachrüstung auf dem Zylinder – entfällt der Schutz oder eine vereinbarte Schließanlage?
6. **Leere Batterie / Defekt:** Tür bleibt zu (Aussperrung, ggf. Menschen im Raum ohne funktionierenden Drehvorgang) oder last-state. Wer haftet, welcher Notöffnungsprozess gilt?
7. **Mechanischer Notschlüssel:** wie viele, wer verwahrt sie, gilt Schlüsselverlust-Klausel analog?
8. **Cloud-Account Nuki:** Remote-Unlock ohne Buchung, geteilte Logins, ehemaliger Admin mit Zugriff – Obliegenheit „Sorgfalt Schließmittel“?
9. Verstößt der Verzicht auf den **geplanten Türöffner** gegen eine Annahme im Brandschutznachweis oder in der Bauabnahme?
10. WEG/Eigentümer: gilt der Aufsatz als **bauliche Veränderung** (das ist oft zuerst Eigentümerbeschluss, dann Versicherung)?

Erwartbares Ergebnis: Nuki an Rettungsweg-/Gemeinschaftstüren wird häufig **abgelehnt**. An der Kellergangtür denkbar, aber schriftlich und getrennt fragen.

### 7.4 Formulierung zum Durchreichen (eine Seite)

Bitte nicht „Ist Nuki versichert?“, sondern:

> Wir erwägen zwei Arten elektronischen Zutritts an vier Türen (drei Veranstaltungsräume, eine Kellergangtür in den Hof, letztere laut Brandschutznachweis kein Fluchtweg). Variante A: Ansteuerung des vorhandenen elektrischen Türöffners, Panikschloss unverändert. Variante B: batteriebetriebenes Smart Lock auf dem Profilzylinder. Der große Gemeinschaftsraum ist bis 100 Personen ausgelegt. Bitte teilen Sie schriftlich mit, ob und unter welchen Auflagen A und B jeweils versichert sind (Gebäude und Haftpflicht), getrennt nach Rettungswegtür und Kellergang, insbesondere Verhalten bei Strom- bzw. Batterieausfall, Panikfunktion, Fernöffnen per App sowie Zutritt für zeitlich begrenzte Gäste.

## 8. Empfehlung an uns (heute, vor dem Termin)

- Termin **annehmen**, Vorhaltung erklären lassen.
- Im Gespräch UniFi (oder „Zutritt über den vorhandenen Türöffner“) als Leitvariante nennen, Nuki als Produktnamen nur erklären, nicht als Wunsch verbauen lassen.
- Schriftliche Brandschutz-/Versicherungsklärung anstoßen (siehe `antwort-groepke.md`).
- Keine Bestellung, bevor Öffner-Spannung und Rettungsweg je Tür klar sind.
