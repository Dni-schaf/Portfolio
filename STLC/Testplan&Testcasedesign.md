# Testplan & Testfallentwurf

### Aufgabe

Erstelle deinen eigenen Testplan für die neuen Funktionen des Webshops!

---
### **1. Produktanalyse**

**Zielsetzung**

Das Hauptziel des Produktes ist die Erweiterung des bestehenden Onlineshops durch neue Funktionen sowie die Gewährleistung der reibungslosen Funktionalität bereits existierender Features.

**Zielnutzergruppe**

Das Produkt richtet sich an neue und bestehende Kunden des Online-Shops wobei Nutzer unter 18 Jahre nicht Produkte aller Kategorien kaufen dürfen.

**Hardware- und Software-Spezifikationen**

- **Hardwareanforderungen:**
    - Geräte: Laptops, Smartphones, Tablets
    - Spezifikationen: Standardkonfigurationen für Android- und iOS-Geräte; Desktops mit mindestens 4 GB RAM und 2 GHz Prozessor
- **Softwareanforderungen:**
    - Betriebssysteme: Windows, Android, iOS
    - Browser: Chrome, Safari
    - Abhängigkeiten: Backend-Dienste, Drittanbieter-Werbeanbieter, Zahlungsschnittstellen

**Funktionalität des Produkts**

- Registrierung und Login
- Waren in den Warenkorb legen
- Produkte zu den Favoriten hinzufügen
- Kaufvorgang abschließen
- Altersverifikation (Neues Feature)
- Versandkostenkalkulation (Neues Feature)
- Bewertungssystem (Neues Feature)

---

### **2. Teststrategie entwerfen**

**Testumfang (Scope of Testing)**

- **Im Umfang enthalten:**
    - Registrierung & Login
    - Produkte suchen
    - Produkt zu Favouriten hinzufügen
    - Altersbeschränkung für Produkte besonderer Kategorien
    - Produkte kaufen
    - Versandkostenkalkulation
    - Produktbewertung abgeben
    
- **Nicht im Umfang enthalten:**
    - Backend-Datenbankoperationen ohne UI-Einfluss

**Geplante Testarten**
- Funktionstests
- Regressions-Tests
- Performanztests
- Sicherheitstests
- Usability-Tests

**Risiken und Gegenmaßnahmen**

- **Entwicklungsverzögerungen**
    
    → Gegenmaßnahme: Zeitpuffer im Zeitplan einplanen
    
- **Fehlende Testdaten**
    
    → Gegenmaßnahme: Erstellen von Testdaten (Mock-Daten)
    
- **Ressourcenengpässe**
    
    → Gegenmaßnahme: Ersatzpersonen identifizieren und einplanen
    

**Testlogistik (Testverantwortlichkeiten)**

- **Testmanager** – Jane Smith
- **QA Engineer (Funktion & Regression)** – John Doe
- **QA Engineer (Performance & Sicherheit)** – Alice Mustermann
- **QA Engineer (Usability)** – Alice Mustermann
- **Endanwender für UAT (User Acceptance Test)** – John Schmidt

---

### **3. Testziele definieren**

**Ziele**

- **Funktionalität:** Sicherstellen, dass neue und bestehende Funktionen wie vorgesehen arbeiten
- **Benutzeroberfläche (GUI):** Überprüfung auf Bedienbarkeit, Konsistenz und Fehlerfreiheit
- **Leistung (Performance):** Bestätigung, dass das System die erwartete Last bewältigt
- **Sicherheit:** Identifikation und Absicherung potenzieller Schwachstellen
- **Benutzbarkeit (Usability):** Bewertung der Nutzerfreundlichkeit und Zugänglichkeit

**Erwartete Ergebnisse**

- Alle Funktionen verhalten sich gemäß Spezifikation
- Die Oberfläche ist intuitiv, responsiv und fehlerfrei
- Performanzkennzahlen werden unter Last eingehalten
- Es bestehen keine sicherheitsrelevanten Schwachstellen
- Die Anwendung ist leicht bedienbar für Endnutzer

