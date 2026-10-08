# Entscheidungstabellen

Das Szenario betrifft ein Zugticket-System mit verschiedenen Rabatten.


Die Bedingungen für die Anwendung eines Rabatts sind:

1. Der Fahrgast ist Senior (65 Jahre oder älter): 20 % Rabatt
2. Der Fahrgast ist Student: 15 % Rabatt
3. Der Fahrgast reist außerhalb der Hauptverkehrszeiten: 10 % Rabatt
4. Der Fahrgast besitzt eine Vielfahrerkarte: 5 % Rabatt

*Rabatte können kombiniert werden, und der Gesamtrabatt ist die Summe aller zutreffenden Rabatte.*

---

### Aufgaben:

- Alle Bedingungen zu identifizieren, die die Anwendung eines Rabatts beeinflussen
- Den Rabattprozentsatz für jede Bedingung bestimmen
- Eine Entscheidungstabelle mit allen möglichen Kombinationen der Bedingungen erstellen
- Den Gesamtrabatt für jede Kombination basierend auf den erfüllten Bedingungen berechnen

---

Das Ergebnis: Eine Entscheidungstabelle mit den Bedingungen und dem Rabattprozentsatz in der Kopfzeile, sowie dem Gesammtrabatt in der letzten Spalte

| Senior (20%) | Student (15%) | Nebenreisezeit (10%) | Rabattkarte (5%) | Gesamtrabatt |
| ---          | ---           | ---                  | ---              | ---          |
| x            |               |                      |                  | 20%          |
|              | x             |                      |                  | 15%          |
|              |               | x                    |                  | 10%          |
|              |               |                      | x                |  5%          |
| x            | x             |                      |                  | 35%          |
| x            |               | x                    |                  | 30%          |
| x            |               |                      | x                | 25%          |
|              | x             | x                    |                  | 25%          |
|              | x             |                      | x                | 20%          |
|              |               | x                    | x                | 15%          |
| x            | x             | x                    |                  | 45%          |
|              | x             | x                    | x                | 30%          |
| x            | x             |                      | x                | 40%          |
| x            |               | x                    | x                | 35%          |
| x            | x             | x                    | x                | 50%          |
|              |               |                      |                  |  0%          |

*Kommentar: Auch ungewöhnliche Kombinationen, wie ein Student über 65 Jahre wurden der Vollständigkeit halber berücksichtigt. Bei der Priorisierung der Tests könnten diese Kombinationen runter priorisiert werden.
