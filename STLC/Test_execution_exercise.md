
### 1. Altersverifikation
Testdurchführung 18.11.2026

| ID | Eingabe | Erwartet | Ergebnis |
|---|---|---|---|
| Age-Pop-1 | User eingeloggt, Geburtsdatum gespeichert, Zugriffversuch auf Shop| kein Popup ||
| Age-Pop-2 | User eingeloggt, Geburtsdatum nicht gespeichert, Zugriffversuch auf Shop| Popup erscheint ||
| Age-Pop-3 | User nicht eingeloggt, Geburtsdatum nicht gespeichert, Zugriffversuch auf Shop| Popup erscheint ||
| Age-Pop-4 | User nicht eingeloggt, - , Zugriffversuch auf Shop | Popup erscheint ||
| Age-Pop-5 | Kein Zugriffsversuch auf Shopseite | kein Popup ||
| Age-Val-6 | 18.11.2008 | Alkohol mit angezeigt ||
| Age-Val-7 | 19.11.2008 | Alkohol ausgeblendet ||
| Age-Val-8 | 17.11.2008 | Alkohol mit angezeigt ||
| Age-Val-9 | 18.11.1876 | Alkohol mit angezeigt ||
| Age-Val-10 | 18.11.1875 | Fehlermeldung (ungültiges Datum) ||
| Age-Val-11 | 19.11.2026 | Fehlermeldung (ungültiges Datum) ||
| Age-Val-12 | 18.11.2026 | Alkohol ausgeblendet ||
| Age-Val-13 | 40.13.2026 | Fehlermeldung (ungültiges Datum) ||
| Age-Val-14 | achtzehn | Fehlermeldung (ungültiges Datum) ||
