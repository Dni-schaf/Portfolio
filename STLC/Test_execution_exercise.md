Testdurchführung 18.11.2026


### 1. Altersverifikation

Tests zum Erscheinen des Alterspopup
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Age-Pop-1 | User eingeloggt, Geburtsdatum gespeichert, Zugriffversuch auf Shop| kein Popup | pass |
| Age-Pop-2 | User eingeloggt, Geburtsdatum nicht gespeichert, Zugriffversuch auf Shop| Popup erscheint | pass |
| Age-Pop-5 | User nicht eingeloggt, Zugriffversuch auf Shop | Popup erscheint | pass |
| Age-Pop-6 | Kein Zugriffsversuch auf Shopseite | kein Popup | pass |

Tests zur Geburtsdatumseingabe
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Age-Val-1 | 18-11-2008 | Alkohol mit angezeigt | pass |
| Age-Val-2 | 19-11-2008 | Alkohol ausgeblendet | pass |
| Age-Val-3 | 17-11-2008 | Alkohol mit angezeigt | pass |
| Age-Val-4 | 18-11-1876 | Alkohol mit angezeigt | pass |
| Age-Val-5 | 18-11-1875 | Fehlermeldung (ungültiges Datum) | FAILED |
| Age-Val-6 | 19-11-2026 | Fehlermeldung (ungültiges Datum) | FAILED (keine Fehlermeldung) |
| Age-Val-7 | 18-11-2026 | Alkohol ausgeblendet | pass |
| Age-Val-8 | 40-13-2026 | Fehlermeldung (ungültiges Datum) | FAILED (keine Fehlermeldung) |
| Age-Val-9 | achtzehn | Fehlermeldung (ungültiges Datum) | FAILED (keine Fehlermeldung) |

Fehlerangriff um Geburtsdatum erneut einzugeben
- Aus- und wieder einloggen
- Seite neulade
- Cookys löschen
- Anderer Browser
- Inkognito-Fenster
- Anderes Gerät

Checkliste um mit Useraccount unter 18 auf alkoholische Produkte zuzugreifen
- [x] In der Shop Produktübersicht sind keine alkoholischen Produkte - pass
- [x] Die Kategorie Alkohol zeigt 0 Produkte - pass
- [ ] Direktlinks zu Produktseiten mit der alkoholischen Produkten zeigen "Produkt nicht Verfügbar"-Seite an - FAILED


### 2. Bewertungssystem

Tests zum Abgeben einer Rezension
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Rec-Val-1 | User eingeloggt, Produkt gekauft, bisher keine Rezension | Rezension-Button sichtbar | pass |
| Rec-Val-2 | User eingeloggt, Produkt gekauft, bereits eine Rezension | Rezension-Button nicht sichtbar | pass |
| Rec-Val-3 | User eingeloggt, Produkt nicht gekauft | Rezension-Button nicht sichtbar | pass |
| Rec-Val-4 | User nicht eingeloggt | Rezension-Button nicht sichtbar | pass |

Tests zur Vergabe der Sterne
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Rec-Sta-1 | 0 | Absenden Button nicht klickbar | pass |
| Rec-Sta-2 | 1 | Absenden Button klickbar | pass |
| Rec-Sta-3 | 5 | Absenden Button klickbar | pass |
| Rec-Sta-4 | 6 | sollte nicht möglich sein | pass |

Zustandsübergangstests zum Bewertungsvorgang
| ID | Aktueller Zustand | Ereignis | Erwarteter Zustand | Ergebnis |
|---|---|---|---|---|
| Rec-Flo-1 | 0 Sterne | Klick auf 2 Sterne | 2 Sterne vergeben | pass |
| Rec-Flo-2 | 0 Sterne | Klick auf Absenden | Button nicht aktiv | pass |
| Rec-Flo-3 | 2 Sterne | Klick auf 5 Sterne | 5 Sterne vergeben | pass |
| Rec-Flo-4 | 5 Sterne | Klick auf Absenden | Bewertung abgesendet / Weiterleitung zu Produktseite mit neuer Bewertung | pass |

