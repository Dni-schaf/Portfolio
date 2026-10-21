# Testplan & Testfallentwurf

## Aufgabe
Erstelle deinen eigenen Testplan für die neuen Funktionen des Webshops!

---

## **1. Produktanalyse**

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

## **2. Teststrategie entwerfen**

**Testumfang (Scope of Testing)**

- **Im Umfang enthalten:**
    
    <aside>
    💡
    
    *Welche Funktionalitäten werden getestet?*
    
    </aside>
    
- **Nicht im Umfang enthalten:**
    
    <aside>
    💡
    
    *Was ist vom Test ausgeschlossen?*
    
    </aside>
    

**Geplante Testarten**

<aside>
💡

*Welche Testarten werden für die neuen Funktionen benötigt?*

</aside>

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
- **QA Engineer (Performance & Sicherheit)** – Alice Johnson
- **QA Engineer (Usability)** – Robert Brown
- **Endanwender für UAT (User Acceptance Test)** – Maria Garcia

---

## **3. Testziele definieren**

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

## **4. Testkriterien definieren**

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

## **5. Ressourcenplanung**

- **Personelle Ressourcen:** QA-Team, Entwicklerteam, Endanwender für UAT
- **Hardware:** PCs, Laptops, Smartphones, Tablets
- **Software:** Aktuelle Browser (Chrome, Firefox, Safari, Edge), Betriebssysteme (Windows, macOS, Android, iOS)
- **Infrastruktur:** Testumgebungen, Automatisierungs-Tools, Performanztest-Werkzeuge

---

## **6. Testumgebung planen**

- **Testgeräte:** Echte Endgeräte mit real installierten Betriebssystemen und Browsern zur realitätsnahen Simulation
- **Umgebungen:**
    - Entwicklung (DEV)
    - Test (TEST)
    - Abnahme (ACC – Acceptance)
    - Produktion (PROD)
    
    ---
    
    ## **7. Zeitplan und Aufwandsschätzung**
    

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

## **8. Testartefakte (Test-Deliverables)**

Folgende Dokumente und Werkzeuge werden im Rahmen des Testprozesses erstellt und bereitgestellt:

- Testplandokument
- Testfälle und Testskripte
- Testdaten
- Testberichte
- Fehlerberichte (Defect Reports)
- UAT-Freigabedokumentation (Sign-off)
