# Übungsaufgabe: Zustandsübergangstest

**Das Szenario beinhaltet einen Geldautomaten (ATM). Um diesen Automaten zu benutzen, muss der Benutzer seine PIN eingeben.**

Der Benutzer sieht zuerst den Startbildschirm, dann den Bildschirm „Warte auf PIN“. Danach sind 3 Versuche möglich. Wenn der PIN-Code korrekt ist, hat der Benutzer Zugriff auf das Konto. Wenn der Benutzer die maximale Anzahl an Versuchen überschreitet, wird die Karte eingezogen.

**Aufgabe:**

1. Bestimme die Zustände, Übergänge und Ereignisse
2. Erstelle die Zustandsübergangstabelle und das Zustandsübergangsdiagramm

---

| State | Action | New State|
| :--- | :--- | :--- |
| Start-Screen	| Karte eingeben | PIN-Screen (Versuch 1) |
|  PIN-Screen (Versuch 1)	| richtigen PIN eingeben | Konto-Screen |
|  PIN-Screen (Versuch 1)	| falschen PIN eingeben |  PIN-Screen (Versuch 2) |
|  PIN-Screen (Versuch 1)	| Vorgang abbrechen | Start-Screen |
|  PIN-Screen (Versuch 2)	| richtigen PIN eingeben | Konto-Screen |
|  PIN-Screen (Versuch 2)	| falschen PIN eingeben |  PIN-Screen (Versuch 3) |
|  PIN-Screen (Versuch 2)	| Vorgang abbrechen | Start-Screen |
|  PIN-Screen (Versuch 3)	| richtigen PIN eingeben | Konto-Screen |
|  PIN-Screen (Versuch 3)	| falschen PIN eingeben |  Karte-wird-eingezogen-Screen |
|  PIN-Screen (Versuch 3)	| Vorgang abbrechen | Start-Screen |