---

### **4. Testkriterien definieren**

**Aussetzungskriterien (Suspension Criteria)**

- Kritische Fehler blockieren die Fortsetzung der Tests
- Fehlende Ressourcen oder Ausfall der Testumgebung

**Abnahmekriterien (Exit Criteria)**

- Alle geplanten Tests wurden ausgeführt
- **Ausführungsrate:** Mindestens 95 % aller Testfälle wurden ausgeführt
- **Bestehensquote:** Mindestens 90 % der ausgeführten Testfälle bestanden
- Alle kritischen und hochpriorisierten Defekte sind geschlossen
- Es bestehen keine offenen Fehler der Schweregrade 1 oder 2
- Performanzanforderungen wurden erfüllt
- Sicherheitslücken wurden behoben
- Der Abnahmetest (UAT) wurde abgeschlossen und freigegeben

---

### **5. Ressourcenplanung**

- **Personelle Ressourcen:** QA-Team, Entwicklerteam, Endanwender für UAT
- **Hardware:** Laptops, Smartphones, Tablets
- **Software:** Aktuelle Browser (Chrome, Safari), Betriebssysteme (Windows, Android, iOS)
- **Infrastruktur:** Testumgebungen, Automatisierungs-Tools, Performanztest-Werkzeuge

---

### **6. Testumgebung planen**

- **Testgeräte:** Echte Endgeräte mit real installierten Betriebssystemen und Browsern zur realitätsnahen Simulation
- **Umgebungen:**
    - Entwicklung (DEV)
    - Test (TEST)
    - Abnahme (ACC – Acceptance)
    - Produktion (PROD)
    
---

### **7. Zeitplan und Aufwandsschätzung**
    

| Aktivität | Startdatum | Enddatum | Umgebung | Verantwortlich | Geplanter Aufwand |
| --- | --- | --- | --- | --- | --- |
| Testplanung | 01.08.2024 | 05.08.2024 | Alle | Testmanager | 20 Stunden |
| Testfalldesign | 06.08.2024 | 15.08.2024 | Alle | QA-Team | 40 Stunden |
| Unittest | 16.08.2024 | 25.08.2024 | DEV | Entwickler-Team | 60 Stunden |
| Integrationstest | 26.08.2024 | 30.08.2024 | TEST | QA-Team | 30 Stunden |
| Systemtest | 01.09.2024 | 10.09.2024 | TEST | QA-Team | 80 Stunden |
| Regressions-Test | 11.09.2024 | 15.09.2024 | TEST | QA-Team | 40 Stunden |
| Performanztest | 16.09.2024 | 18.09.2024 | TEST | QA-Team | 20 Stunden |
| Sicherheitstest | 19.09.2024 | 21.09.2024 | TEST | QA-Team | 20 Stunden |
| Abnahmetest (UAT) | 22.09.2024 | 30.09.2024 | ACC | Endanwender | 50 Stunden |
| Produktivfreigabe | 01.10.2024 | 01.10.2024 | PROD | DevOps-Team | 10 Stunden |

---

### **8. Testartefakte (Test-Deliverables)**

Folgende Dokumente und Werkzeuge werden im Rahmen des Testprozesses erstellt und bereitgestellt:

- Testplandokument
- Testfälle und Testskripte
- Testdaten
- Testberichte
- Fehlerberichte (Defect Reports)
- UAT-Freigabedokumentation (Sign-off)

# Testfallentwurf

### **1. Altersverifikation**
Nutzer unter 18 Jahren dürfen Produkte der Kategorien Alkohol nicht kaufen.

> Nutzen von Black-Box-Testverfahren, da Anforderungen klar und kein Zugriff auf Quellcode:
Äquivalenzklassen, Grenzwertanalysen, Entscheidungstabellen, Zustandübergangtests