Tests zur Freitext-Eingabe
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Rec-Txt-1 | (leer) | Eingabe akzeptiert | pass |
| Rec-Txt-2 | "Das ist ein längerer Eingabetext" | Eingabe akzeptiert | pass |
| Rec-Txt-3 | "Das sind 501 Zeichen: Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed voluptua. At vero et accusam et justo duo dolores et ea rebum. Stet clita kasden no sea takimata sanctus est Lorem ipsum dolor amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea" | Absenden Button grau, Wahrnung | pass |
| Rec-Txt-4 | "Bären, Rüben, Höhrer, Lindstrøm, déjà, forêt" | Eingabe akzeptiert, Zeichendarstellung korrekt | pass |
| Rec-Txt-5 | "汉字 / 漢字" | Eingabe akzeptiert, Darstellungsprobleme toleriert | pass |
| Rec-Txt-6 | "<script>alert(1)</script>" | Eingabe nicht akzeptiert | FAILED (nicht bei Ersteingabe, aber beim edit möglich) |

Tests zur nachträglichen Bearbeitung
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Rec-Edt-1 | User eingeloggt, Kommentar erstellt | Kommentar bearbeitbar/löschbar | pass |
| Rec-Edt-2 | User eingeloggt, Kommentar nicht erstellt | Kommentar nicht bearbeitbar/löschbar | pass |
| Rec-Edt-3 | User nicht eingeloggt | Kommentar nicht bearbeitbar/löschbar | pass |

Checkliste zur Darstellung der Bewertung
- [x] Die Bewertung wird ohne Fehlermeldung abgesendet und der Dialog schließt sich. - pass
- [x] Die Gesamtanzahl der abgegebenen Stimmen in Klammern erhöht sich um +1 (von 21 auf 22). - pass
- [x] Der Gesamt-Mittelwert der Sterne wird basierend auf der neuen Note (1 Stern) neu berechnet und angepasst. - pass
- [x] Die neue Bewertung erscheint direkt an erster Stelle in der Rezensionsliste unter dem Produkt. - pass


### 3. Versandkostenkalkulation

Tests zur Versandkostenkalkulation
| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Shp-Cal-1 | Warenkorb füllen bis 19,99€ | 5€ Versandkosten | pass |
| Shp-Cal-2 | Warenkorb füllen auf 20,00€ | 0€ Versandkosten | pass |
| Shp-Cal-3 | Warenkorb füllen auf 20,01€ | 0€ Versandkosten | pass |

Zustandsübergangstest zur Versandkostenkalkulation
| ID | Aktueller Zustand | Ereignis | Erwarteter Zustand | Ergebnis |
|---|---|---|---|---|
| Shp-Flo-1 | Warenkorbwert 0€ | Artikel für 15€ hinzufügen | Warenkorbwert 15€, Versand 5€ Hinweis sichtbar | pass |
| Shp-Flo-2 | Warenkorbwert 15€ | Artikel für 10€ hinzufügen | Warenkorbwert 25€, Versand 0€ Hinweis nicht sichtbar | pass |
| Shp-Flo-3 | Warenkorbwert 25€ | Artikel für 7€ entfernen | Warenkorbwert 18€, Versand 5€ Hinweis sichtbar | FAILED |
| Shp-Flo-4 | Warenkorbwert 25€ | Alle Artikel aus Warenkorb löschen | Warenkorbwert leer | pass |

Fehlerangriff zu Versandkostenberechnung
- Mehrfach-Klicks: Sehr schnelles mehrmaliges Klicken auf „Artikel löschen“ und schnell Bestellen. - pass
- Gleichzeitige Tabs: Den Warenkorb in zwei Browser-Tabs öffnen. In Tab 1 einen Artikel löschen (unter 20 € fallen) und in Tab 2 direkt auf „Zur Kasse“ klicken. - pass

### Performancetest
