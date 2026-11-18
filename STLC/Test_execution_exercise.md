Testdurchführung 18.11.2026


### 1. Altersverifikation

Tests zum Erscheinen des Alterspopup
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Age-Pop-1 | User eingeloggt, Geburtsdatum gespeichert, Zugriffversuch auf Shop| kein Popup ||
| Age-Pop-2 | User eingeloggt, Geburtsdatum nicht gespeichert, Zugriffversuch auf Shop| Popup erscheint ||
| Age-Pop-3 | User nicht eingeloggt, Geburtsdatum nicht gespeichert, Zugriffversuch auf Shop| Popup erscheint ||
| Age-Pop-4 | User nicht eingeloggt, - , Zugriffversuch auf Shop | Popup erscheint ||
| Age-Pop-5 | Kein Zugriffsversuch auf Shopseite | kein Popup ||

Tests zur Geburtsdatumseingabe
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Age-Val-1 | 18.11.2008 | Alkohol mit angezeigt ||
| Age-Val-2 | 19.11.2008 | Alkohol ausgeblendet ||
| Age-Val-3 | 17.11.2008 | Alkohol mit angezeigt ||
| Age-Val-4 | 18.11.1876 | Alkohol mit angezeigt ||
| Age-Val-5 | 18.11.1875 | Fehlermeldung (ungültiges Datum) ||
| Age-Val-6 | 19.11.2026 | Fehlermeldung (ungültiges Datum) ||
| Age-Val-7 | 18.11.2026 | Alkohol ausgeblendet ||
| Age-Val-8 | 40.13.2026 | Fehlermeldung (ungültiges Datum) ||
| Age-Val-9 | achtzehn | Fehlermeldung (ungültiges Datum) ||

Fehlerangriff um Geburtsdatum erneut einzugeben
- Aus- und wieder einloggen
- Seite neulade
- Cookys löschen
- Anderer Browser
- Inkognito-Fenster
- Anderes Gerät

Checkliste um mit Useraccount unter 18 auf alkoholische Produkte zuzugreifen
[] In der Shop Produktübersicht sind keine alkoholischen Produkte
[] Die Kategorie Alkohol zeigt 0 Produkte
[] Direktlinks zu Produktseiten mit der alkoholischen Produkten zeigen "Produkt nicht Verfügbar"-Seite an


### 2. Bewertungssystem

Tests zum Abgeben einer Rezension
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Rec-Val-1 | User eingeloggt, Produkt gekauft, bisher keine Rezension | Rezension-Button sichtbar ||
| Rec-Val-2 | User eingeloggt, Produkt gekauft, bereits eine Rezension | Rezension-Button nicht sichtbar ||
| Rec-Val-3 | User eingeloggt, Produkt nicht gekauft | Rezension-Button nicht sichtbar ||
| Rec-Val-4 | User nicht eingeloggt | Rezension-Button nicht sichtbar ||

Tests zur Vergabe der Sterne
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Rec-Sta-1 | 0 | Absenden Button nicht klickbar ||
| Rec-Sta-2 | 1 | Absenden Button klickbar ||
| Rec-Sta-3 | 5 | Absenden Button klickbar ||
| Rec-Sta-4 | 6 | sollte nicht möglich sein ||

Zustandsübergangstests zum Bewertungsvorgang
| ID | Aktueller Zustand | Ereignis | Erwarteter Zustand | Ergebnis |
|---|---|---|---|---|
| Rec-Flo-1 | 0 Sterne | Klick auf 2 Sterne | 2 Sterne vergeben ||
| Rec-Flo-2 | 0 Sterne | Klick auf Absenden | Button nicht aktiv ||
| Rec-Flo-3 | 2 Sterne | Klick auf 5 Sterne | 5 Sterne vergeben ||
| Rec-Flo-4 | 5 Sterne | Klick auf Absenden | Bewertung abgesendet / Weiterleitung zu Produktseite mit neuer Bewertung ||

Tests zur Freitext-Eingabe
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Rec-Txt-1 | (leer) | Eingabe akzeptiert ||
| Rec-Txt-2 | "Das ist ein längerer Eingabetext" | Eingabe akzeptiert ||
| Rec-Txt-3 | "Das sind 501 Zeichen: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed voluptua. At vero et accusam et justo duo dolores et ea rebum. Stet clita kasden no sea takimata sanctus est Lorem ipsum dolor amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea" | Absenden Button grau, Wahrnung ||
| Rec-Txt-4 | "Bären, Rüben, Höhrer, Lindstrøm, déjà, forêt" | Eingabe akzeptiert, Zeichendarstellung korrekt ||
| Rec-Txt-5 | "汉字 / 漢字" | Eingabe akzeptiert, Darstellungsprobleme toleriert ||
| Rec-Txt-6 | "(<script>alert(1)</script>)" | Eingabe nicht akzeptiert ||

Tests zur nachträglichen Bearbeitung
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Rec-Edt-1 | User eingeloggt, Kommentar erstellt | Kommentar bearbeitbar/löschbar ||
| Rec-Edt-2 | User eingeloggt, Kommentar nicht erstellt | Kommentar nicht bearbeitbar/löschbar ||
| Rec-Edt-3 | User nicht eingeloggt | Kommentar nicht bearbeitbar/löschbar ||

Checkliste zur Darstellung der Bewertung
[] Die Bewertung wird ohne Fehlermeldung abgesendet und der Dialog schließt sich.
[] Die Gesamtanzahl der abgegebenen Stimmen in Klammern erhöht sich um +1 (von 21 auf 22).
[] Der Gesamt-Mittelwert der Sterne wird basierend auf der neuen Note (1 Stern) neu berechnet und angepasst.
[] Die neue Bewertung erscheint direkt an erster Stelle in der Rezensionsliste unter dem Produkt.


### 3. Versandkostenkalkulation

Tests zur Versandkostenkalkulation
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Shp-Cal-1 | Warenkorb füllen bis 19,99€ | 5€ Versandkosten ||
| Shp-Cal-2 | Warenkorb füllen auf 20,00€ | 0€ Versandkosten ||
| Shp-Cal-3 | Warenkorb füllen auf 20,01€ | 0€ Versandkosten ||

Zustandsübergangstest zur Versandkostenkalkulation
| ID | Aktueller Zustand | Ereignis | Erwarteter Zustand | Ergebnis |
|---|---|---|---|---|
| Shp-Flo-1 | Warenkorbwert 0€ | Artikel für 15€ hinzufügen | Warenkorbwert 15€, Versand 5€ Hinweis sichtbar ||
| Shp-Flo-2 | Warenkorbwert 15€ | Artikel für 10€ hinzufügen | Warenkorbwert 25€, Versand 0€ Hinweis nicht sichtbar ||
| Shp-Flo-3 | Warenkorbwert 25€ | Artikel für 7€ entfernen | Warenkorbwert 18€, Versand 5€ Hinweis sichtbar ||
| Shp-Flo-4 |  Warenkorbwert 25€ | Alle Artikel aus Warenkorb löschen | Warenkorbwert 0€, Versand 5€ Hinweis sichtbar ||

Fehlerangriff zu Versandkostenberechnung
- Mehrfach-Klicks: Sehr schnelles mehrmaliges Klicken auf „Artikel löschen“ und schnell Bestellen.
- Gleichzeitige Tabs: Den Warenkorb in zwei Browser-Tabs öffnen. In Tab 1 einen Artikel löschen (unter 20 € fallen) und in Tab 2 direkt auf „Zur Kasse“ klicken.

### Performancetest