**Popup-Trigger**
> - Hat der User sich eingeloggt und klickt auf den Button "Shop", geht ein Popup auf, das zum eintragen des Geburtsdatums im Format DD-MM-JJJJ auffordert.
> - Klickt ein nicht eingeloggter User auf den Button "Shop" geht ebenfalls das Popup auf.

**Altertvalidierung**
> - Unsinnige Eingaben, wie etwa ein Datum nach dem aktuellen Datum sollte abgelehnt werden, ebenso wie Daten, die ergeben, das der User über 150 Jahre alt wäre oder die nicht im erlaubten Bereich liegen. (bei Tagen 1-31, bei Monaten 1-12).
> - Bei eine unsinnigen Eingabe wird der User mit einem roten Text unter dem Eingabefeld, um ein gültiges Datum gebeten.

---

Testverfahren: Äquivalenzklassenbildung:

| Typ | Äquivalenzklasse | Altersbereich | Erwartetes Systemverhalten |
| --- | --- | --- | --- |
| Gültig | ÄK 1: Volljährig | 18 bis 150 Jahre | Datum akzeptiert, Alkohol sichtbar & kaufbar |
| Ungültig (Fachlich) | ÄK 2: Minderjährig | 0 bis < 18 Jahre (17 Jahre, 364 Tage) | Datum akzeptiert, Alkohol nicht sichtbar/kaufbar|
| Ungültig (Unsinnig - zu alt) | ÄK 3: Zu alt | > 150 Jahre | Fehlermeldung |
| Ungültig (Unsinnig - Zukunft) | ÄK 4: In der Zukunft	| < 0 Jahre (Geburtsdatum > heute)	| Fehlermeldung |
| Ungültig (Unsinnig - Wertebereich) | ÄK 5: Falscher Wertebereich für Tag oder Monat | 1 > Tage > 31 und 1 > Monat > 12 | Fehlermeldung |
| Ungültig (Unsinnig - Eingabetyp) | ÄK 6: Falscher Eingabetyp | Eingabe sind keine Zahlen | Fehlermeldung |

Testverfahren: Grenzwertanalyse (3-Werte, weil Sicherheitsrelevante Funktion, Taggenau):

- Grenzfall 18 Jahre (Erfolg): Exakt am 18. Geburtstag (aktuelles Datum - 18 Jahre).
- Grenzfall 18 Jahre (Alkohol sperre): 1 Tag jünger als 18 (aktuelles Datum + 1 Tag - 18 Jahre).
- Grenzfall 18 Jahre (Erfolg): 1 Tag älter als 18 (aktuelles Datum - 1 Tag - 18 Jahre).
- Grenzfall Höchstalter (Erfolg): 150 Jahre alt (aktuelles Datum - 150 Jahre).
- Grenzfall Höchstalter (Fehlermeldung): 151 Jahre alt (aktuelles Datum - 151 Jahre).
- Grenzfall Zukunft (Fehlermeldung): (aktuelles Datum + 1 Tag)
- Grenzfall Heute (Alkohol sperre): (aktuelles Datum)

So ergeben sich 9 Testfälle (7 um die Grenzwerte abzudecken und 2 für falscher Wertebereich und falscher Eingabetyp)

**Beispieltestfall**
- TESTFALL-ID: TC_SHOP_AGE_001
- TITEL: Geburtstagseingabe mit exakt 18 Jahren (Grenzfallprüfung)
- VORBEDINGUNGEN:
    - Test-User ist registriert, aber hat noch kein Geburtsdatum hinterlegt.
    - User ist eingeloggt.
    - User ist auf der Startseite (Home)
- TESTSCHRITTE/TESTAKTIONEN:
    - Klicke auf den Button "Shop" im Hauptmenü
    - Warte bis das Popup "Age Verification" zur Geburtstagseingabe sich öffnet
    - Trage das Datum (aktuelles Datum - 18 Jahre) im Format DD-MM-JJJJ ein.
    - Klicke auf "Confirm"
- ERWARTETES ERGEBNIS: 
    - Die Eingabe wird ohne Fehlermeldung akzeptiert und das Fenster schließt sich.
- NACHBEDINGUNGEN: 
    - Profil löschen
- RÜCKVERFOLGBARKEIT: 
    - Anforderung: "Nutzer unter 18 Jahren dürfen Produkte... nicht kaufen" / Grenzfall 18 Jahre.

---

- TESTFALL-ID: TC_SHOP_AGE_001
- TITEL: Geburtstagseingabe mit exakt 18 Jahren (Grenzfallprüfung)
- VORBEDINGUNGEN:
    - Test-User ist registriert, aber hat noch kein Geburtsdatum hinterlegt.
    - User ist eingeloggt.
    - User ist auf der Startseite (Home)
- TESTSCHRITTE/TESTAKTIONEN:
    - Klicke auf den Button "Shop" im Hauptmenü
    - Warte bis das Popup "Age Verification" zur Geburtstagseingabe sich öffnet
    - Trage das Datum (aktuelles Datum - 18 Jahre) im Format DD-MM-JJJJ ein.
    - Klicke auf "Confirm"
- ERWARTETES ERGEBNIS: 
    - Die Eingabe wird ohne Fehlermeldung akzeptiert und das Fenster schließt sich.
    - User sieht links in der Kategorie Übersicht in der Kategorie eine Anzahl an Produkten die nicht 0 ist.
    - User kann auf die Kathegorie klicken und sieht alkoholische Produkte.
    - Bei Klick auf Button "Add to Card" wird alkoholisches Produkt in den Warenkorb gelegt.
    - Klick auf Button "Warenkorb"
    - Alkoholisches Produkt ist im Warenkorb. Kaufvorgang kann abgeschlossen werden.
- NACHBEDINGUNGEN: 
    - Im Profil des Users ist dieses Geburtsdatum dauerhaft hinterlegt.
    - Profil löschen
- RÜCKVERFOLGBARKEIT: 
    - Anforderung: "Nutzer unter 18 Jahren dürfen Produkte... nicht kaufen" / Grenzfall 18 Jahre.
 

**Persistenz & Immutability**
> - Die Geburtstagseingabe wird im Profil gespeichert und ist auch nach dem aus und wieder einloggen gesichert.
> - Die Geburtstagseingabe kann nach dem initialen eingeben nicht mehr geändert werden.

**Sichtigkeitslogik**
> - ist der User unter 18 Jahre kann er Produkte der Kathegorie Alkohol weder in der Alle Produktlitse noch in der Kathegorie Alkohol sehen. 
> - Auch ein Direktlink zu einer Detailseite eines Produktes der Kategorie Alkohol sollte nicht angezeigt werden, wenn der User unter 18 ist.





1. TESTFALL-ID: 
2. Ein aussagekräftiger TITEL 
3. VORBEDINGUNGEN (Pre-conditions):
Was muss im System bereits gegeben sein, bevor du diesen Testfall überhaupt starten darfst? 
4. TESTSCHRITTE/TESTAKTIONEN (Test Actions & Inputs):   Die exakte, schrittweise Handlungsanweisung – inklusive konkreter Eingabewerte.   
5. ERWARTETES ERGEBNIS (Expected Results):Der präzise Soll-Zustand des Systems nach der Durchführung. Was muss passieren, damit der Test als bestanden gilt? 
6. NACHBEDINGUNGEN (Post-conditions): Wie sieht der Zustand des Systems nach dem Test aus? Muss etwas zurückgesetzt (Teardown) werden?
7. RÜCKVERFOLGBARKEIT (Traceability): Oft wird im Testfall auch hinterlegt, auf welche Testbedingung oder welche Anforderung (Testbasis / User Story) sich dieser Testfall bezieht.
